"""Generate 翰林版七年級英語（一）A/B/C pages (hanlin-g7-1/) from e7data*/tNN.py, plus the catalog hanlin-g7-1.html.
Templates: tpl_written.html / tpl_listen.html (same as 八上). Paths are relative to the repo, so it runs on any computer.
Run:  python gen_e7.py"""
import json, re, importlib.util, glob, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
OUTDIR = os.path.join(REPO, "hanlin-g7-1")
BOOK = "翰林版七年級英語（一）"
FULL = {"A": "Ａ", "B": "Ｂ", "C": "Ｃ"}
VERSIONS = [("A", "e7data", ""), ("B", "e7dataB", "b"), ("C", "e7dataC", "c")]
LISTEN_INDEX = {5: ("Starter Unit～Unit 2", "聽力測驗一"), 9: ("Unit 3～4", "聽力測驗二"), 13: ("Unit 5～6", "聽力測驗三")}
BACK = "../hanlin-g7-1.html"

def rd(p): return open(p, encoding="utf-8").read()
def wr(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f: f.write(s)

def sub1(s, old, new, count=1):
    n = s.count(old)
    assert n == count, f"expected {count} of {old[:60]!r}, found {n}"
    return s.replace(old, new)

def resub(s, pat, new):
    s2, n = re.subn(pat, lambda m: new, s, count=1, flags=re.S)
    assert n == 1, pat
    return s2

# ---------- written-test template ----------
W = rd(os.path.join(HERE, "tpl_written.html"))
W = sub1(W, "../kangxuan-g8-1.html", BACK, 2)
# section-level image (e.g. one map shared by a whole section)
W = sub1(W, "  if(sec.wordbank){", """  if(sec.image){
    const im = document.createElement("img");
    im.src = sec.image; im.alt = "題目附圖";
    im.style.cssText = "width:100%;max-width:" + (sec.imageWidth || 560) + "px;display:block;margin:0 auto 16px;border-radius:8px;border:1px solid var(--paper-line);";
    block.appendChild(im);
  }

  if(sec.wordbank){""")
# vocab: optional exact-case matching (sec.exact / it.exact), items with several blanks (answers:[...]), numbering offset
old_vocab = """      q.innerHTML = `<div class="q-text"><span class="q-num">${i+1}.</span>${it.q}
        &nbsp; <input type="text" class="blank" data-answer="${it.answer}" placeholder="填入單字">
        <span class="feedback"></span></div>
        <div class="answer-reveal">正解：${it.answer}</div>`;
      const input = q.querySelector("input");
      input.addEventListener("input", ()=>checkBlank(input));"""
new_vocab = """      const ex = (sec.exact || it.exact) ? ' data-exact="1"' : '';
      if(it.answers){
        q.innerHTML = `<div class="q-text"><span class="q-num">${(sec.start||1)+i}.</span>${it.q}
          &nbsp; ${it.answers.map(a=>`<input type="text" class="micro-blank"${ex} data-answer="${a}" style="width:${Math.max(90,a.length*13)}px;" placeholder="填入單字">`).join(" ")}</div>
          <div class="answer-reveal">正解：${it.answers.join(", ")}</div>`;
        q.querySelectorAll(".micro-blank").forEach(inp=>inp.addEventListener("input", ()=>checkMultiBlank(q)));
      } else {
        q.innerHTML = `<div class="q-text"><span class="q-num">${(sec.start||1)+i}.</span>${it.q}
          &nbsp; <input type="text" class="blank"${ex} data-answer="${it.answer}" placeholder="填入單字">
          <span class="feedback"></span></div>
          <div class="answer-reveal">正解：${it.answer}</div>`;
        const input = q.querySelector("input");
        input.addEventListener("input", ()=>checkBlank(input));
      }"""
W = sub1(W, old_vocab, new_vocab)
# question numbering can start from an offset (題組 13–28)
W = sub1(W, "${it.q ? `<span class=\"q-num\">${i+1}.</span>${it.q}` : `<span class=\"q-num\">${i+1}.</span>`}",
            "<span class=\"q-num\">${(sec.start||1)+i}.</span>${it.q||\"\"}")
# cloze renderer (numbering offset)
W = sub1(W, '  else if(sec.type==="reading"){', """  else if(sec.type==="cloze"){
    const passageDiv = document.createElement("div");
    passageDiv.className = "passage";
    passageDiv.textContent = sec.passage;
    block.appendChild(passageDiv);
    sec.items.forEach((it,i)=>{
      const q = document.createElement("div");
      q.className = "q";
      const optsHtml = it.options.map((op,oi)=>`
        <div class="opt" data-idx="${oi}" data-correct="${oi===it.correct}">
          <span class="tag">(${String.fromCharCode(65+oi)})</span><span>${op}</span>
        </div>`).join("");
      q.innerHTML = `<div class="q-text"><span class="q-num">${(sec.start||1)+i}.</span></div><div class="opts">${optsHtml}</div>`;
      q.querySelectorAll(".opt").forEach(optEl=>{
        if(optEl.dataset.correct==="true") optEl.classList.add("is-correct");
        optEl.addEventListener("click", ()=>selectOption(q, optEl));
      });
      block.appendChild(q);
    });
  }

  else if(sec.type==="reading"){""")
W = sub1(W, '<div class="q-text"><span class="q-num">${i+1}.</span>${it.q}</div>\n          ${it.image',
            '<div class="q-text"><span class="q-num">${(p.start||1)+i}.</span>${it.q}</div>\n          ${it.image')
# picture for guided (看圖回答)
W = sub1(W, '<div class="q-text"><span class="q-num">${i+1}.</span>${prompt}</div>',
            '<div class="q-text"><span class="q-num">${i+1}.</span>${prompt}</div>\n        ${it.image ? `<img src="${it.image}" alt="題目附圖" style="width:100%;max-width:${it.imageWidth||240}px;display:block;border-radius:8px;margin:4px 0 8px;border:1px solid var(--paper-line);">`:""}')
# passage picture / poster for 閱讀
W = sub1(W, '${p.text}${p.table ? renderTable(p.table) : ""}',
            '${p.text}${p.image ? `<img src="${p.image}" alt="附圖" style="width:100%;max-width:${p.imageWidth||520}px;display:block;margin:10px auto 0;border-radius:8px;border:1px solid var(--paper-line);">`:""}${p.table ? renderTable(p.table) : ""}')
# guided-multi: optional picture above the sentence, exact-case blanks (it.exact / sec.exact)
W = sub1(W, '''? `<input type="text" class="micro-blank" data-answer="${part}" style="width:${Math.max(60,part.length*13)}px;">`''',
            '''? `<input type="text" class="micro-blank"${(sec.exact||it.exact)?' data-exact="1"':''} data-answer="${part}" style="width:${Math.max(60,part.length*13)}px;">`''')
W = sub1(W, '''      q.innerHTML = `<div class="q-text"><span class="q-num">${i+1}.</span>${it.zh ? it.zh+"<br>" : ""}${linesHtml}</div>''',
            '''      q.innerHTML = `${it.image ? `<img src="${it.image}" alt="題目附圖" style="width:100%;max-width:${it.imageWidth||220}px;display:block;border-radius:8px;margin:0 0 6px;border:1px solid var(--paper-line);">`:""}<div class="q-text"><span class="q-num">${(sec.start||1)+i}.</span>${it.zh ? it.zh+"<br>" : ""}${linesHtml}</div>''')
# blank checking: curly apostrophes, optional exact case, alternatives separated by "/"
W = sub1(W, """function checkBlank(input){
  const val = input.value.trim().toLowerCase();
  const ans = input.dataset.answer.trim().toLowerCase();""",
"""function normTxt(s, exact){ s = s.trim().replace(/[’‘]/g, "'").replace(/[-‐–]/g, " ").replace(/\\s+/g, " "); return exact ? s : s.toLowerCase(); }
function checkBlank(input){
  const ex = input.dataset.exact==="1";
  const val = normTxt(input.value, ex);
  const ans = normTxt(input.dataset.answer, ex);""")
W = sub1(W, "inp.value.trim().toLowerCase() === inp.dataset.answer.trim().toLowerCase()",
            'inp.dataset.answer.split("/").some(a=>normTxt(a, inp.dataset.exact==="1") === normTxt(inp.value, inp.dataset.exact==="1"))')

# ---------- listening template ----------
L = rd(os.path.join(HERE, "tpl_listen.html"))
L = sub1(L, "../kangxuan-g8-1.html", BACK, 2)
L = sub1(L, 'q.innerHTML = `<div class="q-text"><span class="q-num">${i+1}.</span>${it.q||""}</div><div class="opts">${optsHtml}</div>`;',
            'q.innerHTML = `<div class="q-text"><span class="q-num">${i+1}.</span>${it.q||""}</div>${it.image ? `<img class="grid-img" src="${it.image}" alt="題目附圖">` : ""}<div class="opts">${optsHtml}</div>`;')

def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def js(o): return json.dumps(o, ensure_ascii=False, indent=2)

exams = {}
for ver, folder, suf in VERSIONS:
    for path in sorted(glob.glob(os.path.join(HERE, folder, "t*.py"))):
        m = load(path); meta = m.META; n = meta["n"]; h1 = meta["h1"]
        tag = f"{BOOK}{FULL[ver]}卷"
        if getattr(m, "LISTENING", False):
            page = L
            page = resub(page, r"<title>.*?</title>", f"<title>段考題庫｜第{n}回 - {meta['title']}</title>")
            page = resub(page, r"<h1>.*?</h1>", f"<h1>{h1}</h1>")
            page = resub(page, r'<p class="subtitle">.*?</p>', f'<p class="subtitle">{meta["subtitle"]}｜{tag}</p>')
            blocks = "".join(f"""  <section class="block">
    <h2>{s['title']}</h2>
    <p class="meta">{s['meta']}</p>
    <audio controls src="audio/test{n}{suf}/track{s['track']}.mp3"></audio>
    <div id="sec{k}"></div>
  </section>

""" for k, s in enumerate(m.SECTIONS, 1))
            page = resub(page, r"<main>\n.*?  <a class=\"footer-link\"", f"<main>\n{blocks}  <a class=\"footer-link\"")
            calls = "\n".join(f"// {s['title']}\nmc(document.getElementById(\"sec{k}\"), {js(s['items'])});\n" for k, s in enumerate(m.SECTIONS, 1))
            page = resub(page, r"\n// 一、選出聽到的字詞.*?</script>", "\n" + calls + "</script>")
            page = resub(page, r"window\.EXAM_META = \{.*?\};", f'window.EXAM_META = {{version:"{ver}卷", examLabel:"第{n}回"}};')
            (lesson, title), kind = LISTEN_INDEX[n], "聽力"
        else:
            page = W
            page = resub(page, r"<title>.*?</title>", f"<title>段考題庫｜第{n}回 - {h1.split('・')[1]}</title>")
            page = resub(page, r"<h1>.*?</h1>", f"<h1>{h1}</h1>")
            page = resub(page, r'<p class="subtitle">.*?</p>', f'<p class="subtitle">{meta["subtitle"]}｜{tag}</p>')
            data = f'window.EXAM_META = {{ version: "{ver}卷", examLabel: "第{n}回" }};\nconst DATA = {{\n  sections: {js(m.SECTIONS)}\n}};\n'
            page = resub(page, r"window\.EXAM_META = \{.*?\n\};\n", data)
            lesson, title, kind = meta.get("lesson", h1.split("・")[1]), meta.get("ctitle", meta["subtitle"]), "筆試"
        assert "kangxuan" not in page and "康軒" not in page, f"leftover 康軒 text in test{n}{suf}"
        name = f"test{n}{suf}.html"
        wr(os.path.join(OUTDIR, name), page)
        exams.setdefault(n, dict(lesson=lesson, title=title, type=kind, hrefs={}))["hrefs"][ver] = f"hanlin-g7-1/{name}"
        print("wrote", name)

# ---------- catalog (from 康軒 kangxuan-g7-1.html) ----------
I = rd(os.path.join(REPO, "kangxuan-g7-1.html"))
I = sub1(I, "康軒版七年級英語（一）", BOOK, 2)
def h(e, v): return json.dumps(e["hrefs"][v]) if v in e["hrefs"] else "null"
rows = [f'      {{n:{n}, lesson:{json.dumps(e["lesson"], ensure_ascii=False)}, title:{json.dumps(e["title"], ensure_ascii=False)}, type:"{e["type"]}", href:{h(e,"A")}, hrefB:{h(e,"B")}, hrefC:{h(e,"C")}}}'
        for n, e in sorted(exams.items())]
I = resub(I, r"const EXAMS = \[\n.*?\n    \];", "const EXAMS = [\n" + ",\n".join(rows) + "\n    ];")
wr(os.path.join(REPO, "hanlin-g7-1.html"), I)
print("wrote hanlin-g7-1.html")
