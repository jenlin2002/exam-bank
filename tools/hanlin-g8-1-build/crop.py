"""Crop question images out of the scanned 翰林 A卷 PDF.
Boxes are in pixels of the 110-dpi page previews (hanlinA/學用_pNN.png)."""
import pymupdf, os, sys
SRC = r"C:\Users\jenlin2002\OneDrive - avc.co\興雅國中\XXY\校用券1到3 年級全出版社\115年\115上國中2年級校卷\115上翰林2上校卷\115上翰林英文2上校卷\115上翰林英文2上A卷_學用.pdf"
OUT = r"E:\GitHub\exam-bank\hanlin-g8-1\images"
DPI = 170
doc = pymupdf.open(SRC)
k = 72 / 110

def rect(b):
    return pymupdf.Rect(b[0]*k, b[1]*k, b[2]*k, b[3]*k)

def save(test, name, page, *boxes):
    os.makedirs(os.path.join(OUT, test), exist_ok=True)
    path = os.path.join(OUT, test, name + ".png")
    if len(boxes) == 1:
        doc[page-1].get_pixmap(dpi=DPI, clip=rect(boxes[0])).save(path)
    else:  # stack several (page, box) parts vertically
        parts = [(p, rect(b)) for p, b in boxes]
        w = max(r.width for _, r in parts); h = sum(r.height for _, r in parts)
        tmp = pymupdf.open(); pg = tmp.new_page(width=w, height=h); y = 0
        for p, r in parts:
            pg.show_pdf_page(pymupdf.Rect(0, y, r.width, y + r.height), doc, p-1, clip=r); y += r.height
        pg.get_pixmap(dpi=DPI).save(path)
    print(path)

def listening(test, page):
    for i in range(7):
        top = 236 + 192*i
        save(test, f"p1_q{i+1}", page, (122, top, 565, top + 152))

save("test1", "sec5_1", 1, (616, 1195, 748, 1318))
save("test1", "sec5_2", 1, (616, 1322, 742, 1428))
save("test1", "b1_map", 2, (428, 248, 562, 416))
save("test1", "b3_weather", 2, (596, 836, 1098, 1224))
save("test2", "sec5_1", 3, (616, 946, 746, 1064))
save("test2", "sec5_2", 3, (616, 1066, 746, 1188))
save("test3", "b3_poster", 0, (6, (86, 1448, 566, 1612)), (6, (624, 194, 1102, 432)))
listening("test4", 7)
save("test5", "sec4_house", 9, (596, 953, 1100, 1262))
save("test6", "b3_ads", 12, (92, 822, 562, 1388))
save("test7", "sec6_1", 13, (620, 1198, 752, 1320))
save("test7", "sec6_2", 13, (620, 1323, 752, 1442))
listening("test8", 15)
save("test9", "sec4_map", 17, (608, 336, 1090, 712))
save("test9", "b1_bike", 18, (462, 158, 548, 252))
save("test9", "b2_map", 18, (86, 963, 544, 1282))
save("test9", "b2_ad", 18, (623, 450, 1102, 747))
save("test10", "sec4_1", 19, (618, 953, 754, 1067))
save("test10", "sec4_2", 19, (618, 1073, 754, 1192))
save("test10", "b1_sale", 20, (298, 158, 562, 252))
save("test10", "b3_sale", 20, (60, 1188, 562, 1384))
save("test11", "sec4_1", 21, (616, 973, 754, 1094))
save("test11", "sec4_2", 21, (616, 1103, 754, 1212))
save("test11", "b1_sign", 22, (456, 130, 564, 194))
save("test11", "b3_map", 22, (63, 1363, 557, 1627))
listening("test12", 23)
save("test13", "q1", 25, (446, 208, 562, 337))
save("test13", "q28_map", 26, (713, 1373, 1002, 1537))
