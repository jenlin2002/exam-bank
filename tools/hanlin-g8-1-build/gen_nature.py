"""翰林版自然科（七上＝自然(一)、八上＝自然(三)）: 裁附圖 + 產生測驗頁 + 該冊目錄頁。版型和國文／社會頁相同。
Data: nat7data[B|C]/tNN.py（一上）、natdata[B|C]/tNN.py（二上），內容見 nat_lib.py 的說明；答案在同資料夾的 answers.py（ANS）。
CROPS = [(名稱, PDF頁碼, "LT"|"LB"|"RT"|"RB", (x0,y0,x1,y1))]，座標是 nat_view.py 輸出的視圖上的像素（150 dpi），可超出視圖範圍。
用法（任何電腦都能跑，路徑是相對的；有 CROPS 的回才需要 pymupdf）：
    python gen_nature.py          # 二上（翰林版八年級自然（三））
    python gen_nature.py --g7     # 一上（翰林版七年級自然（一））"""
import os, re, sys, json, glob, importlib.util
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
G7 = "--g7" in sys.argv
import nat_lib
from nat_view import pdf_path, crop_rect

if G7:
    GRADE, SLUG, BOOK, DATA = "g7", "hanlin-nature-g7-1", "翰林版七年級自然（一）", "nat7data"
    ROUNDS = [  # (範圍, 主題)  第 N 回 = PDF 第 2N-1、2N 頁
        ("1-1～1-3", "生命現象、科學方法與顯微鏡"), ("2-1～2-2", "細胞的構造與功能"), ("2-3～2-4", "細胞的物質進出與生物體的組成（含尺度）"),
        ("第1～2章", "複習"), ("3-1～3-2", "養分與酵素"), ("3-3～3-4", "光合作用與呼吸作用"),
        ("4-1～4-2", "植物與動物體內的物質運輸"), ("4-3～4-4", "人體的循環與呼吸"), ("第3～4章", "複習"),
        ("5-1～5-2", "動物的協調作用（神經）"), ("5-3～5-4", "內分泌與植物的感應"), ("6-1", "恆定與運動"),
        ("6-2～6-3", "生物的恆定（水分調節）"), ("第5～6章", "複習"),
    ]
else:
    GRADE, SLUG, BOOK, DATA = "g8", "hanlin-nature-g8-1", "翰林版八年級自然（三）", "natdata"
    ROUNDS = [
        ("實驗室常用器材・1-1～1-3", "實驗器材、測量與基本操作"), ("2-1", "氧氣與燃燒"), ("2-2～2-3", "二氧化碳與氧化還原"),
        ("第1～2章", "複習"), ("3-1～3-2", "水溶液與溶解"), ("3-3～3-4", "聲音的產生與傳播、音調響度"),
        ("4-1～4-3", "光的傳播與反射"), ("4-4～4-5", "折射與透鏡成像"), ("第3～4章", "複習"),
        ("5-1～5-2", "溫度與熱"), ("5-3～5-5", "熱的傳播與比熱"), ("6-1～6-2", "物質的組成與元素"),
        ("6-3～6-5", "週期表與原子結構"), ("第5～6章", "複習"),
    ]
OUT = os.path.join(REPO, SLUG)
FULL = {"A": "Ａ", "B": "Ｂ", "C": "Ｃ"}


def rd(p): return open(p, encoding="utf-8").read()
def wr(p, s):
    with open(p, "w", encoding="utf-8", newline="\n") as f: f.write(s)
