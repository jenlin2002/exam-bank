"""自然科 PDF 逐題轉打字用的「看圖」工具。

把 學用 PDF 的某一頁切成 4 張圖（左欄上／下、右欄上／下；上下各多留一段重疊），存到指定資料夾，方便逐題閱讀。
圖上的像素座標（150 dpi）可以直接寫進 CROPS，gen_nature.py 會換算回 PDF 座標去裁附圖：
    CROPS = [(名稱, PDF 頁碼(1 起算), "LT"|"LB"|"RT"|"RB", (x0, y0, x1, y1))]
座標是「那張視圖左上角」起算的像素；超出視圖範圍（負數或超過圖高）也可以，用來裁跨過上下接縫的圖。

用法：python nat_view.py <g7|g8> <A|B|C> <PDF頁碼> <輸出資料夾>
      python nat_view.py <g7|g8> <A|B|C> ans <輸出資料夾>      （簡答頁：每頁左右兩欄各切上下，共 8 張）
"""
import os, sys
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
DPI = 150
OVERLAP = 60   # pt，上下視圖重疊


def pdf_path(grade, ver, kind="學用"):
    if grade == "g7":
        return os.path.join(REPO, "PDF-RAW-DATA", "Nature", "hanlin", "hanlin-G7-1", f"115上翰林自然1上{ver}卷_{kind}.pdf")
    return os.path.join(REPO, "PDF-RAW-DATA", "Nature", "hanlin", "hanlin-G8-1", f"115上翰林自然2上{ver}卷_{kind}.pdf")


def view_rect(page_rect, view):
    """view = "LT" | "LB" | "RT" | "RB"。回傳 PDF 座標的 Rect（pt）。"""
    w, h = page_rect.width, page_rect.height
    x0, x1 = (0, w / 2 + 6) if view[0] == "L" else (w / 2 - 6, w)
    y0, y1 = (0, h / 2 + OVERLAP) if view[1] == "T" else (h / 2 - OVERLAP, h)
    return pymupdf.Rect(x0, y0, x1, y1)


def crop_rect(page_rect, view, box):
    """把視圖像素座標 box 換成 PDF 座標 Rect。"""
    r = view_rect(page_rect, view)
    k = 72 / DPI
    return pymupdf.Rect(r.x0 + box[0] * k, r.y0 + box[1] * k, r.x0 + box[2] * k, r.y0 + box[3] * k)


def draw_grid(png_path):
    """在圖上畫淡藍色的座標格線（每 100 像素一條，邊上標數字），讀圖時可以直接讀出 CROPS 要用的座標。"""
    from PIL import Image, ImageDraw
    im = Image.open(png_path).convert("RGB")
    d = ImageDraw.Draw(im, "RGBA")
    for x in range(100, im.width, 100):
        d.line([(x, 0), (x, im.height)], fill=(0, 140, 255, 70), width=1)
        d.text((x + 2, 2), str(x), fill=(0, 90, 220, 255))
        d.text((x + 2, im.height - 12), str(x), fill=(0, 90, 220, 255))
    for y in range(100, im.height, 100):
        d.line([(0, y), (im.width, y)], fill=(0, 140, 255, 70), width=1)
        d.text((2, y + 2), str(y), fill=(0, 90, 220, 255))
        d.text((im.width - 28, y + 2), str(y), fill=(0, 90, 220, 255))
    im.save(png_path)


def render_views(doc, page_no, out, prefix, grid=True):
    page = doc[page_no - 1]
    os.makedirs(out, exist_ok=True)
    paths = []
    for v in ("LT", "LB", "RT", "RB"):
        p = os.path.join(out, f"{prefix}_{v}.png")
        page.get_pixmap(dpi=DPI, clip=view_rect(page.rect, v)).save(p)
        if grid and "ans" not in prefix: draw_grid(p)
        paths.append(p)
    return paths


if __name__ == "__main__":
    grade, ver, which, out = sys.argv[1:5]
    if which == "ans":
        doc = pymupdf.open(pdf_path(grade, ver, "簡答"))
        for i in range(len(doc)):
            print(*render_views(doc, i + 1, out, f"{grade}{ver}_ans{i + 1}"), sep="\n")
    else:
        doc = pymupdf.open(pdf_path(grade, ver))
        n = int(which)
        print(*render_views(doc, n, out, f"{grade}{ver}_p{n:02d}"), sep="\n")
