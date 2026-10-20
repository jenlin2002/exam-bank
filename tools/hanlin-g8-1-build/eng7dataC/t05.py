# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEFG".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


LISTENING = True
META = dict(n=5, h1="第5回・聽力一", subtitle="Listening Test 1（Starter Unit～Unit 2）", title="聽力一（Starter～Unit 2）")
CROPS = [P(f"p1_q{i+1}", 9, 84, 152.1 + 125.85*i, 700, 252.8 + 125.85*i) for i in range(7)]
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="每題5分，共35分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test5/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([2,0,1,0,2,1,1], 1)]),
  dict(title="第二部分：基本問答", meta="每題5分，共40分・依據所聽到的內容，選出一個最適合的回答", track=2, items=[
    dict(options=["He's fine.","He's Sabrina's brother.","He's eighteen years old."], correct=2),
    dict(options=["One car is not enough.","I see. Is that her car, too?","Oh, really? Your aunt is young."], correct=1),
    dict(options=["Yes, she is my student.","Yes, I'm her teacher.","Yes, she is. She's my teacher."], correct=2),
    dict(options=["It's gray.","It's his favorite clock.","His pencil case is green."], correct=0),
    dict(options=["They are beautiful.","They're my friends.","They are in the school."], correct=1),
    dict(options=["I'm thirty-one.","It's on the bed.","I'm Carol Wang."], correct=2),
    dict(options=["Yes, their house is very big.","No. They are not in the house.","No. The bathroom is next to the kitchen."], correct=1),
    dict(options=["They are inside the box.","They are gifts for Anita.","Your books are under the dining table."], correct=1),
  ]),
  dict(title="第三部分：言談理解", meta="每題5分，共25分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["The man.","The woman's son.","The woman's daughter."], correct=2),
    dict(options=["She's the woman's mom.","She's the man's teacher.","She's the woman's daughter."], correct=0),
    dict(options=["In the kitchen.","In the living room.","In the dining room."], correct=2),
    dict(options=["At home.","At school.","At Brian's house."], correct=2),
    dict(options=["Frank.","Sherry.","Amy."], correct=0),
  ]),
]
