"""由 tpl_chinese.html 產生 tpl_nature.html（自然科用）：題號可用 it.no（題組題號連續）、沒有文字也沒有圖的題組不顯示框、記分說明改成選擇題。
自然科全是選擇題，題組也是選擇題；其他（版型、sync.js、送出成績）和國文／社會頁完全一樣。"""
import io, os
HERE = os.path.dirname(os.path.abspath(__file__))
t = io.open(os.path.join(HERE, 'tpl_chinese.html'), encoding='utf-8', newline='').read().replace('\r\n', '\n')
a = '<div class="q-text"><span class="q-num">${i+1}.</span>${it.q}</div>\n        ${imgHtml}${img2Html}'
assert t.count(a) == 1, t.count(a)
t = t.replace(a, '<div class="q-text"><span class="q-num">${it.no||i+1}.</span>${it.q}</div>\n        ${imgHtml}${img2Html}')
b = '<div class="q-text"><span class="q-num">${i+1}.</span>${it.q}</div>\n          ${it.image ?'
assert t.count(b) == 1, t.count(b)
t = t.replace(b, '<div class="q-text"><span class="q-num">${it.no||i+1}.</span>${it.q}</div>\n          ${it.image ?')
c = '      block.appendChild(passageDiv);\n      p.items.forEach'
assert t.count(c) == 1
t = t.replace(c, '      if(p.text || p.image) block.appendChild(passageDiv);\n      p.items.forEach')
d = '（選擇題與填寫題；解釋題不計分）'
assert t.count(d) == 1
t = t.replace(d, '（選擇題）')
io.open(os.path.join(HERE, 'tpl_nature.html'), 'w', encoding='utf-8', newline='').write(t)
print('tpl_nature.html written', len(t))
