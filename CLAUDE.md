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
- 社會七上（翰林）是在家裡電腦做的，做到地理第 5 回 A 卷。截至 10/02 上午**尚未 Push 到 GitHub**。

### 待辦／注意
- 以上變更要在 GitHub Desktop 裡 Commit + Push，換電腦後先 Pull。
- 尚未製作：翰林二上數學網頁（原始檔已放進 `PDF-RAW-DATA/MATH/hanlin/hanlin-g8-1/`）。另外康軒數學 K 卷只在 OneDrive 裡，沒有放進專案。
- 學生名單寫在 `sync.js` 的 `<select>`（目前是 BRANDEN、MELISSA）。
