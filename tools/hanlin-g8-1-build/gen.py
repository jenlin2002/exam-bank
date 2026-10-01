"""Generate 翰林版八年級英語（三）A卷 pages from data/tNN.py, using the 康軒 pages as templates."""
import json, re, importlib.util, glob, os

REPO = r"E:\GitHub\exam-bank"
OUTDIR = os.path.join(REPO, "hanlin-g8-1")
BOOK = "翰林版八年級英語（三）"
HERE = os.path.dirname(os.path.abspath(__file__))

def rd(p): return open(p, encoding="utf-8").read()
def wr(p, s):
    with open(p, "w", encoding="utf-8", newline="\n") as f: f.write(s)

def sub1(s, old, new, count=1):
    n = s.count(old)
    assert n == count, f"expected {count} of {old[:60]!r}, found {n}"
    return s.replace(old, new)

def resub(s, pat, new):
    s2, n = re.subn(pat, lambda m: new, s, count=1, flags=re.S)
    assert n == 1, pat
    return s2

# ---------- written-test template (from 康軒 test11c, the newest renderer) ----------
W = rd(os.path.join(HERE, "tpl_written.html"))
W = sub1(W, "../kangxuan-g8-1.html", "../hanlin-g8-1.html", 2)
# section-level image (e.g. one map shared by a whole section)
W = sub1(W, "  if(sec.wordbank){", """  if(sec.image){
    const im = document.createElement("img");
    im.src = sec.image; im.alt = "題目附圖";
    im.style.cssText = "width:100%;max-width:560px;display:block;margin:0 auto 16px;border-radius:8px;border:1px solid var(--paper-line);";
    block.appendChild(im);
  }

  if(sec.wordbank){""")
# vocab items with two blanks (answers:[...])
old_vocab = """      q.innerHTML = `<div class="q-text"><span class="q-num">${i+1}.</span>${it.q}
        &nbsp; <input type="text" class="blank" data-answer="${it.answer}" placeholder="填入單字">
        <span class="feedback"></span></div>
        <div class="answer-reveal">正解：${it.answer}</div>`;
      const input = q.querySelector("input");
      input.addEventListener("input", ()=>checkBlank(input));"""
new_vocab = """      if(it.answers){
        q.innerHTML = `<div class="q-text"><span class="q-num">${(sec.start||1)+i}.</span>${it.q}
          &nbsp; ${it.answers.map(a=>`<input type="text" class="micro-blank" data-answer="${a}" style="width:${Math.max(90,a.length*13)}px;" placeholder="填入單字">`).join(" ")}</div>
          <div class="answer-reveal">正解：${it.answers.join(", ")}</div>`;
        q.querySelectorAll(".micro-blank").forEach(inp=>inp.addEventListener("input", ()=>checkMultiBlank(q)));
      } else {
        q.innerHTML = `<div class="q-text"><span class="q-num">${(sec.start||1)+i}.</span>${it.q}
          &nbsp; <input type="text" class="blank" data-answer="${it.answer}" placeholder="填入單字">
          <span class="feedback"></span></div>
          <div class="answer-reveal">正解：${it.answer}</div>`;
        const input = q.querySelector("input");
        input.addEventListener("input", ()=>checkBlank(input));
      }"""
W = sub1(W, old_vocab, new_vocab)
# question numbering can start from an offset (題組 13–28)
W = sub1(W, "${it.q ? `<span class=\"q-num\">${i+1}.</span>${it.q}` : `<span class=\"q-num\">${i+1}.</span>`}",
            "<span class=\"q-num\">${(sec.start||1)+i}.</span>${it.q||\"\"}")
# test11c has no 克漏字 renderer; bring in the one from 康軒 test1 (with numbering offset)
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
# picture for 看圖詳答
W = sub1(W, '<div class="q-text"><span class="q-num">${i+1}.</span>${prompt}</div>',
            '<div class="q-text"><span class="q-num">${i+1}.</span>${prompt}</div>\n        ${it.image ? `<img src="${it.image}" alt="題目附圖" style="width:100%;max-width:240px;display:block;border-radius:8px;margin:4px 0 8px;border:1px solid var(--paper-line);">`:""}')
# passage picture / poster for 閱讀
W = sub1(W, '${p.text}${p.table ? renderTable(p.table) : ""}',
            '${p.text}${p.image ? `<img src="${p.image}" alt="附圖" style="width:100%;max-width:520px;display:block;margin:10px auto 0;border-radius:8px;border:1px solid var(--paper-line);">`:""}${p.table ? renderTable(p.table) : ""}')
# multi-blank answers may list alternatives: "Living/To live"
W = sub1(W, "inp.value.trim().toLowerCase() === inp.dataset.answer.trim().toLowerCase()",
            "inp.dataset.answer.split(\"/\").some(a=>a.trim().toLowerCase() === inp.value.trim().toLowerCase())")

