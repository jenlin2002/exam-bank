"""Crop question images out of the scanned 翰林 C卷 PDF (boxes in 110-dpi preview pixels)."""
import pymupdf, os
SRC = r"C:\Users\jenlin2002\OneDrive - avc.co\興雅國中\XXY\校用券1到3 年級全出版社\115年\115上國中2年級校卷\115上翰林2上校卷\115上翰林英文2上校卷\115上翰林英文2上C卷_學用.pdf"
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
        top = 232 + 192*i
        save(test, f"p1_q{i+1}", page, (128, top, 1032, top + 150))

save("test1c", "q7_weather", 2, (100, 896, 1040, 1022))
save("test1c", "q8_clothes", 2, (128, 1470, 1092, 1602))
listening("test4c", 7)
save("test5c", "sec2_clocks", 9, (70, 533, 1050, 667))
save("test5c", "sec4_mia", 9, (56, 1328, 528, 1594))
save("test6c", "sec4_pics", 11, (100, 1303, 1012, 1434))
save("test6c", "r_pie", 12, (80, 1174, 602, 1545))
listening("test8c", 15)
save("test9c", "sec3_map", 17, (56, 1193, 640, 1462))
save("test9c", "r_map", 18, (108, 1310, 492, 1572))
save("test10c", "r_ad", 20, (62, 918, 1100, 1312))
save("test11c", "sec6_map", 22, (64, 500, 467, 734))
save("test11c", "r_shoes", 22, (618, 983, 1072, 1227))
save("test11c", "r_q2", 22, (128, 1406, 992, 1480))
listening("test12c", 23)
save("test13c", "q28_weather", 26, (128, 523, 1097, 777))
save("test13c", "q29_map", 26, (883, 820, 1092, 922))
