"""Write all 翰林 A/B/C pages + the book index. Templates/helpers come from gen.py (run up to its page loop)."""
import os, re, json, glob
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gen.py"), encoding="utf-8").read()
exec(src.split("\nexams = []\n")[0])   # templates W, L and helpers

FULL = {"A": "Ａ", "B": "Ｂ", "C": "Ｃ"}
VERSIONS = [("A", "data", ""), ("B", "dataB", "b"), ("C", "dataC", "c")]
LISTEN_INDEX = {4: ("Unit 1～2", "聽力測驗一"), 8: ("Unit 3～4", "聽力測驗二"), 12: ("Unit 5～6", "聽力測驗三")}
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
            lesson, title, kind = h1.split("・")[1], meta["subtitle"], "筆試"
        assert "kangxuan" not in page and "康軒" not in page, f"leftover 康軒 text in test{n}{suf}"
        name = f"test{n}{suf}.html"
        wr(os.path.join(OUTDIR, name), page)
        exams.setdefault(n, dict(lesson=lesson, title=title, type=kind, hrefs={}))["hrefs"][ver] = f"hanlin-g8-1/{name}"
        print("wrote", name)

I = rd(os.path.join(REPO, "kangxuan-g8-1.html"))
I = sub1(I, "康軒版八年級英語（三）", BOOK, 2)
def h(e, v): return json.dumps(e["hrefs"][v]) if v in e["hrefs"] else "null"
rows = [f'      {{n:{n}, lesson:{json.dumps(e["lesson"], ensure_ascii=False)}, title:{json.dumps(e["title"], ensure_ascii=False)}, type:"{e["type"]}", href:{h(e,"A")}, hrefB:{h(e,"B")}, hrefC:{h(e,"C")}}}'
        for n, e in sorted(exams.items())]
I = resub(I, r"const EXAMS = \[\n.*?\n    \];", "const EXAMS = [\n" + ",\n".join(rows) + "\n    ];")
wr(os.path.join(REPO, "hanlin-g8-1.html"), I)
print("wrote hanlin-g8-1.html")
