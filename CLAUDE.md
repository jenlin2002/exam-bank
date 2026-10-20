# exam-bank（國中段考題庫）

靜態網站（GitHub Pages），學生做線上練習卷，成績透過 `sync.js` 送到 Google 試算表。
本機預覽：`python -m http.server 8532`（設定在 `.claude/launch.json`）。

## 使用者與工作方式（學習網站各 repo 共用同一段，2026-10-13）

- 使用者在三個地方用 Claude Code：**家裡電腦、公司電腦**（兩台都有 GitHub Desktop，用它 Pull／Push）、**外出用手機 App（雲端版）**。學習成長網站已經做很久了，不用從頭介紹。
- **不用教 git／GitHub Desktop／PowerShell 的操作。** 改完直接開 PR 合併到 `main`（使用者另一台電腦用 GitHub Desktop Pull 就好），只要回報「改了什麼、合併到哪裡」。
- 一律用**繁體中文**回覆。
- **每次結束前**：把這次做的事、待辦更新到這個 CLAUDE.md，合併到 `main`，下一個地方 Pull 後就接得上。
- 學習網站的 repo（都在 jenlin2002 底下，GitHub Pages 從 `main` 發布）：
  `jenlin2002.github.io`（網站首頁＝成長學習館總入口、點數存摺、B&M 學習 App）、`english-quiz`（英文測驗系統）、
  `daily_life_listening`（美式生活館）、`vocab-king`（圖解單字）、`nat-geo-reading`（國家地理風閱讀）、`exam-bank`（段考題庫）。
  雲端版只讀得到這次有載入的 repo；要改的 repo 沒載入時，直接用 add_repo 加進來。
- 股票（`stock`、`stock-dashboard`）和學習網站分開，學習網站裡不要放股票相關的東西。

## 結構與規格
- `english.html`：英語科總目錄（年級 × 康軒／翰林／南一卡片，`href:null` 代表「即將推出」）。
- `<版本>-g<年級>-<冊>.html`：該冊目錄頁，例如 `kangxuan-g8-1.html`、`hanlin-g8-1.html`。`EXAMS` 陣列每回有 A／B／C 卷三個連結。
- `<版本>-g8-1/testN.html` = A 卷，`testNb.html` = B 卷，`testNc.html` = C 卷。
  - 一般回：資料寫在 `DATA.sections`。題型有 vocab、mc、cloze、reading、guided、translation、guided-multi。`window.EXAM_META = {version:"A卷", examLabel:"第N回"}`。
  - 聽力回（第 4、8、12 回）：每個部分一個 `<audio>`，音檔放在 `audio/testN[b|c]/trackK.mp3`。
  - 圖片放在 `images/testN[b|c]/`。
