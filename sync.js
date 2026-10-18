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
    + "body.exam-locked .opt.wrong{border-color:#c0392b !important;background:#fdecea !important;color:#c0392b}"
    + "body.exam-locked .opt.wrong::after{content:'  ✗ 你的答案';color:#c0392b;font-weight:800;margin-left:auto;padding-left:10px}"
    + "body.exam-locked .opt.correct::after{content:'  ✓ 正解';color:#2e7d4f;font-weight:800;margin-left:auto;padding-left:10px}"
    + "@media print{body.exam-locked .opt.wrong::after,body.exam-locked .opt.correct::after{content:none}}";
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
        if(q.dataset.isCorrect !== "true") return;
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
    for(const block of blocks){
      const h2 = block.querySelector("h2");
      const sectionTitle = h2 ? h2.textContent.trim() : "";
      const items = [];
      let score = 0, total = 0;
      block.querySelectorAll(".q").forEach((q, idx)=>{
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
          examLabel: window.EXAM_META.examLabel,
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
      statusEl.textContent = `已送出 ${sections} 個單元的成績！`;
      submitBtn.textContent = "已送出成績";
      if(typeof window.refreshStudentOwnerBadge === "function"){
        window.refreshStudentOwnerBadge(student);
      }
      // 計入學習點數（每題 1 點、同一份考卷每天第一次才算，規則在點數後端）
      if(window.Points){
        Points.earn({ name: student, label: document.title + "（" + window.EXAM_META.version + "）", mode: "全卷", correct: allScore, total: allTotal });
      }
      // 成功送出後按鈕維持鎖住，避免手滑重複點擊造成同一份成績送出兩次
      if(typeof window.unlockPrintMode === "function"){
        window.unlockPrintMode();
      }
      window.revealExamAnswers();
      showAllAnswers();   // 不用再按「完整題目與解答」：所有正解、詳解直接顯示
      document.querySelectorAll(".script-toggle button").forEach(b=>{
        b.disabled = false;
        b.textContent = "顯示逐字稿";
        b.title = "";
      });
    }
  };

  document.addEventListener("DOMContentLoaded", injectPicker);
})();
