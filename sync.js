/* 段考題庫 - 共用的 Google Sheet 回傳邏輯 (exam-bank/sync.js) */
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

  function injectPicker(){
    if(document.getElementById("examSyncBar")) return;
    const bar = document.createElement("div");
    bar.id = "examSyncBar";
    bar.style.cssText = "position:fixed;bottom:16px;right:16px;z-index:999;background:#2f4538;color:#eef2ea;"
      + "padding:10px 14px;border-radius:10px;box-shadow:0 4px 14px rgba(0,0,0,.25);"
      + "font-family:'Noto Sans TC',sans-serif;font-size:13.5px;display:flex;gap:8px;align-items:center;";
    bar.innerHTML = `
      <select id="examStudentSelect" style="border-radius:6px;border:none;padding:6px 8px;font-size:13.5px;">
        <option value="">選擇學生</option>
        <option value="BRANDEN">BRANDEN</option>
        <option value="MELISSA">MELISSA</option>
      </select>
      <button id="examSubmitBtn" style="background:#b5842a;color:#fff;border:none;border-radius:6px;
        padding:7px 14px;font-size:13.5px;cursor:pointer;">送出成績</button>
      <span id="examSyncStatus" style="font-size:12px;color:#cfe0d1;"></span>
    `;
    document.body.appendChild(bar);

    const saved = localStorage.getItem("examBankStudent");
    if(saved) document.getElementById("examStudentSelect").value = saved;
    document.getElementById("examStudentSelect").addEventListener("change", (e)=>{
      localStorage.setItem("examBankStudent", e.target.value);
    });

    document.getElementById("examSubmitBtn").addEventListener("click", ()=>{
      window.submitExamResults();
    });
  }

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
    if(typeof window.updateScore === "function") window.updateScore();
  };

  window.submitExamResults = function(){
    const student = document.getElementById("examStudentSelect").value;
    const statusEl = document.getElementById("examSyncStatus");
    if(!student){ alert("請先在右下角選擇學生身分"); return; }
    if(!window.EXAM_META){ alert("這個頁面尚未設定考卷資訊"); return; }

    // 檢查所有可判斷對錯的題目是否都已作答
    const unanswered = [];
    document.querySelectorAll("section.block .q").forEach(q=>{
      const gradable = q.querySelector(".opts") || q.querySelector("input.blank") || q.querySelector("input.line-answer");
      if(gradable && q.dataset.studentAnswer === undefined){
        unanswered.push(q);
      }
    });
    if(unanswered.length > 0){
      alert(`還有 ${unanswered.length} 題尚未作答，請先完成所有測驗題目再送出成績。`);
      unanswered[0].scrollIntoView({behavior:"smooth", block:"center"});
      return;
    }

    const date = nowStr();
    let sections = 0;

    document.querySelectorAll("section.block").forEach(block=>{
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
        sendToSheet({
          date, student,
          version: window.EXAM_META.version,
          examLabel: window.EXAM_META.examLabel,
          sectionTitle,
          items,
          summary: { score, total }
        });
      }
    });

    if(sections === 0){
      statusEl.textContent = "尚未作答任何題目";
    } else {
      statusEl.textContent = `已送出 ${sections} 個單元的成績！`;
      if(typeof window.unlockPrintMode === "function"){
        window.unlockPrintMode();
      }
      window.revealExamAnswers();
      document.querySelectorAll(".script-toggle button").forEach(b=>{
        b.disabled = false;
        b.textContent = "顯示逐字稿";
        b.title = "";
      });
    }
  };

  document.addEventListener("DOMContentLoaded", injectPicker);
})();
