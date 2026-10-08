"""把某一回裁出來的附圖拼成一張檢查用的總覽圖：python nat_sheet.py <資料夾> <輸出png>（每張圖下面標檔名）"""
import os, sys, glob
from PIL import Image, ImageDraw

folder, out = sys.argv[1:3]
files = sorted(glob.glob(os.path.join(folder, "*.png")))
cols = 3; cw = 520
thumbs = []
for f in files:
    im = Image.open(f).convert("RGB")
    s = min(cw / im.width, 1.0)
    im = im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))))
    thumbs.append((os.path.basename(f), im))
rows = [thumbs[i:i + cols] for i in range(0, len(thumbs), cols)]
heights = [max(t[1].height for t in r) + 22 for r in rows]
sheet = Image.new("RGB", (cols * (cw + 10) + 10, sum(heights) + 10), "white")
d = ImageDraw.Draw(sheet)
y = 5
for r, h in zip(rows, heights):
    for i, (name, im) in enumerate(r):
        x = 10 + i * (cw + 10)
        d.text((x, y), name, fill="red")
        sheet.paste(im, (x, y + 16))
        d.rectangle((x - 1, y + 15, x + im.width, y + 16 + im.height), outline="#999")
    y += h
sheet.save(out)
print(out, sheet.size, len(files), "images")
