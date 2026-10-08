"""自然科資料檔共用的小工具：把「題目＋選項」和簡答頁抄下來的答案（ANS，由 gen_nature.py 在載入資料檔前塞進來）組成 SECTIONS。

資料檔（nat7data/tNN.py、natdata/tNN.py）的寫法：
    from nat_lib import *
    META = dict(n=1)
    CROPS = [("q3", 1, "LT", (30, 400, 700, 800)), ...]       # 名稱、PDF 頁碼、視圖、視圖像素座標（見 nat_view.py）
    SECTIONS = exam(1,
        A1=[ Q("題目", ["選項A","選項B","選項C","選項D"], img="q3"), ... ],         # 一、選擇題
        A2=[ Q(...), G("題組共用的文字", [Q(...), Q(...)], img="g1"), ... ],        # 二、素養題（可含題組）
        B =[ ... ])                                                                  # B 部分 活用題
答案不用寫在題目裡：依序（題組也算）對應簡答頁的答案。
"""
ANS = {}   # {回: (A一答案字串, A二答案字串, B答案字串)}，由 gen_nature.py 設定
I = "images/t/"   # gen_nature.py 會把 images/t/ 換成 images/testN[b|c]/


def Q(q, options, img=None, img2=None, fix=None):
    """fix="C"：簡答頁的答案明顯有誤時，強制用這個字母（要在資料檔該題旁邊寫註解說明原因，並記在 CLAUDE.md）。"""
    d = dict(q=q, options=list(options))
    if fix: d["_fix"] = fix
    if img: d["image"] = I + img + ".png"
    if img2: d["image2"] = I + img2 + ".png"
    return d


def G(text, items, img=None, label=None):
    return dict(_group=True, text=text, items=items, image=(I + img + ".png") if img else None, label=label)


def tbl(rows, head=True):
    """題目裡的小表格（HTML）。rows 是二維串列，head=True 時第一列當表頭。"""
    td = 'style="border:1px solid #888;padding:3px 10px;text-align:center"'
    out = ['<table style="border-collapse:collapse;margin:8px 0;font-size:.95em">']
    for i, r in enumerate(rows):
        tag = "th" if (head and i == 0) else "td"
        out.append("<tr>" + "".join(f"<{tag} {td}>{c}</{tag}>" for c in r) + "</tr>")
    out.append("</table>")
    return "".join(out)


def _part(title, meta, entries, answers, note=None):
    flat = []
    for e in entries:
        flat.extend(e["items"] if e.get("_group") else [e])
    assert len(flat) == len(answers), f"{title}：題目 {len(flat)} 題，但簡答有 {len(answers)} 個答案"
    k = 0
    for it in flat:
        key = it.pop("_fix", None) or answers[k]; k += 1
        c = "ABCD".index(key)
        assert c < len(it["options"]), (title, k, key, len(it["options"]))
        it["correct"] = c
        it["no"] = k
    passages, run = [], []
    def flush():
        nonlocal run
        if run:
            passages.append(dict(text="", items=run)); run = []
    for e in entries:
        if e.get("_group"):
            flush()
            p = dict(text=e["text"], items=e["items"])
            if e.get("image"): p["image"] = e["image"]
            if e.get("label"): p["label"] = e["label"]
            passages.append(p)
        else:
            run.append(e)
    flush()
    sec = dict(type="reading", title=title, meta=meta, passages=passages)
    if note: sec["note"] = note
    return sec


def exam(n, A1, A2, B, m1="每題3分，共54分", m2="每題4分，共28分", mb="每題2分，共18分", t1="A部分 基礎題　一、選擇題", t2="二、素養題", tb="B部分 活用題"):
    a1, a2, b = ANS[n]
    return [_part(t1, m1, A1, a1), _part(t2, m2, A2, a2), _part(tb, mb, B, b)]
