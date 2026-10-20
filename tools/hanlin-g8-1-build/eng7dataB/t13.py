# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEF".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


LISTENING = True
META = dict(n=13, h1="第13回・聽力三", subtitle="Listening Test 3（Unit 5～Unit 6）", title="聽力三（Unit 5～6）")
CROPS = [P(f"p1_q{i+1}", 25, 84, 150 + 111.5*i, 674, 246 + 111.5*i) for i in range(7)]
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="每題4分，共28分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test13/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([1,0,1,2,2,2,1], 1)]),
  dict(title="第二部分：基本問答", meta="每題4分，共32分・依據所聽到的內容，選出一個最適合的回答", track=2, items=[
    dict(options=["Yes, they are tigers.","Yes, there are.","They are over there."], correct=1),
    dict(options=["He is from the USA.","It's at 7 p.m. on August 8.","It's on the third Sunday of June."], correct=2),
    dict(options=["It's healthy.","Maybe it's a bear.","It's an important holiday."], correct=1),
    dict(options=["It's Friday.","It's the day before Christmas.","It's April twenty-first."], correct=2),
    dict(options=["Yes, but it is small.","Yes, it is a small bathroom.","No, it's not my bedroom."], correct=0),
    dict(options=["No, there aren't.","No, they are not.","Yes, they are near the farm."], correct=0),
    dict(options=["Yes, it's a holiday.","No. It's in March here.","Really? When is it?"], correct=1),
    dict(options=["Yes, it's January 23.","No. It's in January.","No. It's the twenty-fourth."], correct=2),
  ]),
  dict(title="第三部分：言談理解", meta="每題4分，共40分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["The pig.","The cow.","The turkey."], correct=2),
    dict(options=["At a zoo.","In a classroom.","In a museum."], correct=0),
    dict(options=["It's on September 7.","It's on September 27.","It's on Teacher's Day."], correct=1),
    dict(options=["A banana.","Some oranges.","An apple."], correct=2),
    dict(options=["It's on November 21.","It's on November 22.","It's on November 23."], correct=1),
    dict(options=["No. There are no foxes.","No. There are three foxes.","Yes. There's only one fox."], correct=1),
    dict(options=["Billy is.","Chris is.","Lisa is."], correct=0),
    dict(options=["In a class.","At a concert.","At a birthday party."], correct=1),
    dict(options=["It's today.","It's on December 24.","It's on Christmas Day."], correct=1),
    dict(options=["A bird.","A cat.","A monkey."], correct=0),
  ]),
]
