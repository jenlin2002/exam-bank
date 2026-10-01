"""Crop question images out of the scanned 翰林 B卷 PDF (boxes in 110-dpi preview pixels)."""
import pymupdf, os
SRC = r"C:\Users\jenlin2002\OneDrive - avc.co\興雅國中\XXY\校用券1到3 年級全出版社\115年\115上國中2年級校卷\115上翰林2上校卷\115上翰林英文2上校卷\115上翰林英文2上B卷_學用.pdf"
OUT = r"E:\GitHub\exam-bank\hanlin-g8-1\images"
doc = pymupdf.open(SRC)
k = 72 / 110

def save(test, name, page, b):
    os.makedirs(os.path.join(OUT, test), exist_ok=True)
    path = os.path.join(OUT, test, name + ".png")
    doc[page-1].get_pixmap(dpi=170, clip=pymupdf.Rect(b[0]*k, b[1]*k, b[2]*k, b[3]*k)).save(path)
    print(path)

def listening(test, page):
    for i in range(7):
        top = 228 + 166*i
        save(test, f"p1_q{i+1}", page, (128, top, 1025, top + 142))

save("test1b", "q5_chart", 2, (130, 1056, 760, 1164))
listening("test4b", 7)
listening("test8b", 15)
save("test9b", "r_map", 18, (818, 408, 1066, 600))
save("test10b", "r_flyer", 20, (718, 1182, 1112, 1268))
save("test11b", "r_map", 22, (604, 430, 930, 614))
listening("test12b", 23)
save("test13b", "q1", 25, (592, 158, 736, 266))
save("test13b", "q36_maps", 26, (128, 998, 1010, 1126))
save("test13b", "q37_flyer", 26, (60, 1148, 472, 1400))