# ---------- listening template (from 康軒 test4) ----------
L = rd(os.path.join(HERE, "tpl_listen.html"))
L = sub1(L, "../kangxuan-g8-1.html", "../hanlin-g8-1.html", 2)
L = sub1(L, 'q.innerHTML = `<div class="q-text"><span class="q-num">${i+1}.</span>${it.q||""}</div><div class="opts">${optsHtml}</div>`;',
            'q.innerHTML = `<div class="q-text"><span class="q-num">${i+1}.</span>${it.q||""}</div>${it.image ? `<img class="grid-img" src="${it.image}" alt="題目附圖">` : ""}<div class="opts">${optsHtml}</div>`;')

def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def js(o): return json.dumps(o, ensure_ascii=False, indent=2)

exams = []
for path in sorted(glob.glob(os.path.join(HERE, "data", "t*.py"))):
    m = load(path); meta = m.META; n = meta["n"]
    h1 = meta["h1"]
    if getattr(m, "LISTENING", False):
        page = L
        page = resub(page, r"<title>.*?</title>", f"<title>段考題庫｜第{n}回 - {meta['title']}</title>")
        page = resub(page, r"<h1>.*?</h1>", f"<h1>{h1}</h1>")
        page = resub(page, r'<p class="subtitle">.*?</p>', f'<p class="subtitle">{meta["subtitle"]}｜{BOOK}Ａ卷</p>')
        blocks = "".join(f"""  <section class="block">
    <h2>{s['title']}</h2>
    <p class="meta">{s['meta']}</p>
    <audio controls src="audio/test{n}/track{s['track']}.mp3"></audio>
    <div id="sec{k}"></div>
  </section>

""" for k, s in enumerate(m.SECTIONS, 1))
        page = resub(page, r"<main>\n.*?(  <a class=\"footer-link\")", f"<main>\n{blocks}\\1")
        page = page.replace("\\1", '  <a class="footer-link"')
        calls = "\n".join(f"// {s['title']}\nmc(document.getElementById(\"sec{k}\"), {js(s['items'])});\n" for k, s in enumerate(m.SECTIONS, 1))
        page = resub(page, r"\n// 一、選出聽到的字詞.*?</script>", "\n" + calls + "</script>")
        page = resub(page, r"window\.EXAM_META = \{.*?\};", f'window.EXAM_META = {{version:"A卷", examLabel:"第{n}回"}};')
        exams.append(dict(n=n, lesson=meta["subtitle"].split("（")[1].rstrip("）").replace("Unit ", "Unit ") if "（" in meta["subtitle"] else "", title=h1.split("・")[1], type="聽力"))
    else:
        page = W
        page = resub(page, r"<title>.*?</title>", f"<title>段考題庫｜第{n}回 - {h1.split('・')[1]}</title>")
        page = resub(page, r"<h1>.*?</h1>", f"<h1>{h1}</h1>")
        page = resub(page, r'<p class="subtitle">.*?</p>', f'<p class="subtitle">{meta["subtitle"]}｜{BOOK}Ａ卷</p>')
        data = f'window.EXAM_META = {{ version: "A卷", examLabel: "第{n}回" }};\nconst DATA = {{\n  sections: {js(m.SECTIONS)}\n}};\n'
        page = resub(page, r"window\.EXAM_META = \{.*?\n\};\n", data)
        exams.append(dict(n=n, lesson=h1.split("・")[1], title=meta["subtitle"], type="筆試"))
    assert "kangxuan" not in page and "康軒" not in page, f"leftover 康軒 text in test{n}"
    wr(os.path.join(OUTDIR, f"test{n}.html"), page)
    print("wrote", f"test{n}.html")

# ---------- book index (from 康軒 kangxuan-g8-1.html) ----------
I = rd(os.path.join(REPO, "kangxuan-g8-1.html"))
I = sub1(I, "康軒版八年級英語（三）", BOOK, 2)
rows = []
for e in exams:
    n = e["n"]
    if e["type"] == "聽力":
        lesson, title = {4: ("Unit 1～2", "聽力測驗一"), 8: ("Unit 3～4", "聽力測驗二"), 12: ("Unit 5～6", "聽力測驗三")}[n]
    else:
        lesson, title = e["lesson"], e["title"]
    rows.append(f'      {{n:{n}, lesson:{json.dumps(lesson, ensure_ascii=False)}, title:{json.dumps(title, ensure_ascii=False)}, type:"{e["type"]}", href:"hanlin-g8-1/test{n}.html", hrefB:null, hrefC:null}}')
I = resub(I, r"const EXAMS = \[\n.*?\n    \];", "const EXAMS = [\n" + ",\n".join(rows) + "\n    ];")
wr(os.path.join(REPO, "hanlin-g8-1.html"), I)
print("wrote hanlin-g8-1.html")
