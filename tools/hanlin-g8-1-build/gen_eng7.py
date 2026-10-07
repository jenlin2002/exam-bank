"""翰林版七年級英語（一）: crop figures, copy audio, generate pages + index.
Data: eng7data[B|C]/tNN.py (META, SECTIONS, CROPS). Listening rounds have LISTENING=True.
Templates/helpers come from gen.py (same as 翰林二上英語)."""
import os, re, json, glob, sys, zipfile
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, "gen.py"), encoding="utf-8").read().split("\nexams = []\n")[0])  # W, L, helpers

BOOK7 = "翰林版七年級英語（一）"
SLUG = "hanlin-g7-1"
OUT7 = os.path.join(REPO, SLUG)
SRC = r"C:\Users\jenlin2002\OneDrive - avc.co\興雅國中\XXY\校用券1到3 年級全出版社\115年\115上國中1年級校卷\115上翰林1上校卷\115上翰林英文1上校卷\115上翰林英文1上{}卷_{}"
FULL = {"A": "Ａ", "B": "Ｂ", "C": "Ｃ"}
LISTEN = {5: ("Starter～Unit 2", "聽力測驗一", [1, 2, 3]), 9: ("Unit 3～4", "聽力測驗二", [4, 5, 6]), 13: ("Unit 5～6", "聽力測驗三", [7, 8, 9])}
k = 72 / 110

W7 = W.replace("../hanlin-g8-1.html", f"../{SLUG}.html")
# case-sensitive blanks (e.g. 大小寫轉換)
W7 = sub1(W7, '<input type="text" class="blank" data-answer="${it.answer}" placeholder="填入單字">',
              '<input type="text" class="blank" data-answer="${it.answer}" ${it.exact ? \'data-exact="1"\' : ""} placeholder="填入答案">')
W7 = sub1(W7, "  const val = input.value.trim().toLowerCase();\n  const ans = input.dataset.answer.trim().toLowerCase();",
              "  const ex = input.dataset.exact === \"1\";\n  const val = ex ? input.value.trim().replace(/\\s+/g,\"\") : input.value.trim().toLowerCase();\n  const ans = ex ? input.dataset.answer.trim() : input.dataset.answer.trim().toLowerCase();")
# picture for guided-multi items (看圖填空)
W7 = sub1(W7, '${it.zh ? it.zh+"<br>" : ""}${linesHtml}</div>',
              '${it.zh ? it.zh+"<br>" : ""}${it.image ? `<img src="${it.image}" alt="題目附圖" style="width:100%;max-width:220px;display:block;border-radius:8px;margin:4px 0 8px;border:1px solid var(--paper-line);">` : ""}${linesHtml}</div>')
L7 = L.replace("../hanlin-g8-1.html", f"../{SLUG}.html")

