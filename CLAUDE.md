# exam-bank（國中段考題庫）

靜態網站（GitHub Pages），學生做線上練習卷，成績透過 `sync.js` 送到 Google 試算表。
本機預覽：`python -m http.server 8532`（設定在 `.claude/launch.json`）。

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

### 待辦／注意
- 以上變更要在 GitHub Desktop 裡 Commit + Push，換電腦後先 Pull。
- 尚未製作：翰林二上數學網頁（原始檔已放進 `PDF-RAW-DATA/MATH/hanlin/hanlin-g8-1/`）。另外康軒數學 K 卷只在 OneDrive 裡，沒有放進專案。
- 國文一上、二上（翰林）B、C 卷還沒做（原始檔在 `PDF-RAW-DATA/Chinese/hanlin/hanlin-G7-1/`、`hanlin-G8-1/`）。
- 學生名單不再寫在 `sync.js`：改由點數存摺的登入帳號決定（家長在「帳號管理」建立）。
