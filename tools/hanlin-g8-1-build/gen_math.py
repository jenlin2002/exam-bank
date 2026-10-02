"""Generate 翰林版八年級數學（三） pages (hanlin-math-g8-1/) from mathdata/tNN.py.
Built on the English written-test template from gen.py, plus KaTeX and two new section types:
  fill  — short answer, auto-graded against `answers` (normalised: spaces, ^, ², −, ×, π/pi, units)
  calc  — worked problem; no input, reference answer revealed after submitting
mc items may also carry `pre` (shared passage text) and `preImage`."""
import os, json, glob, sys

HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, "gen.py"), encoding="utf-8").read().split("\nexams = []\n")[0])  # W, helpers

# python gen_math.py        -> 翰林二上 (mathdata*/ -> hanlin-math-g8-1/)
# python gen_math.py --g7   -> 翰林一上 (math7data*/ -> hanlin-math-g7-1/)
G7 = "--g7" in sys.argv
BOOK_M = "翰林版七年級數學（一）" if G7 else "翰林版八年級數學（三）"
SLUG = "hanlin-math-g7-1" if G7 else "hanlin-math-g8-1"
DATA_PREFIX = "math7data" if G7 else "mathdata"
OUTDIR_M = os.path.join(REPO, SLUG)
FULL = {"A": "Ａ", "B": "Ｂ", "C": "Ｃ"}

M = W
M = sub1(M, "../hanlin-g8-1.html", f"../{SLUG}.html", 2)
M = sub1(M, "（僅計算選擇題與字彙填空）", "（僅計算選擇題與填充題）")
M = sub1(M, "</style>", """  .katex{font-size:1.05em;}
  .q-text .katex-display{margin:6px 0;}
  .parts{margin:6px 0 4px 1.4em;padding:0;}
  .parts li{margin-bottom:4px;}
  input.math-blank{width:200px;}
  .fill-hint{font-size:12.5px;color:var(--ink-soft);margin-left:4px;}
  .calc-stem{margin:18px 0 8px;}
  .calc-stem:first-of-type{margin-top:0;}
  .q.calc-part{margin-left:1.4em;}
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js"></script>""")
# typeset math after every render (quiz/print mode switch, 重新作答)
M = sub1(M, "\n}\n\nfunction renderTable(t){", """
  if(window.renderMathInElement){
    renderMathInElement(contentEl, {delimiters:[{left:"$", right:"$", display:false}], throwOnError:false});
  }
}

function renderTable(t){""")
# mc: optional shared passage before a question
M = sub1(M, '`<div class="q-text"><span class="q-num">${(sec.start||1)+i}.</span>${it.q||""}</div>',
            '`${it.pre ? `<div class="passage">${it.pre}${it.preImage ? `<img src="${it.preImage}" alt="附圖" style="width:100%;max-width:420px;display:block;margin:10px auto 0;border-radius:8px;border:1px solid var(--paper-line);background:#fff;">` : ""}</div>` : ""}<div class="q-text"><span class="q-num">${(sec.start||1)+i}.</span>${it.q||""}</div>')
