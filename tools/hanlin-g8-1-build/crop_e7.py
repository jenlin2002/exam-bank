"""Crop figures for 翰林七上英語 out of the scanned 學用 PDFs, and extract the listening audio.
Each e7data*/tNN.py lists CROPS = [(name, page, (x0,y0,x1,y1))]; boxes are pixels of the 2x page render
(1514x2183 for one page), i.e. what you see when you view a page rendered with Matrix(2,2).
Cropping is done from a 3x render for sharper images.
Run:  python crop_e7.py            (images)
      python crop_e7.py --audio    (mp3 from the 聽力檔 zips: round 5/9/13 = TRACK 1-3/4-6/7-9)"""
import os, sys, glob, io, zipfile, importlib.util
import pymupdf
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
RAWDIR = os.path.join(REPO, "PDF-RAW-DATA", "english", "hanlin", "hanlin-g7-1")
OUT = os.path.join(REPO, "hanlin-g7-1")
VERSIONS = [("A", "e7data", ""), ("B", "e7dataB", "b"), ("C", "e7dataC", "c")]
LISTEN_ROUNDS = {5: 0, 9: 3, 13: 6}   # round -> index of its first track in the zip

def load(path):
    spec = importlib.util.spec_from_file_location("m", path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def crops():
    for ver, folder, suf in VERSIONS:
        files = sorted(glob.glob(os.path.join(HERE, folder, "t*.py")))
        if not files: continue
        doc = pymupdf.open(os.path.join(RAWDIR, f"115上翰林英文1上{ver}卷_學用.pdf"))
        cache, count = {}, 0
        for path in files:
            m = load(path); n = m.META["n"]
            for name, page, box in getattr(m, "CROPS", []):
                if page not in cache:
                    pix = doc[page-1].get_pixmap(matrix=pymupdf.Matrix(3, 3))
                    cache[page] = Image.open(io.BytesIO(pix.tobytes("png")))
                d = os.path.join(OUT, "images", f"test{n}{suf}"); os.makedirs(d, exist_ok=True)
                cache[page].crop(tuple(int(v * 1.5) for v in box)).save(os.path.join(d, name + ".png")); count += 1
        print(ver, "cropped", count)

def audio():
    for ver, _, suf in VERSIONS:
        z = zipfile.ZipFile(os.path.join(RAWDIR, f"115上翰林英文1上{ver}卷_聽力檔.zip"))
        names = sorted(z.namelist())
        for n, first in LISTEN_ROUNDS.items():
            d = os.path.join(OUT, "audio", f"test{n}{suf}"); os.makedirs(d, exist_ok=True)
            for k in range(3):
                with open(os.path.join(d, f"track{k+1}.mp3"), "wb") as f: f.write(z.read(names[first + k]))
            print(ver, "round", n, "audio ok")

if __name__ == "__main__":
    audio() if "--audio" in sys.argv else crops()
