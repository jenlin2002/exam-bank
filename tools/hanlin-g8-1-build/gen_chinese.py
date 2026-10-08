"""翰林版八年級國文（三）: generate pages + book index (same layout as 社會 hanlin-social-g8-1).
Data: chidata[B|C]/tNN.py with META, SECTIONS and optional CROPS=[(name, pdf_page, "L"|"R", (x0,y0,x1,y1))].
CROPS boxes are pixel coords on a half-page column image rendered at 200 dpi
(L = left half 0..w/2+8pt, R = right half w/2-8pt..w), same as the images used for transcription.
Run from anywhere: python gen_chinese.py  (needs pymupdf only when CROPS are used)."""
import os, re, json, glob, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(REPO, "PDF-RAW-DATA", "Chinese", "hanlin", "hanlin-G8-1", "115上翰林國文2上{}卷_學用.pdf")
OUT = os.path.join(REPO, "hanlin-chinese-g8-1")
BOOK = "翰林版八年級國文（三）"
FULL = {"A": "Ａ", "B": "Ｂ", "C": "Ｃ"}
# 每回的範圍（第 N 回 = PDF 第 2N-1、2N 頁）
ROUNDS = [
    ("第一課", "田園之秋選"), ("第二課", "古詩選"), ("第三課", "下雨天，真好・語文常識（一）"),
    ("第一～三課・語文常識（一）", "複習"), ("第四課", "愛蓮說"), ("第五課", "生命中的碎珠"),
    ("第六課", "鳥・語文常識（二）"), ("第四～六課・語文常識（二）", "複習"), ("第七課", "張釋之執法"),
    ("第八課", "找尋失落的水源"), ("第九課", "一棵開花的樹"), ("第十課", "畫的哀傷"),
    ("第七～十課", "複習"), ("自學選文一", "六朝名士畫廊──世說新語選"), ("自學選文二", "一團人生"),
    ("自學選文三", "安藤忠雄：孤獨，也要讓夢想開花"),
]

def rd(p): return open(p, encoding="utf-8").read()
def wr(p, s):
    with open(p, "w", encoding="utf-8", newline="\n") as f: f.write(s)
def load(path):
    spec = importlib.util.spec_from_file_location("m", path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

T = rd(os.path.join(HERE, "tpl_chinese.html"))
hrefs = {}
for ver, folder, suf in [("A", "chidata", ""), ("B", "chidataB", "b"), ("C", "chidataC", "c")]:
    files = sorted(glob.glob(os.path.join(HERE, folder, "t*.py")))
    if not files: continue
    doc = None
    for path in files:
        m = load(path); n = m.META["n"]; lesson, title = ROUNDS[n-1]
        name = f"test{n}{suf}"
        crops = getattr(m, "CROPS", [])
        if crops:
            import pymupdf
            doc = doc or pymupdf.open(SRC.format(ver))
            os.makedirs(os.path.join(OUT, "images", name), exist_ok=True)
            k = 72 / 200
            for cn, pg, side, b in crops:
                page = doc[pg-1]; w = page.rect.width; off = 0 if side == "L" else w/2 - 8
                clip = pymupdf.Rect(off + b[0]*k, b[1]*k, off + b[2]*k, b[3]*k)
                page.get_pixmap(dpi=170, clip=clip).save(os.path.join(OUT, "images", name, cn + ".png"))
        secs = json.loads(json.dumps(m.SECTIONS, ensure_ascii=False).replace("images/t/", f"images/{name}/"))
        nq = 0
        for s in secs:
            if s["type"] == "reading":
                for p in s["passages"]:
                    for it in p["items"]: assert 0 <= it["correct"] < len(it["options"]), (name, s["title"]); nq += 1
            elif s["type"] == "mc":
                for it in s["items"]: assert 0 <= it["correct"] < len(it["options"]), (name, s["title"], it["q"]); nq += 1
            elif s["type"] == "fill":
                for it in s["items"]: assert it["answers"] and all(it["answers"]), (name, it); nq += 1
            else:
                assert s["type"] == "explain", s["type"]
                for it in s["items"]: assert it["answer"], (name, it)
        p = T.replace("__TITLE__", f"段考題庫｜國文第{n}回 - {title}")
        p = p.replace("__H1__", f"國文・第{n}回")
        p = p.replace("__SUB__", f"{lesson} {title}｜{BOOK}{FULL[ver]}卷")
        data = (f'window.EXAM_META = {{ version: "國文{ver}卷", examLabel: "國文第{n}回" }};\nconst DATA = {{\n  sections: '
                + json.dumps(secs, ensure_ascii=False, indent=2) + "\n};\n")
        p = p.replace("/*__DATA__*/\n", data)
        os.makedirs(OUT, exist_ok=True)
        wr(os.path.join(OUT, name + ".html"), p)
        hrefs.setdefault(n, {})[ver] = f"hanlin-chinese-g8-1/{name}.html"
        print("wrote", name, nq, "graded questions")

def h(n, v): return json.dumps(hrefs.get(n, {}).get(v))
rows = ",\n".join(f'        {{n:{n}, lesson:{json.dumps(l, ensure_ascii=False)}, title:{json.dumps(t, ensure_ascii=False)}, hrefA:{h(n,"A")}, hrefB:{h(n,"B")}, hrefC:{h(n,"C")}}}'
                  for n, (l, t) in enumerate(ROUNDS, 1))
I = rd(os.path.join(REPO, "hanlin-social-g8-1.html"))
I = I.replace("<title>段考題庫｜翰林版八年級社會（三）</title>", f"<title>段考題庫｜{BOOK}</title>")
I = I.replace('href="social.html" style="color:#cfe0d1;">社會科', 'href="chinese.html" style="color:#cfe0d1;">國文科')
I = re.sub(r'<p class="sub">.*?</p>', f'<p class="sub">{BOOK}平時考練習：每一課一回，另有複習回與自學選文，題目會陸續增加</p>', I, count=1)
I = re.sub(r"const SECTIONS = \[.*?\n    \];", lambda _: 'const SECTIONS = [\n      {icon:"📖", subject:"國文", folder:"chi", rounds:[\n' + rows + "\n      ]}\n    ];", I, count=1, flags=re.S)
I = I.replace('href="social.html">← 回社會科總目錄', 'href="chinese.html">← 回國文科總目錄')
assert "social" not in I and "社會" not in I, "index still mentions 社會"
wr(os.path.join(REPO, "hanlin-chinese-g8-1.html"), I)
print("wrote hanlin-chinese-g8-1.html")