def load(path):
    spec = importlib.util.spec_from_file_location("m", path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


T = rd(os.path.join(HERE, "tpl_nature.html")).replace("hanlin-chinese-g8-1.html", SLUG + ".html")
hrefs = {}
for ver, folder, suf in [("A", DATA, ""), ("B", DATA + "B", "b"), ("C", DATA + "C", "c")]:
    dpath = os.path.join(HERE, folder)
    files = sorted(glob.glob(os.path.join(dpath, "t*.py")))
    if not files: continue
    nat_lib.ANS = load(os.path.join(dpath, "answers.py")).ANS
    doc = None
    for path in files:
        m = load(path); n = m.META["n"]; lesson, title = ROUNDS[n-1]
        name = f"test{n}{suf}"
        crops = getattr(m, "CROPS", [])
        if crops:
            import pymupdf
            doc = doc or pymupdf.open(pdf_path(GRADE, ver))
            os.makedirs(os.path.join(OUT, "images", name), exist_ok=True)
            for old in glob.glob(os.path.join(OUT, "images", name, "*.png")):   # 刪掉改名或不用的舊圖
                if os.path.splitext(os.path.basename(old))[0] not in {c[0] for c in crops}: os.remove(old)
            for cn, pg, view, b in crops:
                page = doc[pg-1]
                page.get_pixmap(dpi=170, clip=crop_rect(page.rect, view, b)).save(os.path.join(OUT, "images", name, cn + ".png"))
        secs = json.loads(json.dumps(m.SECTIONS, ensure_ascii=False).replace("images/t/", f"images/{name}/"))
        used = set(re.findall(r"images/" + name + r"/([A-Za-z0-9_]+)\.png", json.dumps(secs)))
        have = {c[0] for c in crops}
        assert used <= have, (name, "沒有裁切的圖", sorted(used - have))
        nq = 0
        for s in secs:
            for p in s["passages"]:
                for it in p["items"]:
                    assert 0 <= it["correct"] < len(it["options"]), (name, s["title"], it["q"]); nq += 1
        pg = T.replace("__TITLE__", f"段考題庫｜自然第{n}回 - {title}")
        pg = pg.replace("__H1__", f"自然・第{n}回")
        pg = pg.replace("__SUB__", f"{lesson} {title}｜{BOOK}{FULL[ver]}卷")
        data = (f'window.EXAM_META = {{ version: "自然{ver}卷", examLabel: "自然第{n}回" }};\nconst DATA = {{\n  sections: '
                + json.dumps(secs, ensure_ascii=False, indent=2) + "\n};\n")
        pg = pg.replace("/*__DATA__*/\n", data)
        os.makedirs(OUT, exist_ok=True)
        wr(os.path.join(OUT, name + ".html"), pg)
        hrefs.setdefault(n, {})[ver] = f"{SLUG}/{name}.html"
        print("wrote", name, nq, "graded questions")

def h(n, v): return json.dumps(hrefs.get(n, {}).get(v))
rows = ",\n".join(f'        {{n:{n}, lesson:{json.dumps(l, ensure_ascii=False)}, title:{json.dumps(t, ensure_ascii=False)}, hrefA:{h(n,"A")}, hrefB:{h(n,"B")}, hrefC:{h(n,"C")}}}'
                  for n, (l, t) in enumerate(ROUNDS, 1))
I = rd(os.path.join(REPO, "hanlin-social-g8-1.html"))
I = I.replace("<title>段考題庫｜翰林版八年級社會（三）</title>", f"<title>段考題庫｜{BOOK}</title>")
I = I.replace('href="social.html" style="color:#cfe0d1;">社會科', 'href="nature.html" style="color:#cfe0d1;">自然科')
I = re.sub(r'<p class="sub">.*?</p>', f'<p class="sub">{BOOK}平時考練習：每回對應一～二節課，題目全部是選擇題</p>', I, count=1)
I = re.sub(r"const SECTIONS = \[.*?\n    \];", lambda _: 'const SECTIONS = [\n      {icon:"🔬", subject:"自然", folder:"nat", rounds:[\n' + rows + "\n      ]}\n    ];", I, count=1, flags=re.S)
I = I.replace('href="social.html">← 回社會科總目錄', 'href="nature.html">← 回自然科總目錄')
assert "social" not in I and "社會" not in I, "index still mentions 社會"
wr(os.path.join(REPO, SLUG + ".html"), I)
print("wrote", SLUG + ".html")
