# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEF".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


LISTENING = True
META = dict(n=5, h1="第5回・聽力一", subtitle="Listening Test 1（Starter Unit～Unit 2）", title="聽力一（Starter～Unit 2）")
CROPS = [P(f"p1_q{i+1}", 9, 84, 150 + 111.5*i, 674, 246 + 111.5*i) for i in range(7)]
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="每題4分，共28分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test5/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([1,0,1,2,2,0,0], 1)]),
  dict(title="第二部分：基本問答", meta="每題4分，共32分・依據所聽到的內容，選出一個最適合的回答", track=2, items=[
    dict(options=["She is Rita.","Helen is fine.","Her number is 19."], correct=0),
    dict(options=["He is 16 years old.","He is tall and handsome.","He's John's son."], correct=2),
    dict(options=["My husband isn't old.","He's fine. Thank you.","He's forty-two years old."], correct=2),
    dict(options=["They are young.","They are pencil cases.","They are pink."], correct=1),
    dict(options=["Yes, they're notebooks.","No. They're my brother's notebooks.","No, they're not your notebooks."], correct=1),
    dict(options=["They are writers.","They are my parents.","They are in the dining room."], correct=2),
    dict(options=["It is gray.","They are beautiful.","It is my cat."], correct=2),
    dict(options=["Yes, she is.","No, they aren't.","Yes, they are Debbie and Judy."], correct=1),
  ]),
  dict(title="第三部分：言談理解", meta="每題4分，共40分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["He is Jay.","He is Bill.","He is Sam."], correct=2),
    dict(options=["Susan.","John.","Annie."], correct=2),
    dict(options=["In the kitchen.","In the bathroom.","In the dining room."], correct=1),
    dict(options=["It's white.","It's purple.","It's blue."], correct=0),
    dict(options=["An egg.","A clock.","A notebook."], correct=2),
    dict(options=["It is near the school.","It is next to Lily's house.","It is in the park."], correct=1),
    dict(options=["He's eighteen.","He's fifteen.","He's twelve."], correct=0),
    dict(options=["She's a writer.","She's a singer.","She's Jenny's sister."], correct=1),
    dict(options=["They're on the desk.","They're on the bed.","They're under the bed."], correct=2),
    dict(options=["A doll.","A special pencil.","A pencil case."], correct=2),
  ]),
]