FIG = '${it.image ? `<img src="${it.image}" alt="題目附圖" style="width:100%;max-width:260px;display:block;border-radius:8px;margin:4px 0 10px;border:1px solid var(--paper-line);background:#fff;">`:""}'
M = sub1(M, '  else if(sec.type==="reading"){', """  else if(sec.type==="fill"){
    sec.items.forEach((it,i)=>{
      const q = document.createElement("div");
      q.className = "q";
      q.innerHTML = `<div class="q-text"><span class="q-num">${it.num || ((sec.start||1)+i)+"."}</span>${it.q}</div>
        """ + FIG + """
        <div><input type="text" class="blank math-blank" placeholder="填入答案" autocomplete="off"><span class="feedback"></span>${it.hint ? `<span class="fill-hint">（${it.hint}）</span>` : ""}</div>
        <div class="answer-reveal">正解：${it.show}</div>`;
      const input = q.querySelector("input");
      input.dataset.answer = it.answers[0];
      input.addEventListener("input", ()=>checkMath(input, it.answers));
      block.appendChild(q);
    });
  }

  else if(sec.type==="calc"){
    // 題幹＋附圖，每個小題各自一格最後答案（自動批改）；過程寫在紙上
    sec.items.forEach((it,i)=>{
      const stem = document.createElement("div");
      stem.className = "calc-stem";
      stem.innerHTML = `<div class="q-text"><span class="q-num">${(sec.start||1)+i}.</span>${it.q}</div>
        """ + FIG + """`;
      block.appendChild(stem);
      it.parts.forEach((pt,pi)=>{
        const q = document.createElement("div");
        q.className = "q calc-part";
        q.innerHTML = `<div class="q-text"><span class="q-num">${pt.label || "("+(pi+1)+")"}</span>${pt.p}</div>
          <div><input type="text" class="blank math-blank" placeholder="填入最後答案" autocomplete="off"><span class="feedback"></span>${pt.hint ? `<span class="fill-hint">（${pt.hint}）</span>` : ""}</div>
          <div class="answer-reveal">正解：${pt.show}</div>`;
        const input = q.querySelector("input");
        input.dataset.answer = pt.answers[0];
        input.addEventListener("input", ()=>checkMath(input, pt.answers));
        block.appendChild(q);
      });
    });
  }

  else if(sec.type==="reading"){""")
M = sub1(M, "function updateScore(){", """function normMath(s){
  return s.toLowerCase()
    .replace(/(\\d)\\s*x\\s*(?=\\d)/g,"$1*")
    .replace(/[＋]/g,"+").replace(/[，、；;]/g,",").replace(/[（]/g,"(").replace(/[）]/g,")").replace(/[＝]/g,"=").replace(/[：]/g,":").replace(/[＜]/g,"<").replace(/[＞]/g,">").replace(/[－−–—]/g,"-").replace(/[×＊]/g,"*").replace(/[／÷]/g,"/")
    .replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹]/g, c=>"⁰¹²³⁴⁵⁶⁷⁸⁹".indexOf(c)).replace(/\\^/g,"").replace(/π/g,"pi")
    .replace(/根號|sqrt/g,"√").replace(/\\+-|\\+\\/-/g,"±").replace(/或|or|and|和/g,",")
    .replace(/[\\s　]+/g,"")
    .replace(/平方公分|平方公尺|平方公寸|平方單位|公分|公尺|公寸|單位|毫升|公克|公斤|公里|元|個|人|題|秒|次|片|班|瓶蓋|顆|杯|圈|歲|位|天|%|％|°c|度|\\(重根\\)|重根/g,"")
    .replace(/√\\((\\w+)\\)/g,"√$1").replace(/[。．.]+$/,"");
}
// 「或」「,」分隔的多個答案不計順序；座標 (a,b) 等括號包住的整串保留順序
function canonMath(s){
  let t = normMath(s).replace(/\\*/g,"");
  // 因式分解：係數＋括號因式的乘積，因式順序不同也算對
  const m = t.match(/^(-?\\d*)((?:\\([^()]+\\)\\d?)+)$/);
  if(m) t = m[1] + m[2].match(/\\([^()]+\\)\\d?/g).sort().join("");
  if(!t.includes(",") || /^\\(.*\\)$/.test(t)) return t;
  return t.split(",").filter(Boolean).sort().join(",");
}
function checkMath(input, answers){
  const qEl = input.closest(".q");
  const val = input.value.trim();
  if(!val){ delete qEl.dataset.studentAnswer; updateScore(); return; }
  qEl.dataset.studentAnswer = val;
  qEl.dataset.correctAnswer = answers[0];
  qEl.dataset.isCorrect = answers.some(a=>canonMath(a)===canonMath(val)) ? "true" : "false";
  updateScore();
}

function updateScore(){""")