- `sync.js`：共用的送出成績邏輯（選學生 → 檢查是否全部作答 → 逐單元送出 → 解鎖完整題目與解答）。
- `PDF-RAW-DATA/<科目>/<版本>/<版本>-g8-1/`：原始 PDF 和聽力 zip，**網頁不會讀取**。
- 原始檔來源（公司電腦 OneDrive）：`OneDrive - avc.co\興雅國中\XXY\校用券1到3 年級全出版社\115年\115上國中2年級校卷\115上<版本>2上校卷\`

## 工作紀錄

### 2026-10-01（公司電腦）
1. **翰林二上英語 A／B／C 卷全部完成**
   - 新增 `hanlin-g8-1.html` 和 `hanlin-g8-1/test1~13(.html / b.html / c.html)`，共 39 頁。
   - `english.html` 的「國中二上・翰林」改為已上線。
   - 翰林比康軒多一回：第 13 回是 Review Test 4（全冊總複習）。
   - 聽力音檔對應：第 4 回 = TRACK 1～3，第 8 回 = TRACK 4～6，第 12 回 = TRACK 7～9（每卷 zip 裡各 9 軌）。
   - 聽力第三部分題數各卷不同：A 卷 8 題、B 卷 10 題、C 卷 5 題。
   - 答案都對照過各卷簡答 PDF。39 頁的圖片和音檔都在本機驗證過可以載入。
2. **修正 `sync.js` 的 bug**
   - 原本：有「依提示作答」或「翻譯」（`input.line-answer`）的頁面，學生打字不會被記成已作答，送出時永遠跳出「還有 N 題尚未作答」，成績送不出去。康軒和翰林都受影響。
   - 修正：用 document 層級的 input 事件委派，記錄 `studentAnswer`。
   - 對錯判定：和正解一致才算對（不分大小寫、忽略句尾標點和多餘空格；正解用「 / 」分隔的任一完整句也算對），其餘算錯。老師可以在試算表看學生原句再批改。
3. **整理 `PDF-RAW-DATA`**
   - `english/hanlin/hanlin-g8-1` 和 `MATH/hanlin/hanlin-g8-1` 原本誤放了康軒檔案，現在已換成真正的翰林檔案。
   - 康軒檔案移到 `.../kangxuan/kangxuan-g8-1/`。重複的檔案比對過內容才刪除，沒有遺失。
   - 新建了 `MATH/kangxuan/kangxuan-g8-1/`。
4. **產生工具** 放在 `tools/hanlin-g8-1-build/`
   - `data*/tNN.py`：每回的題目資料（A／B／C）。
   - `gen.py` + `gen_pages.py`：以康軒頁面為範本產生所有翰林頁面和目錄頁。
   - `crop*.py`：從 PDF 裁切附圖，需要 `pip install pymupdf`。
   - 腳本裡寫死了路徑：`E:\GitHub\exam-bank`、公司電腦的 OneDrive 路徑。在家裡電腦使用前要先改成家裡的路徑。
   - 改錯字的流程：修改 `data*/tNN.py` → `python gen_pages.py`。

### 2026-10-02（公司電腦）
- 翰林二上**數學** A 卷第 1～2 回樣本：`hanlin-math-g8-1.html`、`hanlin-math-g8-1/test1~2.html`、`math.html`。**首頁 `index.html` 的數學入口尚未開放**，要等老師確認版面。
- 數學版面：
  - 用 KaTeX（cdnjs）排版，算式寫成 `$...$`。
  - 選擇題可以加 `pre`（共用題組文字）。
  - 填充題（`fill`）：自動批改，會把空格、`^`、²、全形符號、π/pi、單位統一後再比對，`answers` 可以列多種寫法。
  - 計算題（`calc`）：每個小題一格最後答案、自動批改，過程寫在紙上（老師選 A 方案，不在網頁上打計算過程）。
  - 試算表上的版別標成「數學A卷」。
- 產生方式：`tools/hanlin-g8-1-build/` 裡的 `mathdata/tNN.py` → `python gen_math.py`；附圖用 `crop_math.py` 裁切。
- 下午：數學 **A 卷第 1～15 回全部完成**，首頁 `index.html` 的「數學」入口已開放。
  - 每回的附圖裁切座標寫在 `mathdata/tNN.py` 的 `CROPS`，`crop_math.py` 會依此裁切（A／B／C 卷通用）。
  - 自動批改另外支援：根號（√/sqrt/根號）、±（+-）、「或」分隔的多解（不計順序）、因式分解的因式順序、全形符號、% 與單位。
  - 15 頁都驗證過：每題的官方答案都判為正確、KaTeX 沒有錯誤、圖片都有載入。
  - 待辦：數學 B、C 卷（原始檔在 `PDF-RAW-DATA/MATH/hanlin/hanlin-g8-1/`，資料放 `mathdataB/`、`mathdataC/`）。
- 晚上：**翰林二上社會 A 卷完成**（地理、歷史、公民各 9 回，共 27 回）。
  - 頁面：`hanlin-social-g8-1.html` 和 `hanlin-social-g8-1/{geo,hist,civ}1~9.html`。`social.html` 的「國中二上・翰林」已開放。
  - 版型沿用家裡做的翰林七上社會（`hanlin-social-g7-1/geo1.html`）。每回的題型是：單題 20 題、題組 4 題、進階思考題 7 題。
  - 產生方式：`tools/hanlin-g8-1-build/socdata/*.py` → `python gen_soc.py`（會一併裁切附圖；原始 PDF 路徑寫死為公司電腦的 OneDrive）。B、C 卷的資料放 `socdataB/`、`socdataC/`。
  - 27 頁都驗證過：答案標記數＝題數，圖片都有載入，可以正常送出。
  - 待辦：社會 B、C 卷；數學 B、C 卷。
- **翰林一上數學 A 卷完成**（第 1～14 回）：`hanlin-math-g7-1.html`、`hanlin-math-g7-1/test1~14.html`，`math.html` 的「國中一上・翰林」已開放。
  - 產生方式：`math7data/tNN.py` → `python crop_math.py --g7`、`python gen_math.py --g7`（不加 `--g7` 就是產生二上）。原始 PDF 讀自 OneDrive 的 `115上國中1年級校卷\115上翰林1上校卷\115上翰林數學1上校卷`。
  - 自動批改另外支援：上標數字（²、⁵）、× 打成 x、常見單位（毫升、公克、題、秒、°C 等）。
  - 14 頁都驗證過：官方答案都判為正確、KaTeX 沒有錯誤、圖片都有載入。
- **翰林一上英語 A 卷完成**（第 1～14 回，聽力是第 5、9、13 回）：`hanlin-g7-1.html`、`hanlin-g7-1/test1~14.html`，`english.html` 的「國中一上・翰林」已開放。
  - 聽力音檔對應：第 5 回 = TRACK 1～3，第 9 回 = TRACK 4～6，第 13 回 = TRACK 7～9（各卷 zip 都是 9 軌）。
  - 產生方式：`eng7data/tNN.py` → `python gen_eng7.py`（會一併裁圖、解壓音檔，原始檔讀自 OneDrive 的 `115上國中1年級校卷\115上翰林1上校卷\115上翰林英文1上校卷`）。
  - 新增：填空題可設定 `exact=True` 區分大小寫（用於大小寫轉換題）；看圖填空題可附圖。
- 社會七上（翰林）是在家裡電腦做的，做到地理第 5 回 A 卷。截至 10/02 上午**尚未 Push 到 GitHub**。

### 2026-10-04（家裡電腦）
- **選擇題在「送出成績」之前可以改選答案**（使用者要求：沒送出前都還在考試中，不要鎖死）。
  各頁面自己的 `selectOption` 在選過之後會設 `dataset.answered="true"` 鎖住該題；修在共用的 `sync.js`（所有英語／數學／社會頁都載入它）：
  捕捉階段的 click 事件，在頁面程式執行前先清掉該題的作答狀態（answered／studentAnswer／correctAnswer／isCorrect、selected／disabled 樣式），
  讓頁面把新選的答案當成第一次作答；送出成績後（`#examSubmitBtn` 被鎖住，body 加上 `exam-locked`）才真的不能改。按「重新作答」會解鎖。
  填空、翻譯、計算題本來就是 input 事件，可以隨時修改。以後新做的頁面只要照舊慣例（`.q`、`.opt`、`dataset.answered`）並載入 `sync.js` 就自動有這個行為。
  已測：社會（hanlin-social-g8-1/geo1）、英語一般回與聽力回（hanlin-g8-1/test4）、數學（hanlin-math-g8-1/test1）；改選後作答數、對錯、已選樣式都正確，鎖住後點選無效。
- **段考題庫接上學習點數存摺（使用者要求：只要是測驗都記錄、都納入點數）**：根目錄新增 `points.js`（和英文測驗系統共用的同一份，第 6 份副本，主檔在 english-quiz-plan/points/points.js；改主檔要同步各處）。
  `sync.js` 一載入就用 `document.currentScript.src` 找同資料夾的 `points.js` 動態載入（所以 281 頁不用逐頁加 script）；
  `submitExamResults()` 成功送出後呼叫 `Points.earn({ name: 選的學生, label: 頁面標題（A卷）, mode: "全卷", correct, total })`。
  **不用再選學生了（使用者 2026-10-04）**：右下角的下拉選單拿掉，改顯示「登入者：XXX」；「送出成績」自動帶登入者（localStorage 的 `quizStudentName`，由 points.js 的 PIN 關卡寫入）回傳試算表與點數；沒登入會提示先登入；家長（PARENT）測試只記點數的測試存摺、不寫進成績單。規則同其他網站：每題 1 點、同一份考卷每天第一次才算、每天上限 50 點。
  沒登入的人會先看到「你是誰？」關卡。已用社會地理第 1 回測過（stub 掉真正的送出）：回報的名字、標題、答對／總題數都正確。

### 2026-10-08（手機雲端版）
- **翰林二上國文 A 卷第 1～16 回完成**，取代原本 Gemini 做的版本（舊版只有「第1套・A卷／B卷／C卷」三張卡片，題目也不是出自原卷，`hanlin-chinese-g8-1-a.html` 已刪除）。
  - 目錄頁 `hanlin-chinese-g8-1.html` 改成和社會科（地理）一樣：「第N回・第N課／課名」＋ A卷／B卷／C卷 按鈕（B、C 卷還沒做，按鈕是灰的）。
  - 測驗頁 `hanlin-chinese-g8-1/test1~16.html`，版型沿用社會科測驗頁（`tools/hanlin-g8-1-build/tpl_chinese.html`）。
  - 每回的範圍：第 1～3 回＝第一～三課，第 4 回＝第一～三課複習，第 5～7 回＝第四～六課，第 8 回＝複習，第 9～12 回＝第七～十課，第 13 回＝複習，第 14～16 回＝自學選文一～三。第 N 回＝PDF 第 2N-1、2N 頁。
  - 題型：注音國字、改錯（`fill`，自動批改：去掉空白標點後比對，注音一聲可不標；改錯是依序寫出改正後的字）；解釋（`explain`，寫在格子裡，送出後顯示參考答案，**不計分**）；成語填空（做成選擇題，選項是參考選項）；基礎題／進階題（`mc`）；閱讀測驗／題組（`reading`）。
  - 原卷是掃描檔（PDF 沒有文字），題目是看圖逐題打字的；答案全部照 `PDF-RAW-DATA/Chinese/hanlin/hanlin-G8-1/` 的 A 卷簡答。
  - 少數地方簡答和題目用字不同（例如第 11 回改錯「勘／堪」、第 12 回「憤／忿」、第 7 回羽「翮」ㄍㄜˊ／ㄏㄜˊ），兩種寫法都算對。
  - 16 頁都驗證過：每題的官方答案都判為正確、沒有 JS 錯誤、圖片都有載入、可以送出。
  - 產生方式：改 `tools/hanlin-g8-1-build/chidata/tNN.py` → `python gen_chinese.py`（路徑是相對路徑，任何電腦都能跑；有附圖的回才需要 pymupdf）。B、C 卷的資料放 `chidataB/`、`chidataC/`，檔名一樣，產生 `testNb.html`、`testNc.html`。

- **翰林一上國文 A 卷第 1～16 回完成**（同一天）：`hanlin-chinese-g7-1.html` 和 `hanlin-chinese-g7-1/test1~16.html`，格式和二上國文一樣；`chinese.html` 的「國中一上・翰林」已開放。
  - 範圍：第 1～3 回＝第一～三課（夏夜、無心的錯誤、母親的教誨），第 4 回複習，第 5～7 回＝第四～六課（論語選、背影、心囚），第 8 回複習，第 9～12 回＝第七～十課（兒時記趣、朋友相交、音樂家與職籃巨星、玫瑰淚），第 13 回複習，第 14～16 回＝自學選文一～三。
  - 產生方式：`chi7data/tNN.py` → `python gen_chinese.py --g7`（不加 `--g7` 是二上）。
  - **簡答有一題錯**：第 16 回單題第 16 題簡答寫 D（「好逸惡勞」明顯誤用），網頁改用 B（焦頭爛額），檔案裡有註解。
  - 16 頁都驗證過：每題正解都判為正確、沒有 JS 錯誤、可以送出。

### 2026-10-09（家裡電腦）
- **翰林一上、二上自然 A 卷各 14 回完成**：`nature.html`（自然科總目錄）、`hanlin-nature-g7-1.html` + `hanlin-nature-g7-1/test1~14.html`、`hanlin-nature-g8-1.html` + `hanlin-nature-g8-1/test1~14.html`（圖在各自的 `images/testN/`）；首頁 `index.html` 的「自然」入口已開放。
  - 原始檔是掃描 PDF（`PDF-RAW-DATA/Nature/hanlin/hanlin-G7-1`、`hanlin-G8-1`），題目是看圖逐題打字，答案抄自各卷簡答。每回題型全是選擇題：一、選擇題 18 題、二、素養題 6～7 題（含題組）、B 部分 6～9 題（含題組），每回 31～34 題。
  - 簡答與題目不符時用 `Q(..., fix="C")` 強制改字母（檔案旁有註解）。
  - 產生方式：`tools/hanlin-g8-1-build/nat7data/tNN.py`（一上）、`natdata/tNN.py`（二上）→ `python gen_nature.py --g7`（不加 `--g7` 是二上）；`nat_view.py` 轉圖看題、`nat_sheet.py` 檢查附圖。每回的範圍與主題名在 `gen_nature.py` 的 `ROUNDS`。
  - 二上第 11～14 回：驗證過每題簡答與實際計算相符（熱傳播與比熱、元素與化合物、原子結構、複習），附圖都有載入。
  - 待辦：自然 B、C 卷。

### 2026-10-18（手機雲端版）
- **送出成績後每個大題列小計、答對的題目標得分**（使用者要求）：共用的 `sync.js` 的 `showSectionScores()`（`revealExamAnswers()` 時呼叫）：每個 `section.block` 的說明下面加「📊 本大題：答對 c / n 題　得 X / Y 分」，答對的題目 `.q-text` 後面加「+N 分」。每題幾分從大題說明 `.meta` 的「每題N分／每格N分」讀出；讀不到只列題數。按「重新作答」會清掉。
- **修正：還沒送出成績就能看「完整題目與解答」**：送出過一次後按「重新作答」，`printModeBtn` 沒有重新鎖住，下一次還沒送出就能點開看到正解（一、文意字彙和四、五大題的正解露出）。`sync.js` 重新作答時 `lockPrintMode()`（鎖回去，正在看解答就切回測驗模式），另外捕捉階段擋住：body 沒有 `exam-locked`（還沒送出）時點這顆一律不切換並提示。
- 實測（Playwright）：康軒七上英語第 1 回、翰林二上數學第 1 回、翰林二上地理第 1 回：送出前點解答被擋、送出後小計與 +N 分正確、重新作答後小計清掉且解答重新鎖住。所有頁面都載入 `sync.js`，不用改個別頁面。
- **修正：送出後切到「完整題目與解答」再切回來，作答全部不見、選項鎖住、再送出說「還有 25 題尚未作答」**（使用者回報）：各頁面的模式切換程式會把整份考卷重畫（`render()`）。改由 `sync.js` 用捕捉階段接手兩顆模式按鈕、不重畫：還沒送出不能看解答；送出後「完整題目與解答」在原本作答上顯示所有正解／詳解（body 加 `answer-view`），「測驗模式」切回來作答、對錯、小計都還在。實測英語、數學、地理、國文：送出→看解答→回測驗模式作答都在；重新作答後可改選、可再送出。
- **送出成績自動對答案＋訂正錯誤（使用者要求）**：都在 `sync.js`，所有頁面共用。
  - 送出成績後不用按鈕，直接顯示所有正解／詳解：答對綠色、答錯紅色（選項標「✗ 你的答案」「✓ 正解」）。上方「測驗模式／完整題目與解答」切換鈕藏起來。
  - 有錯題時，上方（`.controls` 下面）出現 `#fixBar`「✏️ 訂正錯誤」＋說明「錯誤全部訂正完畢再另加補送 1 點」。按下後：答對的題目鎖住（class `fix-locked`，不能改），答錯的題目清空作答、藏起正解（class `fixing`，黃框）；右下角按鈕變「送出訂正」。送出後再對答案，還有錯就再訂正，直到全對。
  - **測試帳號 TEST、家長 PARENT**：「訂正錯誤」旁多「🚪 立即離開」（`canSkipFix()`），按了解除訂正限制，出現「↩ 回單元目錄」（頁尾 `a.footer-link` 的網址）、「🏠 回主頁面」；學生帳號沒有這顆。
  - 還有錯題沒訂正完：點離開這一頁的連結會被擋（提示還有幾題），關分頁／重新整理會跳確認；「重新作答」按鈕藏起來。
  - 試算表：第一次照舊送全部題目；第 N 次訂正只送那次訂正的題目，單元名稱前加「【第 N 次訂正】」、回次後加「（第 N 次訂正）」（題目、作答、正解、對錯照常）；全部訂正完成另送一列「【全部訂正完成】補送 1 點」（回次「…（訂正完成）」）。成績單的 Apps Script 不在這些 repo 裡，沒辦法加新欄位，所以用這兩欄註明。
  - 點數：只有第一次作答算點數；全部訂正完成 `Points.earn({ mode:'訂正完成', kind:'fix-bonus', correct:1, total:1 })` 補送 1 點（後端要重新部署）。大題小計、+N 分都以第一次作答為準。
- **暫存（使用者要求）**：上方 `#draftBar`「💾 暫存」：作答時也會自動暫存（點選項、打字後 0.6 秒、離開頁面時），存在這台裝置的 localStorage `examDraft:頁面路徑:登入者`；下次用同一帳號打開同一頁自動接續（用頁面自己的點選／input 事件還原，選項用文字比對），顯示「📌 已接續 … 暫存的作答」與「清除暫存、重新開始」。送出成績或重新作答後清掉。只存在那台裝置（換電腦接不到）；訂正中不暫存（訂正完才能離開）。
- 實測（Playwright）：康軒七上英語第 1 回、翰林二上英語第 4 回（聽力）、數學第 1 回、地理第 1 回、國文第 1 回：錯 3 題→訂正兩次→全部完成補送；答對題目點不動；離開連結被擋；試算表送出內容正確；暫存→重新整理接續→清除。
- 測試帳號 TEST（家長在帳號管理建立）：成績照樣寫進試算表（只有 PARENT 不寫）；點數要記，TEST 的類型要是「學生」（「只能練習」不計點數）。

### 2026-10-17（手機雲端版）
- **翰林二上國文 B 卷、C 卷第 1～16 回完成**（共 32 頁）：`hanlin-chinese-g8-1/test1~16b.html`、`test1~16c.html`，目錄頁 `hanlin-chinese-g8-1.html` 的 B卷／C卷 按鈕已全部開放。
  - 資料在 `tools/hanlin-g8-1-build/chidataB/`、`chidataC/`（`tNN.py`），產生方式同 A 卷：`python gen_chinese.py`。
  - 版型和題型與 A 卷相同（注音國字、解釋、改錯、成語／配合題、基礎題、進階題、閱讀測驗、閱讀素養題；自學選文回是單題＋題組）。C 卷的「配合題」有詞性、句型、成語、詠物新詩等，一律做成選擇題。
  - 原卷是掃描檔，題目看圖逐題打字；答案全部對照各卷簡答。附圖：C 卷第 4 回圖像詩、第 10 回原住民玩偶圖（`images/test4c/`、`images/test10c/`）。
  - 簡答沒列答案的題目（B 卷第 4、8、13 回的閱讀素養題）依文意判定，檔案旁有註解。簡答印錯字的兩題（B 卷第 4 回改錯「巒」、第 13 回「樁」），兩種寫法都算對。
  - 32 頁都驗證過：每題正解都判為正確、沒有 JS 錯誤、附圖都有載入。用的是 10-18 新版範本（`sync.js?v=20261018b`，有訂正錯誤、暫存）。
- 待辦：國文一上（翰林）B、C 卷（原始檔在 `PDF-RAW-DATA/Chinese/hanlin/hanlin-G7-1/`）。

### 2026-10-21（手機雲端版）
- **修正：翰林一上英語整頁空白**：`hanlin-g7-1.html` 和 `hanlin-g7-1/test1~14.html` 都殘留合併衝突標記（`<<<<<<< Updated upstream`／`>>>>>>> Stashed changes`，GitHub Desktop 的 stash 還原時留下的），JS 壞掉、目錄頁空白。用 `eng7data` 重新產生後內容等於「Stashed」那一邊。**以後 Pull 前若 GitHub Desktop 跳出 stash／衝突，先別 Commit，問 Claude 處理。**
  - `gen.py` 的 `REPO` 和 `gen_eng7.py` 的 `SRC` 改成相對路徑（讀 `PDF-RAW-DATA/english/hanlin/hanlin-g7-1/`），任何電腦都能跑：`python gen_eng7.py`。
- **翰林一上英語 B 卷、C 卷第 1～14 回完成**（共 28 頁，聽力第 5、9、13 回，音檔每卷 9 軌、依舊對應 1～3／4～6／7～9）。資料在 `tools/hanlin-g8-1-build/eng7dataB/`、`eng7dataC/`。目錄頁 B／C 卷按鈕已全部開放。
  - 原卷是掃描檔，看圖逐題打字；選擇題答案全部對過各卷簡答。附圖用 `CROPS` 從原卷裁切（P() 用 PDF pt 座標）。
  - C 卷的「依句意填入代號」做成選擇題（選項是那組 A～G 句子）；「依照字母順序寫出缺少的字母」做成一格依序填兩個字母（大小寫要對）。
  - 英語範本不顯示 `note`，說明都寫在 `meta` 裡。
  - 28 頁都驗證過：每題填正解都判為正確、沒有 JS 錯誤、附圖與音檔都有載入。

### 待辦／注意
- 以上變更要在 GitHub Desktop 裡 Commit + Push，換電腦後先 Pull。
- 尚未製作：翰林二上數學網頁（原始檔已放進 `PDF-RAW-DATA/MATH/hanlin/hanlin-g8-1/`）。另外康軒數學 K 卷只在 OneDrive 裡，沒有放進專案。
- 國文一上（翰林）B、C 卷還沒做（原始檔在 `PDF-RAW-DATA/Chinese/hanlin/hanlin-G7-1/`）；二上 B、C 卷已於 10/17 完成。
- 學生名單不再寫在 `sync.js`：改由點數存摺的登入帳號決定（家長在「帳號管理」建立）。

## 測驗規則統一以段考題庫為準（2026-10-18 使用者要求，以後新做的測驗也照做）

- **成長學習館各單元有測驗的地方，作答、送出、計分、訂正方式一律以國中英語段考題庫（exam-bank `sync.js`）為準**（使用者已測試驗證 OK）：
  送出成績（全部作答才送）→ 馬上對答案（綠對紅錯＋正解）→ 有錯題時上方「✏️ 訂正錯誤」＋「錯誤全部訂正完畢再另加補送 1 點」（答對的鎖住、錯題清空重答）→「送出訂正」直到全對 → 補送 1 點（`Points.earn` `kind:'fix-bonus'`）；
  沒訂正完不能離開這一頁（擋連結、關分頁跳確認）；測試帳號 TEST、家長 PARENT 有「🚪 立即離開」；試算表每次訂正 mode／單元名稱註明「【第 N 次訂正】」、完成記「【全部訂正完成】補送 1 點」；點數只算第一次作答；「💾 暫存」＋自動暫存接續作答。
- 各站的做法：段考題庫 `sync.js`；圖解單字 `topic.html`；國家地理閱讀 `fixkit.js`（`points-glue.js` 載入）；英文測驗系統 `eqfix.js`；美式生活館 `lifefix.js`（engine.js、index.html 用）。
  英文測驗系統、美式生活館是「一題一題做、答完看解說」的形式，使用者選擇保留，只把結果頁改成訂正規則（只重做錯題、直到全對）。
- 這個 repo 是標準（`sync.js`）。其他站改測驗時以這裡的行為為準。

- **快取（2026-10-18）**：各頁用 `sync.js?v=20261018b` 載入共用程式；**改了共用程式要把所有頁面的 v 一起改**（sed 全部替換），不然手機瀏覽器會繼續用舊版（使用者 10-18 看到沒有「訂正錯誤」）。

## 連續學習紅利＋稱讚畫面（2026-10-18）

- 送出測驗後跳出稱讚卡（得幾點、連續第幾天、還差幾點到 100 點）；每跨過 100 點跳出大的恭喜兌換畫面。
- 連續學習紅利：第 2 天 +2、第 3、4 天 +3、第 5 天起每天 +4（2026-10-18 使用者改），中斷就重算；不算在每天 50 點上限內；存摺分頁記成類型「紅利」。
- **答對率計分（2026-10-18）**：答對 1 題得幾點看答對率（第三版，2026-10-18 使用者定）：低於 30% 0.25、30～50% 0.5、50～60% 0.8、60～70% 1、70～90% 1.2、90% 以上 1.5、全對 2，四捨五入成整數（80～90% 使用者沒另外寫，同 7～8 成）；後端 `Code.gs` 的 `CONFIG.RATE_TIERS`，要重新部署 Apps Script 才生效。
- **段考訂正完成補送 1 點（2026-10-18）**：段考題庫錯題全部訂正完成後 `Points.earn({kind:'fix-bonus'})`，後端 `fixBonus_()` 記一筆類型「訂正獎勵」+`CONFIG.FIX_BONUS`（1）點，同一份考卷每天一次、不算每天上限與連續天數；要重新部署 Apps Script 才生效（舊版後端會當成一般賺點、全對每題 2 點＝給 2 點）。
- 程式在 `points.js`（7 份副本內容一致，主檔在 english-quiz-plan `points/points.js`）與後端 `Code.gs`（`CONFIG.STREAK_BONUS`）。
- **要先更新 Apps Script 後端（貼新版 Code.gs → 部署新版本）紅利才會開始算**，步驟在 english-quiz-plan `points/README-點數存摺.md` 最後一節。
