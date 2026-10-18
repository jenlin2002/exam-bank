/* 段考題庫 - 共用的 Google Sheet 回傳邏輯 (exam-bank/sync.js) */
// 學習點數存摺：每個頁面都載入 sync.js，所以在這裡順便載入同資料夾的 points.js（不用每頁各加一行）。
// 送出成績時 submitExamResults() 會呼叫 Points.earn()；沒有 points.js 或沒登入時什麼都不會發生。
(function(){
  const cs = document.currentScript;
  if(cs && cs.src && !window.Points){
    const s = document.createElement("script");
    s.src = new URL("points.js", cs.src).href;
    document.head.appendChild(s);
  }
})();

(function(){
  const SHEET_ENDPOINT = "https://script.google.com/macros/s/AKfycbxO7EkmhoM2Bex59yRrBJrvY9nXEHCpUGykEP0YdkvCvtSYZ4lhDPB2N6uDHO2y3uCu/exec";

  function pad(n){ return n.toString().padStart(2,"0"); }
  function nowStr(){
    const d = new Date();
    return `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`;
  }

  function sendToSheet(payload){
    return fetch(SHEET_ENDPOINT, {
      method: "POST",
      mode: "no-cors",
      headers: { "Content-Type": "text/plain;charset=utf-8" },
      body: JSON.stringify(payload)
    }).catch(()=>{});
  }

  // 目前登入的人：points.js 的「你是誰？」關卡驗證 PIN 之後，名字存在 localStorage 的 quizStudentName
  function loggedInStudent(){
    let n = "";
    try{ n = (localStorage.getItem("quizStudentName") || "").trim().toUpperCase(); }catch(e){}
    return (!n || /^訪客/.test(n)) ? "" : n;
  }

  function injectPicker(){
    if(document.getElementById("examSyncBar")) return;
    const bar = document.createElement("div");
    bar.id = "examSyncBar";
    // 右下角最下面是點數存摺的「🪙 點數」按鈕（z-index 9000），送出列要放在它上面，不然會被蓋住
    bar.style.cssText = "position:fixed;bottom:calc(70px + env(safe-area-inset-bottom,0px));right:14px;z-index:999;background:#2f4538;color:#eef2ea;"
      + "padding:10px 14px;border-radius:10px;box-shadow:0 4px 14px rgba(0,0,0,.25);"
      + "font-family:'Noto Sans TC',sans-serif;font-size:13.5px;display:flex;gap:8px;align-items:center;";
    bar.innerHTML = `
      <span id="examWho" style="font-weight:700;"></span>
      <button id="examSubmitBtn" style="background:#b5842a;color:#fff;border:none;border-radius:6px;
        padding:7px 14px;font-size:13.5px;cursor:pointer;">送出成績</button>
      <span id="examSyncStatus" style="font-size:12px;color:#cfe0d1;"></span>
    `;
    document.body.appendChild(bar);

    // 不用再選學生：成績自動記在「登入者」（用 PIN 登入點數存摺的人）名下。登入／切換帳號後這裡的名字會跟著更新。
    const who = document.getElementById("examWho");
    function showWho(){
      const n = loggedInStudent();
      who.textContent = n ? ("登入者：" + n) : "尚未登入";
      if(typeof window.refreshStudentOwnerBadge === "function"){
        window.refreshStudentOwnerBadge(n || "");
      }
    }
    showWho();
    setInterval(showWho, 1500);

    document.getElementById("examSubmitBtn").addEventListener("click", (e)=>{
      if(e.target.disabled) return; // 防止重複點擊、重複送出
      window.submitExamResults();
    });

    // 如果頁面上有「重新作答」按鈕，點下去時把送出按鈕的鎖定狀態也一併重置
    const resetBtn = document.getElementById("resetBtn");
    if(resetBtn){
      resetBtn.addEventListener("click", ()=>{
        const btn = document.getElementById("examSubmitBtn");
        const status = document.getElementById("examSyncStatus");
        btn.disabled = false;
        btn.style.opacity = "";
        btn.style.cursor = "";
        document.body.classList.remove("exam-locked");
        btn.textContent = "送出成績";
        if(status) status.textContent = "";
        clearSectionScores();
        lockPrintMode();
        fixRound = 0; pendingFix = false; clearDraft();
        const fb = document.getElementById("fixBar"); if(fb) fb.remove();
        document.querySelectorAll(".q").forEach(q=>{ q.classList.remove("fixing", "fix-locked"); delete q.dataset.firstCorrect; });
      });
    }
  }

  // 「完整題目與解答」只有送出成績後才能看（使用者 2026-10-18 發現：送出過一次後按「重新作答」，
  // 這顆沒有重新鎖住，還沒送出就能點開看到正解）。重新作答時鎖回去；正在看解答就切回測驗模式。
  function lockPrintMode(){
    const pb = document.getElementById("printModeBtn");
    if(!pb) return;
    document.body.classList.remove("answer-view");
    const qb = document.getElementById("quizModeBtn");
    if(qb) qb.classList.add("active");
    pb.classList.remove("active");
    pb.disabled = true;
    pb.title = "完成測驗並送出成績後才能查看";
  }
  // 「測驗模式／完整題目與解答」切換（使用者 2026-10-18 反映：送出後切去看解答再切回來，作答全部不見、選項鎖住、
  // 再按送出變成「還有 25 題尚未作答」）。原因是各頁面的切換程式會把整份考卷重畫一次。
  // 改成由這裡接手、不重畫：還沒送出成績不能看解答；送出後「完整題目與解答」直接在原本的作答上顯示所有正解與詳解，
  // 「測驗模式」切回來，作答、對錯、小計都還在。
  const viewStyle = document.createElement("style");
  viewStyle.textContent = "body.answer-view .explain, body.answer-view .answer-reveal{display:block !important}"
    // 送出成績後自動顯示解答（使用者 2026-10-18：「送出成績→不須按鈕，就給出解答」），所以上方的模式切換鈕不再需要
    + ".mode-toggle{display:none !important}"
    // 做錯的題目呈現紅色：題號、選錯的選項、打錯的填空／句子；答對的選項標「✓ 正解」
    + "body.exam-locked .q[data-is-correct=\"false\"] .q-num{color:#c0392b !important}"
    + "body.exam-locked .q[data-is-correct=\"false\"] input{color:#c0392b !important;border-color:#c0392b !important;font-weight:700;background:#fdecea}"
    + "body.exam-locked .opt.wrong{border-color:#c0392b !important;background:#fdecea !important;color:#c0392b !important}"
    + "body.exam-locked .opt.wrong::after{content:'  ✗ 你的答案';color:#c0392b;font-weight:800;margin-left:auto;padding-left:10px}"
    + "body.exam-locked .opt.correct::after,.q.fix-locked .opt.correct::after{content:'  ✓ 正解';color:#2e7d4f;font-weight:800;margin-left:auto;padding-left:10px}"
    // 答對的題目綠色（訂正時也一直鎖著、維持綠色）
    + "body.exam-locked .q[data-is-correct=\"true\"] input,.q.fix-locked input{color:#2e7d4f !important;border-color:#2e7d4f !important;font-weight:700;background:#e8f5ec}"
    + "body.exam-locked .q[data-is-correct=\"true\"] .q-num,.q.fix-locked .q-num{color:#2e7d4f !important}"
    + ".q.fix-locked .opt{cursor:not-allowed !important}"
    // 訂正中的題目：黃色左框＋標籤，正解先藏起來
    + ".q.fixing{border-left:4px solid #e0a020;padding-left:10px;background:#fffaf0}"
    + ".q.fixing .q-text::before{content:'✏️ 訂正 ';color:#b5761a;font-weight:800}"
    + ".q.fixing .answer-reveal,.q.fixing .explain{display:none !important}"
    + "#fixBar{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin:0 0 14px;padding:10px 14px;border-radius:12px;background:#fff4dc;border:2px solid #e7c98a;font-family:'Noto Sans TC',sans-serif}"
    + "#fixBar button{background:#c0392b;color:#fff;border:0;border-radius:999px;padding:9px 18px;font-size:15px;font-weight:800;cursor:pointer;font-family:inherit}"
    + "#fixBar button.exit{background:#fff;color:#5a4a2a;border:1.5px solid #c9b88f}"
    + "#fixBar a.exit-link{display:inline-block;padding:7px 14px;border-radius:999px;background:#2f6fb5;color:#fff;font-weight:800;text-decoration:none;font-size:14px}"
    + "#fixBar button[disabled]{background:#d8cdb4;color:#7a6a48;cursor:default}"
    + "#fixBar .note{font-size:14px;color:#6b4a12;font-weight:600}#fixBar .note b{color:#c0392b}#fixBar.done{background:#e8f5ec;border-color:#9ccfab}#fixBar.done .note{color:#1f6b3a}"
    + "#draftBar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:0 0 12px;padding:8px 12px;border-radius:12px;background:#eef4fb;border:1.5px solid #b9cde6;font-family:'Noto Sans TC',sans-serif;font-size:14px;color:#2c4a6e}"
    + "#draftBar button{border:0;border-radius:999px;padding:7px 16px;font-size:14px;font-weight:800;cursor:pointer;font-family:inherit;background:#2f6fb5;color:#fff}"
    + "#draftBar button.ghost{background:transparent;color:#2f6fb5;border:1.5px solid #9dbbe0;font-weight:700;padding:5px 12px}"
    + "body.exam-locked #draftBar{display:none}"
    + "@media print{#draftBar{display:none}}"
    + "@media print{body.exam-locked .opt.wrong::after,body.exam-locked .opt.correct::after{content:none}#fixBar{display:none}}";
  document.head.appendChild(viewStyle);
  document.addEventListener("click", (e)=>{
    const pb = e.target.closest && e.target.closest("#printModeBtn");
    const qb = e.target.closest && e.target.closest("#quizModeBtn");
    if(!pb && !qb) return;
    e.preventDefault(); e.stopImmediatePropagation();
    const P = document.getElementById("printModeBtn"), Q = document.getElementById("quizModeBtn");
    if(qb){   // 回到測驗模式：只換按鈕樣子，不重畫（重畫會清掉作答）
      document.body.classList.remove("answer-view");
      if(Q) Q.classList.add("active"); if(P) P.classList.remove("active");
      return;
    }
    if(!document.body.classList.contains("exam-locked")){
      if(P) P.disabled = true;
      alert("完整題目與解答要先「送出成績」才能查看喔！");
      return;
    }
    showAllAnswers();
    if(P) P.classList.add("active"); if(Q) Q.classList.remove("active");
  }, true);
  function showAllAnswers(){
    document.body.classList.add("answer-view");
    document.querySelectorAll(".opt").forEach(o=>{ o.classList.add("disabled"); if(o.dataset.correct === "true") o.classList.add("correct"); });
    document.querySelectorAll(".explain, .answer-reveal").forEach(el=>el.classList.add("show"));
  }

  // 送出成績後：每個大題標題下面列出小計（答對幾題／共幾題、得幾分／滿分），答對的題目後面標「+N 分」。
  // 每題幾分從大題說明（例如「20分，每題2分」「每格2分」）讀出來；讀不到就只列題數。
  const scoreStyle = document.createElement("style");
  scoreStyle.textContent = ".sec-score{margin:4px 0 10px;padding:8px 12px;border-radius:8px;background:#fff4dc;border:1px solid #e7c98a;color:#6b4a12;font-weight:700;font-size:14.5px}"
    + ".sec-score b{color:#b5561c;font-size:16px}.q-pts{display:inline-block;margin-left:8px;padding:1px 8px;border-radius:999px;background:#e3f2e6;color:#2e7d4f;font-weight:800;font-size:13px;white-space:nowrap}";
  document.head.appendChild(scoreStyle);
  function gradableQ(q){ return q.querySelector(".opts") || q.querySelector("input.blank") || q.querySelector("input.line-answer") || q.querySelector("input.micro-blank"); }
  function fmtPts(x){ return Math.round(x * 100) / 100; }
  function clearSectionScores(){ document.querySelectorAll(".sec-score, .q-pts").forEach(el=>el.remove()); }
  function showSectionScores(){
    clearSectionScores();
    document.querySelectorAll("section.block").forEach(block=>{
      const qs = Array.from(block.querySelectorAll(".q")).filter(q=>gradableQ(q) && q.dataset.studentAnswer !== undefined);
      if(!qs.length) return;
      const meta = block.querySelector(".meta");
      const m = meta && /每[題格]\s*(\d+(?:\.\d+)?)\s*分/.exec(meta.textContent);
      const per = m ? parseFloat(m[1]) : null;
      let ok = 0;
      qs.forEach(q=>{
        if((q.dataset.firstCorrect || q.dataset.isCorrect) !== "true") return;   // 小計、+N 分都以第一次作答為準（訂正對的不加分數）
        ok++;
        if(per != null){
          const tag = document.createElement("span");
          tag.className = "q-pts"; tag.textContent = "+" + fmtPts(per) + " 分";
          (q.querySelector(".q-text") || q).appendChild(tag);
        }
      });
      const box = document.createElement("div");
      box.className = "sec-score";
      box.innerHTML = "📊 本大題：答對 <b>" + ok + "</b> / " + qs.length + " 題" +
        (per != null ? "　得 <b>" + fmtPts(ok * per) + "</b> / " + fmtPts(qs.length * per) + " 分" : "");
      const anchor = meta || block.querySelector("h2");
      if(anchor) anchor.insertAdjacentElement("afterend", box); else block.prepend(box);
    });
  }

  // 選擇題在「送出成績」之前都還在考試中，可以改選答案。
  // 各頁面自己的點選程式在選過之後會把這題鎖住（dataset.answered），這裡用捕捉階段的點擊事件，
  // 在頁面自己的程式執行之前先把該題的作答狀態清掉，讓頁面把新選的答案當成第一次作答；
  // 送出成績之後（按鈕變成鎖住）才真的不能再改。
  const lockStyle = document.createElement("style");
  lockStyle.textContent = "body:not(.exam-locked) .q .opt.disabled{cursor:pointer;}";   // 還沒送出時，選過的題目看起來也是可以再點的
  document.head.appendChild(lockStyle);
  function examLocked(){
    const b = document.getElementById("examSubmitBtn");
    return !!(b && b.disabled);
  }
  document.addEventListener("click", (e)=>{
    const opt = e.target.closest && e.target.closest(".q .opt");
    if(!opt) return;
    const q = opt.closest(".q");
    if(q && q.classList.contains("fix-locked")){ e.preventDefault(); e.stopImmediatePropagation(); return; }   // 訂正時答對的題目鎖住
    if(!q || q.dataset.answered !== "true" || examLocked()) return;
    delete q.dataset.answered;
    delete q.dataset.studentAnswer;
    delete q.dataset.correctAnswer;
    delete q.dataset.isCorrect;
    q.querySelectorAll(".opt").forEach(o=>o.classList.remove("selected", "correct", "wrong", "disabled"));
  }, true);

  // 依提示作答／翻譯題（input.line-answer）：打字時記錄作答內容，
  // 否則送出前的「尚未作答」檢查永遠過不了。用事件委派，「重新作答」重繪後仍有效。
  // 句子題無法完全自動判分：只有和正解（或「 / 」分隔的其中一個完整句）一致才記為答對，
  // 其餘記為答錯，老師可在試算表裡看學生的原始作答再批改。
  function normSentence(s){
    return s.toLowerCase().replace(/[’‘]/g, "'").replace(/[.?!。？！]+$/g, "").replace(/\s+/g, " ").trim();
  }
  document.addEventListener("input", (e)=>{
    const input = e.target;
    if(!input.matches || !input.matches("input.line-answer")) return;
    const q = input.closest(".q");
    if(!q) return;
    const val = input.value.trim();
    if(!val){
      delete q.dataset.studentAnswer;
    } else {
      const reveal = q.querySelector(".answer-reveal");
      const answer = reveal ? reveal.textContent.replace(/^\s*正解：/, "").trim() : "";
      const options = [answer].concat(answer.split(" / "));
      q.dataset.studentAnswer = val;
      q.dataset.correctAnswer = answer;
      q.dataset.isCorrect = options.some(a => normSentence(a) === normSentence(val)) ? "true" : "false";
    }
    if(typeof window.updateScore === "function") window.updateScore();
  });

  window.revealExamAnswers = function(){
    window.examAnswersRevealed = true;
    document.querySelectorAll(".q").forEach(q=>{
      if(q.dataset.studentAnswer === undefined) return;
      const opts = q.querySelectorAll(".opt");
      if(opts.length){
        opts.forEach(o=>{ if(o.dataset.correct==="true") o.classList.add("correct"); });
        const chosen = q.querySelector(".opt.selected");
        if(chosen && chosen.dataset.correct!=="true") chosen.classList.add("wrong");
        const ex = q.querySelector(".explain");
        if(ex) ex.classList.add("show");
      }
      const blank = q.querySelector("input.blank");
      if(blank){
        const fb = blank.parentElement.querySelector(".feedback");
        if(fb){
          const ok = q.dataset.isCorrect === "true";
          fb.textContent = ok ? "✓" : "✗";
          fb.className = "feedback " + (ok ? "ok" : "no");
        }
      }
    });
    // 依提示作答／翻譯題：送出成績後自動顯示正解，按鈕維持隱藏
    document.querySelectorAll(".answer-reveal").forEach(el=>{
      el.classList.add("show");
    });
    document.querySelectorAll(".reveal-btn").forEach(btn=>{
      btn.style.display = "none";
    });
    showSectionScores();
    if(typeof window.updateScore === "function") window.updateScore();
  };

  // ===================== 訂正錯誤（使用者 2026-10-18） =====================
  // 送出成績 → 自動對答案（對綠錯紅、顯示正解）→ 上方「✏️ 訂正錯誤」：答對的題目鎖住，答錯的題目清空、藏起正解，
  // 學生再作答 →「送出訂正」→ 再對答案 → 還有錯就繼續訂正，全部訂正完畢補送 1 點（點數存摺「訂正獎勵」）。
  // 還有錯題沒訂正完不能離開這一頁（點連結會擋，關分頁會跳確認）。每次訂正的題目、作答、對錯都送到試算表，
  // 單元名稱前加「【第 N 次訂正】」、回次加「（第 N 次訂正）」；全部訂正完成另送一列「【全部訂正完成】補送 1 點」。
  let fixRound = 0, pendingFix = false;
  function wrongQs(){ return Array.from(document.querySelectorAll("section.block .q")).filter(q=>gradableQ(q) && q.dataset.studentAnswer !== undefined && q.dataset.isCorrect !== "true"); }
  function fixBar(){
    let bar = document.getElementById("fixBar");
    if(!bar){
      bar = document.createElement("div"); bar.id = "fixBar";
      const ctl = document.querySelector(".controls");
      const first = document.querySelector("section.block");
      if(ctl) ctl.insertAdjacentElement("afterend", bar);
      else if(first) first.insertAdjacentElement("beforebegin", bar);
      else document.body.prepend(bar);
      bar.addEventListener("click", (e)=>{
        if(e.target.closest("button[data-exit]")) skipFix();
        else if(e.target.closest("button[data-fix]")) startFix();
      });
    }
    return bar;
  }
  // 測試帳號 TEST、家長 PARENT：訂正鍵旁多「🚪 立即離開」，按了解除「訂正完才能離開」，可以回單元目錄或主頁面（使用者 2026-10-18）
  function canSkipFix(){ const n = loggedInStudent(); return n === "TEST" || n === "PARENT"; }
  function exitHtml(){ return canSkipFix() ? '<button type="button" data-exit class="exit">🚪 立即離開</button>' : ""; }
  function unitHref(){
    const a = document.querySelector("a.footer-link[href]") || Array.from(document.querySelectorAll("a[href]")).find(x=>/段考題庫/.test(x.textContent) && !/^https?:/.test(x.getAttribute("href")));
    return a ? a.getAttribute("href") : "";
  }
  function skipFix(){
    pendingFix = false;
    const reset = document.getElementById("resetBtn"); if(reset) reset.style.display = "";
    const bar = fixBar(), u = unitHref();
    bar.className = "done";
    bar.innerHTML = '<span class="note">🚪 已解除訂正限制（測試／家長帳號），可以離開：</span>'
      + (u ? '<a class="exit-link" href="' + u + '">↩ 回單元目錄</a>' : '')
      + '<a class="exit-link" href="https://jenlin2002.github.io/">🏠 回主頁面</a>';
  }
  function lockCorrect(q){
    q.classList.remove("fixing"); q.classList.add("fix-locked");
    q.querySelectorAll("input").forEach(i=>{ i.readOnly = true; });
  }
  function startFix(){
    const wrong = wrongQs();
    if(!wrong.length) return;
    fixRound++;
    document.querySelectorAll("section.block .q").forEach(q=>{ if(gradableQ(q) && q.dataset.isCorrect === "true") lockCorrect(q); });
    wrong.forEach(q=>{
      q.classList.add("fixing");
      delete q.dataset.answered; delete q.dataset.studentAnswer; delete q.dataset.correctAnswer; delete q.dataset.isCorrect;
      q.querySelectorAll(".opt").forEach(o=>o.classList.remove("selected", "correct", "wrong", "disabled"));
      q.querySelectorAll("input").forEach(i=>{ i.value = ""; i.readOnly = false; });
      q.querySelectorAll(".feedback").forEach(f=>{ f.textContent = ""; f.className = "feedback"; });
      q.querySelectorAll(".answer-reveal, .explain").forEach(el=>el.classList.remove("show"));
    });
    document.body.classList.remove("exam-locked");
    window.examAnswersRevealed = false;
    const btn = document.getElementById("examSubmitBtn");
    btn.disabled = false; btn.style.opacity = ""; btn.style.cursor = ""; btn.textContent = "送出訂正";
    const st = document.getElementById("examSyncStatus"); if(st) st.textContent = "";
    const bar = fixBar(); bar.className = "";
    bar.innerHTML = '<button type="button" data-fix disabled>✏️ 第 ' + fixRound + ' 次訂正中</button><span class="note">把 <b>' + wrong.length + ' 題</b>黃色框的題目重新作答，完成後按右下角「送出訂正」。錯題全部訂正完畢再另加補送 <b>1 點</b>。</span>' + exitHtml();
    wrong[0].scrollIntoView({ behavior: "smooth", block: "center" });
    if(typeof window.updateScore === "function") window.updateScore();
  }
  function afterGrade(student, label){
    const wrong = wrongQs();
    document.querySelectorAll("section.block .q").forEach(q=>{ if(gradableQ(q) && q.dataset.isCorrect === "true" && (fixRound > 0 || q.classList.contains("fixing"))) lockCorrect(q); });
    const bar = fixBar();
    const reset = document.getElementById("resetBtn");
    if(wrong.length){
      pendingFix = true;
      if(reset) reset.style.display = "none";   // 訂正完才能重新作答
      bar.className = "";
      bar.innerHTML = '<button type="button" data-fix>✏️ 訂正錯誤</button><span class="note">還有 <b>' + wrong.length + ' 題</b>錯誤（紅色）。按「訂正錯誤」重新作答，<b>錯誤全部訂正完畢再另加補送 1 點</b>；訂正完才能離開這一頁。</span>' + exitHtml();
      return;
    }
    pendingFix = false;
    if(reset) reset.style.display = "";
    if(fixRound === 0){ bar.remove(); return; }   // 第一次就全對，不用訂正
    bar.className = "done";
    bar.innerHTML = '<span class="note">🎉 錯題全部訂正完成（訂正 ' + fixRound + ' 次）！補送 <b>1 點</b>。可以回到單元目錄了。</span>';
    if(student !== "PARENT") sendToSheet({
      date: nowStr(), student, version: window.EXAM_META.version,
      examLabel: window.EXAM_META.examLabel + "（訂正完成）",
      sectionTitle: "【全部訂正完成】補送 1 點",
      items: [{ num: 0, question: "錯題全部訂正完成（共訂正 " + fixRound + " 次）", studentAnswer: "", correctAnswer: "", isCorrect: true }],
      summary: { score: 1, total: 1 }
    });
    if(window.Points) Points.earn({ name: student, label: label, mode: "訂正完成", kind: "fix-bonus", correct: 1, total: 1 });
  }
  // 還有錯題沒訂正完：擋住離開這一頁的連結；關分頁／重新整理跳出確認
  document.addEventListener("click", (e)=>{
    if(!pendingFix) return;
    const a = e.target.closest && e.target.closest("a[href]");
    if(!a || a.getAttribute("href").charAt(0) === "#") return;
    e.preventDefault(); e.stopImmediatePropagation();
    alert("還有 " + wrongQs().length + " 題錯誤，先按上方「訂正錯誤」訂正完才能離開喔！");
  }, true);
  window.addEventListener("beforeunload", (e)=>{ if(pendingFix){ e.preventDefault(); e.returnValue = ""; } });

  window.submitExamResults = async function(){
    const student = loggedInStudent();
    const statusEl = document.getElementById("examSyncStatus");
    if(!student){ alert("請先登入（在「你是誰？」選名字並輸入 PIN），成績才會記在你的名下"); return; }
    if(!window.EXAM_META){ alert("這個頁面尚未設定考卷資訊"); return; }

    // 檢查所有可判斷對錯的題目是否都已作答
    const unanswered = [];
    document.querySelectorAll("section.block .q").forEach(q=>{
      const gradable = q.querySelector(".opts") || q.querySelector("input.blank") || q.querySelector("input.line-answer") || q.querySelector("input.micro-blank");
      if(gradable && q.dataset.studentAnswer === undefined){
        unanswered.push(q);
      }
    });
    if(unanswered.length > 0){
      alert(`還有 ${unanswered.length} 題尚未作答，請先完成所有測驗題目再送出成績。`);
      unanswered[0].scrollIntoView({behavior:"smooth", block:"center"});
      return;
    }

    const submitBtn = document.getElementById("examSubmitBtn");
    submitBtn.disabled = true;
    submitBtn.style.opacity = "0.6";
    submitBtn.style.cursor = "not-allowed";
    document.body.classList.add("exam-locked");

    const date = nowStr();
    let sections = 0;

    statusEl.textContent = "送出中...";

    // 逐一依序送出（不要同時平行送出多個單元），
    // 避免多個請求同時打到 Apps Script 造成寫入衝突、漏掉部分列。
    const blocks = Array.from(document.querySelectorAll("section.block"));
    let allScore = 0, allTotal = 0;
    const fixing = fixRound > 0;
    for(const block of blocks){
      const h2 = block.querySelector("h2");
      const sectionTitle = (fixing ? "【第 " + fixRound + " 次訂正】" : "") + (h2 ? h2.textContent.trim() : "");
      const items = [];
      let score = 0, total = 0;
      block.querySelectorAll(".q").forEach((q, idx)=>{
        if(fixing && !q.classList.contains("fixing")) return;   // 訂正時只送這次訂正的題目
        if(!fixing && q.dataset.studentAnswer !== undefined) q.dataset.firstCorrect = q.dataset.isCorrect;
        if(q.dataset.studentAnswer !== undefined){
          total++;
          const correct = q.dataset.isCorrect === "true";
          if(correct) score++;
          const qtext = q.querySelector(".q-text");
          items.push({
            num: idx+1,
            question: qtext ? qtext.textContent.trim() : "",
            studentAnswer: q.dataset.studentAnswer,
            correctAnswer: q.dataset.correctAnswer,
            isCorrect: correct
          });
        }
      });
      if(items.length){
        sections++;
        allScore += score; allTotal += total;
        statusEl.textContent = `送出中...（第 ${sections} 個單元）`;
        // 家長（PARENT）測試時不寫進成績單，只在點數的測試存摺記一筆
        if(student !== "PARENT") await sendToSheet({
          date, student,
          version: window.EXAM_META.version,
          examLabel: window.EXAM_META.examLabel + (fixing ? "（第 " + fixRound + " 次訂正）" : ""),
          sectionTitle,
          items,
          summary: { score, total }
        });
        // 每個單元之間留一點間隔，讓 Apps Script 那邊有時間把上一筆寫完，
        // 進一步降低並發衝突的機率。
        await new Promise(r=>setTimeout(r, 400));
      }
    }

    if(sections === 0){
      statusEl.textContent = "尚未作答任何題目";
      // 沒有真的送出任何資料，把按鈕解鎖讓學生可以再試一次
      submitBtn.disabled = false;
      submitBtn.style.opacity = "";
      submitBtn.style.cursor = "";
      document.body.classList.remove("exam-locked");
    } else {
      statusEl.textContent = fixing ? `已送出第 ${fixRound} 次訂正！` : `已送出 ${sections} 個單元的成績！`;
      submitBtn.textContent = fixing ? "已送出訂正" : "已送出成績";
      if(typeof window.refreshStudentOwnerBadge === "function"){
        window.refreshStudentOwnerBadge(student);
      }
      // 計入學習點數（每題 1 點、同一份考卷每天第一次才算，規則在點數後端）
      const ptsLabel = document.title + "（" + window.EXAM_META.version + "）";
      if(window.Points && !fixing){   // 點數只算第一次作答；訂正全部完成另外補送 1 點（afterGrade）
        Points.earn({ name: student, label: ptsLabel, mode: "全卷", correct: allScore, total: allTotal });
      }
      // 成功送出後按鈕維持鎖住，避免手滑重複點擊造成同一份成績送出兩次
      if(typeof window.unlockPrintMode === "function"){
        window.unlockPrintMode();
      }
      window.revealExamAnswers();
      showAllAnswers();   // 不用再按「完整題目與解答」：所有正解、詳解直接顯示
      document.querySelectorAll(".q.fixing").forEach(q=>q.classList.remove("fixing"));
      if(!fixing) clearDraft();   // 送出成績了，暫存的作答不用再接續
      afterGrade(student, ptsLabel);
      document.querySelectorAll(".script-toggle button").forEach(b=>{
        b.disabled = false;
        b.textContent = "顯示逐字稿";
        b.title = "";
      });
    }
  };

  // ===================== 暫存（使用者 2026-10-18） =====================
  // 做到一半有事：按上方「💾 暫存」（作答時也會自動暫存），下次用同一個帳號打開這一頁會自動接續作答。
  // 存在這台裝置的 localStorage（examDraft:頁面路徑:登入者），送出成績或按「重新作答」後清掉。
  // 每題記：選的選項文字、各空格／文字框的內容；接續時用頁面自己的點選與 input 事件還原，對錯照常判。
  function draftKey(){ return "examDraft:" + location.pathname + ":" + (loggedInStudent() || "-"); }
  function allQs(){ return Array.from(document.querySelectorAll("section.block .q")); }
  function optText(o){ return (o.textContent || "").replace(/\s+/g, " ").trim(); }
  function collectDraft(){
    const qs = allQs(), data = {}; let n = 0;
    qs.forEach((q, i)=>{
      const d = {};
      const sel = q.querySelector(".opt.selected");
      if(sel) d.o = optText(sel);
      const vals = Array.from(q.querySelectorAll("input[type=text], input:not([type]), textarea")).map(el=>el.value);
      if(vals.some(v=>v.trim())) d.v = vals;
      if(d.o || d.v){ data[i] = d; n++; }
    });
    return { n, total: qs.length, data };
  }
  function draftNote(t){ const el = document.getElementById("draftNote"); if(el) el.textContent = t; }
  function hhmm(t){ const d = new Date(t); return (d.getMonth()+1) + "/" + d.getDate() + " " + String(d.getHours()).padStart(2,"0") + ":" + String(d.getMinutes()).padStart(2,"0"); }
  function saveDraft(manual){
    if(examLocked() || fixRound > 0) return;
    const c = collectDraft();
    try{
      if(!c.n){ localStorage.removeItem(draftKey()); if(manual) draftNote("還沒有作答，不用暫存"); return; }
      const t = Date.now();
      localStorage.setItem(draftKey(), JSON.stringify({ t, n: c.n, total: c.total, data: c.data }));
      draftNote((manual ? "✅ 已暫存" : "已自動暫存") + "（" + hhmm(t) + "，已作答 " + c.n + " / " + c.total + " 題）。下次打開這一頁會自動接續。");
    }catch(e){ if(manual) draftNote("這台裝置無法暫存（瀏覽器不允許）"); }
  }
  function clearDraft(){ try{ localStorage.removeItem(draftKey()); }catch(e){} draftNote("作答時會自動暫存，做到一半可以先離開，下次打開這一頁接續作答。"); }
  function restoreDraft(d){
    const qs = allQs(); let n = 0;
    Object.keys(d.data || {}).forEach(k=>{
      const q = qs[+k], it = d.data[k];
      if(!q) return;
      if(it.o){
        const o = Array.from(q.querySelectorAll(".opt")).find(x=>optText(x) === it.o);
        if(o && !o.classList.contains("selected")) o.click();
      }
      if(it.v){
        Array.from(q.querySelectorAll("input[type=text], input:not([type]), textarea")).forEach((el, j)=>{
          if(it.v[j] === undefined || el.value === it.v[j]) return;
          el.value = it.v[j];
          el.dispatchEvent(new Event("input", { bubbles: true }));
          el.dispatchEvent(new Event("change", { bubbles: true }));
        });
      }
      n++;
    });
    return n;
  }
  let draftTimer = 0;
  function autoSave(){ clearTimeout(draftTimer); draftTimer = setTimeout(()=>saveDraft(false), 600); }
  function initDraft(){
    if(document.getElementById("draftBar") || !document.querySelector("section.block .q")) return;
    const bar = document.createElement("div"); bar.id = "draftBar";
    bar.innerHTML = '<button type="button" id="draftSave">💾 暫存</button><span id="draftNote"></span><button type="button" class="ghost" id="draftClear" hidden>清除暫存、重新開始</button>';
    const ctl = document.querySelector(".controls"), first = document.querySelector("section.block");
    if(ctl) ctl.insertAdjacentElement("afterend", bar); else first.insertAdjacentElement("beforebegin", bar);
    document.getElementById("draftSave").addEventListener("click", ()=>saveDraft(true));
    document.getElementById("draftClear").addEventListener("click", ()=>{
      if(!confirm("確定清除暫存、從頭作答？")) return;
      clearDraft(); document.getElementById("draftClear").hidden = true;
      const r = document.getElementById("resetBtn"); if(r) r.click(); else location.reload();
    });
    let d = null;
    try{ d = JSON.parse(localStorage.getItem(draftKey()) || "null"); }catch(e){}
    if(d && d.data){
      const n = restoreDraft(d);
      draftNote("📌 已接續 " + hhmm(d.t) + " 暫存的作答（" + n + " 題），繼續做完再送出成績。");
      document.getElementById("draftClear").hidden = false;
    } else {
      draftNote("作答時會自動暫存，做到一半可以先離開，下次打開這一頁接續作答。");
    }
    // 作答時自動暫存（點選項、打字）
    document.addEventListener("click", (e)=>{ if(e.target.closest && e.target.closest(".opt")) autoSave(); });
    document.addEventListener("input", (e)=>{ if(e.target.matches && e.target.matches("section.block input, section.block textarea")) autoSave(); });
    window.addEventListener("pagehide", ()=>{ if(!examLocked() && fixRound === 0 && collectDraft().n) saveDraft(false); });
  }

  document.addEventListener("DOMContentLoaded", injectPicker);
  // 頁面自己的程式畫好題目後再接續暫存（等登入關卡寫好 quizStudentName）
  window.addEventListener("load", ()=>setTimeout(initDraft, 300));
})();
