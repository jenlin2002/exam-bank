/* 段考題庫 - 共用的 Google Sheet 回傳邏輯 (exam-bank/sync.js) */
(function () {
  const SHEET_ENDPOINT = "https://script.google.com/macros/s/AKfycbxAHs05hVkOrjz36ZBZ5gDugcTOJSCDNOBAmDMwXiEpyoGxV-1Wm5sT3G8SK04e2w5m/exec";

  function pad(n) { return n.toString().padStart(2, "0"); }
  function nowStr() {
    const d = new Date();
    return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}`;
  }

  // 送出「答題明細」：items 是一個陣列，每個元素是一題的作答結果
  window.sendExamDetail = function (student, version, examLabel, sectionTitle, items) {
    const payload = {
      date: nowStr(),
      student,
      version,
      examLabel,
      sectionTitle,
      items
    };
    fetch(SHEET_ENDPOINT, {
      method: "POST",
      mode: "no-cors",
      headers: { "Content-Type": "text/plain;charset=utf-8" },
      body: JSON.stringify(payload)
    }).catch(function (err) {
      console.error("送出成績失敗：", err);
    });
  };

  // 送出「測驗紀錄」總結
  window.sendExamSummary = function (student, version, examLabel, sectionTitle, score, total) {
    const payload = {
      date: nowStr(),
      student,
      version,
      examLabel,
      sectionTitle,
      summary: { score, total }
    };
    fetch(SHEET_ENDPOINT, {
      method: "POST",
      mode: "no-cors",
      headers: { "Content-Type": "text/plain;charset=utf-8" },
      body: JSON.stringify(payload)
    }).catch(function (err) {
      console.error("送出總結失敗：", err);
    });
  };
})();