do_crop = "--nocrop" not in sys.argv
exams = {}
for ver, folder, suf in [("A", "eng7data", ""), ("B", "eng7dataB", "b"), ("C", "eng7dataC", "c")]:
    files = sorted(glob.glob(os.path.join(HERE, folder, "t*.py")))
    if not files: continue
    doc = pymupdf.open(SRC.format(ver, "學用.pdf")) if do_crop else None
    for path in files:
        m = load(path); meta = m.META; n = meta["n"]; name = f"test{n}{suf}"
        if doc:
            os.makedirs(os.path.join(OUT7, "images", name), exist_ok=True)
            for cn, pg, b in getattr(m, "CROPS", []):
                doc[pg-1].get_pixmap(dpi=170, clip=pymupdf.Rect(b[0]*k, b[1]*k, b[2]*k, b[3]*k)).save(os.path.join(OUT7, "images", name, cn + ".png"))
        secs = json.loads(json.dumps(m.SECTIONS).replace(f"images/test{n}/", f"images/{name}/"))
        tag = f"{BOOK7}{FULL[ver]}卷"
        if getattr(m, "LISTENING", False):
            lesson, title, tracks = LISTEN[n]
            if do_crop:
                os.makedirs(os.path.join(OUT7, "audio", name), exist_ok=True)
                with zipfile.ZipFile(SRC.format(ver, "聽力檔.zip")) as z:
                    for e in z.infolist():
                        t = int(e.filename[:2])
                        if t in tracks:
                            with open(os.path.join(OUT7, "audio", name, f"track{tracks.index(t)+1}.mp3"), "wb") as f:
                                f.write(z.read(e))
            p = L7
            p = resub(p, r"<title>.*?</title>", f"<title>段考題庫｜第{n}回 - {meta['title']}</title>")
            p = resub(p, r"<h1>.*?</h1>", f"<h1>{meta['h1']}</h1>")
            p = resub(p, r'<p class="subtitle">.*?</p>', f'<p class="subtitle">{meta["subtitle"]}｜{tag}</p>')
            blocks = "".join(f"""  <section class="block">
    <h2>{s['title']}</h2>
    <p class="meta">{s['meta']}</p>
    <audio controls src="audio/{name}/track{s['track']}.mp3"></audio>
    <div id="sec{i}"></div>
  </section>

""" for i, s in enumerate(secs, 1))
            p = resub(p, r"<main>\n.*?  <a class=\"footer-link\"", f"<main>\n{blocks}  <a class=\"footer-link\"")
            calls = "\n".join(f"// {s['title']}\nmc(document.getElementById(\"sec{i}\"), {js(s['items'])});\n" for i, s in enumerate(secs, 1))
            p = resub(p, r"\n// 一、選出聽到的字詞.*?</script>", "\n" + calls + "</script>")
            p = resub(p, r"window\.EXAM_META = \{.*?\};", f'window.EXAM_META = {{version:"{ver}卷", examLabel:"一上第{n}回"}};')
            kind = "聽力"
        else:
            p = W7
            p = resub(p, r"<title>.*?</title>", f"<title>段考題庫｜第{n}回 - {meta['h1'].split('・')[1]}</title>")
            p = resub(p, r"<h1>.*?</h1>", f"<h1>{meta['h1']}</h1>")
            p = resub(p, r'<p class="subtitle">.*?</p>', f'<p class="subtitle">{meta["subtitle"]}｜{tag}</p>')
            data = f'window.EXAM_META = {{ version: "{ver}卷", examLabel: "一上第{n}回" }};\nconst DATA = {{\n  sections: {js(secs)}\n}};\n'
            p = resub(p, r"window\.EXAM_META = \{.*?\n\};\n", data)
            lesson, title, kind = meta["h1"].split("・")[1], meta["subtitle"], "筆試"
        assert "kangxuan" not in p and "康軒" not in p and "八年級" not in p, name
        os.makedirs(OUT7, exist_ok=True)
        wr(os.path.join(OUT7, name + ".html"), p)
        exams.setdefault(n, dict(lesson=lesson, title=title, type=kind, hrefs={}))["hrefs"][ver] = f"{SLUG}/{name}.html"
        print("wrote", name)

I = rd(os.path.join(REPO, "hanlin-g8-1.html"))
I = sub1(I, "翰林版八年級英語（三）", BOOK7, 2)
def h(e, v): return json.dumps(e["hrefs"][v]) if v in e["hrefs"] else "null"
rows = [f'      {{n:{n}, lesson:{json.dumps(e["lesson"], ensure_ascii=False)}, title:{json.dumps(e["title"], ensure_ascii=False)}, type:"{e["type"]}", href:{h(e,"A")}, hrefB:{h(e,"B")}, hrefC:{h(e,"C")}}}'
        for n, e in sorted(exams.items())]
I = resub(I, r"const EXAMS = \[\n.*?\n    \];", "const EXAMS = [\n" + ",\n".join(rows) + "\n    ];")
wr(os.path.join(REPO, f"{SLUG}.html"), I)
print(f"wrote {SLUG}.html")

E = rd(os.path.join(REPO, "english.html"))
old = '{grade:"國中一上", items:[\n        {pub:"康軒", href:"kangxuan-g7-1.html"},\n        {pub:"翰林", href:null},'
if old in E:
    E = E.replace(old, old.replace('{pub:"翰林", href:null}', f'{{pub:"翰林", href:"{SLUG}.html"}}'))
    wr(os.path.join(REPO, "english.html"), E); print("english.html: 國中一上・翰林 enabled")
