"""翰林版八年級社會（三）: crop figures + generate pages + book index.
Data: socdata[B|C]/{geo,hist,civ}N.py with META, SECTIONS, CROPS=[(name, pdf_page, box@110dpi)].
Template: the 翰林七上社會 pages made on the home PC (hanlin-social-g7-1/)."""
import os, re, json, glob, importlib.util, sys
import pymupdf

REPO = r"E:\GitHub\exam-bank"
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = r"C:\Users\jenlin2002\OneDrive - avc.co\興雅國中\XXY\校用券1到3 年級全出版社\115年\115上國中2年級校卷\115上翰林2上校卷\115上翰林社會2上校卷\115上翰林社會2上{}卷_學用.pdf"
OUT = os.path.join(REPO, "hanlin-social-g8-1")
BOOK = "翰林版八年級社會（三）"
SUBJ = {"geo": "地理", "hist": "歷史", "civ": "公民"}
FULL = {"A": "Ａ", "B": "Ｂ", "C": "Ｃ"}
k = 72 / 110

def rd(p): return open(p, encoding="utf-8").read()
def wr(p, s):
    with open(p, "w", encoding="utf-8", newline="\n") as f: f.write(s)
def resub(s, pat, new):
    s2, n = re.subn(pat, lambda m: new, s, count=1, flags=re.S); assert n == 1, pat; return s2
def load(path):
    spec = importlib.util.spec_from_file_location("m", path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

T = rd(os.path.join(REPO, "hanlin-social-g7-1", "geo1.html"))
T = T.replace("../hanlin-social-g7-1.html", "../hanlin-social-g8-1.html")
assert "hanlin-social-g7-1" not in T

do_crop = "--nocrop" not in sys.argv
rows = {}
for ver, folder, suf in [("A", "socdata", ""), ("B", "socdataB", "b"), ("C", "socdataC", "c")]:
    files = sorted(glob.glob(os.path.join(HERE, folder, "*.py")))
    if not files: continue
    doc = pymupdf.open(SRC.format(ver)) if do_crop else None
    for path in files:
        m = load(path); meta = m.META; s, n = meta["subj"], meta["n"]
        name = f"{s}{n}{suf}"
        if doc:
            os.makedirs(os.path.join(OUT, "images", name), exist_ok=True)
            for cn, pg, b in m.CROPS:
                doc[pg-1].get_pixmap(dpi=170, clip=pymupdf.Rect(b[0]*k, b[1]*k, b[2]*k, b[3]*k)).save(os.path.join(OUT, "images", name, cn + ".png"))
        secs = json.loads(json.dumps(m.SECTIONS).replace(f"images/{s}{n}/", f"images/{name}/"))
        p = T
        p = resub(p, r"<title>.*?</title>", f"<title>段考題庫｜{SUBJ[s]}第{n}回 - {meta['title']}</title>")
        p = resub(p, r"<h1>.*?</h1>", f"<h1>{SUBJ[s]}・第{n}回</h1>")
        p = resub(p, r'<p class="subtitle">.*?</p>', f'<p class="subtitle">{meta["lesson"]} {meta["title"]}｜{BOOK}{FULL[ver]}卷</p>')
        data = (f'window.EXAM_META = {{ version: "{ver}卷", examLabel: "{SUBJ[s]}第{n}回" }};\nconst DATA = {{\n  sections: '
                + json.dumps(secs, ensure_ascii=False, indent=2) + "\n};\n")
        p = resub(p, r"window\.EXAM_META = \{.*?\n\};\n", data)
        assert "七年級" not in p
        wr(os.path.join(OUT, name + ".html"), p)
        rows.setdefault(s, {}).setdefault(n, dict(lesson=meta["lesson"], title=meta["title"], hrefs={}))["hrefs"][ver] = f"hanlin-social-g8-1/{name}.html"
        print("wrote", name)

# book index from the 七上 index; rounds without pages keep the titles listed here
TITLES = {
  "geo": ["中國的地形","中國的氣候","第1～2章 總複習","中國的人口與文化","中國的產業","第3～4章 總複習","中國的區域發展","中國與世界的連結","第5～6章 總複習"],
  "hist": [""]*9, "civ": [""]*9,
}
I = rd(os.path.join(REPO, "hanlin-social-g7-1.html"))
I = I.replace("翰林版七年級社會（一）", BOOK)
def h(e, v): return json.dumps(e["hrefs"][v]) if e and v in e["hrefs"] else "null"
for s in ("geo", "hist", "civ"):
    lines = []
    for n in range(1, 10):
        e = rows.get(s, {}).get(n)
        lesson = e["lesson"] if e else ""
        title = e["title"] if e else TITLES[s][n-1]
        lines.append(f'        {{n:{n}, lesson:{json.dumps(lesson, ensure_ascii=False)}, title:{json.dumps(title, ensure_ascii=False)}, hrefA:{h(e,"A")}, hrefB:{h(e,"B")}, hrefC:{h(e,"C")}}}')
    I = resub(I, r'(folder:"' + s + r'", rounds:\[\n).*?(\n\s*\]\})', lambda_ := None) if False else I
    I = re.sub(r'(folder:"' + s + r'", rounds:\[\n).*?(\n\s*\]\})', lambda mm: mm.group(1) + ",\n".join(lines) + mm.group(2), I, count=1, flags=re.S)
assert "hanlin-social-g7-1/" not in I, "index still points at 七上 pages"
wr(os.path.join(REPO, "hanlin-social-g8-1.html"), I)
print("wrote hanlin-social-g8-1.html")
