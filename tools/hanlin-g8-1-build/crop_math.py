"""Crop figures out of the scanned 翰林數學 PDFs. Each mathdata*/tNN.py lists CROPS = [(name, page, box)],
boxes in 110-dpi preview pixels. Rounds 1–2 (written before CROPS existed) are listed here."""
import pymupdf, os, glob, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = r"E:\GitHub\exam-bank\PDF-RAW-DATA\MATH\hanlin\hanlin-g8-1\115上翰林數學2上{}卷_學用.pdf"
OUT = r"E:\GitHub\exam-bank\hanlin-math-g8-1\images"
k = 72 / 110

EARLY = {
  "test1": [("q8",1,(452,1312,558,1408)), ("q9_board",1,(652,422,1044,560)), ("f4",1,(948,1202,1102,1348)),
            ("c1",2,(376,86,558,288)), ("c2",2,(412,856,558,1004)), ("b1",2,(962,836,1106,982))],
  "test2": [("q9_board",3,(676,603,1030,745)), ("f3",3,(948,1452,1104,1522)), ("f4",4,(402,60,560,154)),
            ("c2",4,(380,936,560,1072)), ("b1",4,(928,630,1108,752)), ("b4",4,(912,1184,1108,1268))],
}

def crop(doc, folder, name, page, b):
    os.makedirs(os.path.join(OUT, folder), exist_ok=True)
    doc[page-1].get_pixmap(dpi=200, clip=pymupdf.Rect(b[0]*k, b[1]*k, b[2]*k, b[3]*k)).save(os.path.join(OUT, folder, name + ".png"))

for ver, src_folder, suf in [("A","mathdata",""), ("B","mathdataB","b"), ("C","mathdataC","c")]:
    files = sorted(glob.glob(os.path.join(HERE, src_folder, "t*.py")))
    if not files: continue
    doc = pymupdf.open(RAW.format(ver))
    count = 0
    for path in files:
        spec = importlib.util.spec_from_file_location("m", path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        folder = f"test{m.META['n']}{suf}"
        for name, page, box in getattr(m, "CROPS", None) or EARLY.get(folder, []):
            crop(doc, folder, name, page, box); count += 1
    print(ver, "cropped", count)