def page_for(m, ver, suf):
    meta, n = m.META, m.META["n"]
    p = M
    p = resub(p, r"<title>.*?</title>", f"<title>段考題庫｜第{n}回 - {meta['lesson']} {meta['title']}</title>")
    p = resub(p, r"<h1>.*?</h1>", f"<h1>{meta['h1']}</h1>")
    p = resub(p, r'<p class="subtitle">.*?</p>', f'<p class="subtitle">{meta["subtitle"]}｜{BOOK_M}{FULL[ver]}卷</p>')
    data = f'window.EXAM_META = {{ version: "數學{ver}卷", examLabel: "第{n}回" }};\nconst DATA = {{\n  sections: {js(m.SECTIONS)}\n}};\n'
    p = resub(p, r"window\.EXAM_META = \{.*?\n\};\n", data)
    assert "kangxuan" not in p and "康軒" not in p and "英語" not in p, f"leftover text in math test{n}{suf}"
    return p

exams = {}
for ver, folder, suf in [("A", DATA_PREFIX, ""), ("B", DATA_PREFIX + "B", "b"), ("C", DATA_PREFIX + "C", "c")]:
    for path in sorted(glob.glob(os.path.join(HERE, folder, "t*.py"))):
        m = load(path); n = m.META["n"]
        name = f"test{n}{suf}.html"
        os.makedirs(OUTDIR_M, exist_ok=True)
        wr(os.path.join(OUTDIR_M, name), page_for(m, ver, suf))
        e = exams.setdefault(n, dict(lesson=m.META["lesson"], title=m.META["title"], hrefs={}))
        e["hrefs"][ver] = f"{SLUG}/{name}"
        print("wrote", name)

# book index (from the 翰林英語 index) and subject page (from english.html)
I = rd(os.path.join(REPO, "hanlin-g8-1.html"))
I = sub1(I, "翰林版八年級英語（三）", BOOK_M, 2)
I = sub1(I, '<a href="english.html" style="color:#cfe0d1;">英語科</a>', '<a href="math.html" style="color:#cfe0d1;">數學科</a>')
I = sub1(I, '<a class="footer-link" href="english.html">← 回英語科總目錄</a>', '<a class="footer-link" href="math.html">← 回數學科總目錄</a>')
def h(e, v): return json.dumps(e["hrefs"][v]) if v in e["hrefs"] else "null"
rows = [f'      {{n:{n}, lesson:{json.dumps(e["lesson"], ensure_ascii=False)}, title:{json.dumps(e["title"], ensure_ascii=False)}, type:"筆試", href:{h(e,"A")}, hrefB:{h(e,"B")}, hrefC:{h(e,"C")}}}'
        for n, e in sorted(exams.items())]
I = resub(I, r"const EXAMS = \[\n.*?\n    \];", "const EXAMS = [\n" + ",\n".join(rows) + "\n    ];")
wr(os.path.join(REPO, f"{SLUG}.html"), I)
print(f"wrote {SLUG}.html")

S = rd(os.path.join(REPO, "english.html"))
S = sub1(S, "<title>國中題庫｜英語科總目錄</title>", "<title>國中題庫｜數學科總目錄</title>")
S = sub1(S, "<h1>英語科</h1>", "<h1>數學科</h1>")
S = sub1(S, "版英語段考題庫", "版數學段考題庫")
S = S.replace('href:"kangxuan-g7-1.html"', "href:null").replace('href:"kangxuan-g7-2.html"', "href:null").replace('href:"kangxuan-g8-1.html"', "href:null").replace('href:"hanlin-g8-1.html"', "href:null")
# every 翰林 math book that has an index page gets its card switched on
for grade, slug in [("國中一上", "hanlin-math-g7-1"), ("國中二上", "hanlin-math-g8-1")]:
    if os.path.exists(os.path.join(REPO, slug + ".html")):
        S = sub1(S, f'{{grade:"{grade}", items:[\n        {{pub:"康軒", href:null}},\n        {{pub:"翰林", href:null}},',
                    f'{{grade:"{grade}", items:[\n        {{pub:"康軒", href:null}},\n        {{pub:"翰林", href:"{slug}.html"}},')
assert "英語" not in S
wr(os.path.join(REPO, "math.html"), S)
print("wrote math.html")
