# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEFG".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


LISTENING = True
META = dict(n=9, h1="第9回・聽力二", subtitle="Listening Test 2（Unit 3～Unit 4）", title="聽力二（Unit 3～4）")
CROPS = [P(f"p1_q{i+1}", 17, 84, 152.1 + 125.85*i, 700, 252.8 + 125.85*i) for i in range(7)]
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="每題5分，共35分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test9/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([2,1,0,2,2,2,0], 1)]),
  dict(title="第二部分：基本問答", meta="每題5分，共40分・依據所聽到的內容，選出一個最適合的回答", track=2, items=[
    dict(options=["Sure. Thank you.","No. You can't run here.","Sorry. You can't eat here."], correct=2),
    dict(options=["Sure. Let's talk to Mom.","Don't turn off your phone.","I see. No phone use in the classroom."], correct=2),
    dict(options=["It's on Friday and Saturday.","It's at 2 p.m. on Wednesday.","It's two thirty in the afternoon."], correct=2),
    dict(options=["Don't take pictures here.","She's watching a music video.","She is in her room now."], correct=1),
    dict(options=["I can't read the sign.","Okay. Wait for me.","Yes, wait for your turn, please."], correct=1),
    dict(options=["Isn't it Monday?","Isn't the movie today?","I'm not free this weekend."], correct=0),
    dict(options=["No, I'm not in the band.","Yes, my favorite color is black.","Yes, and their new songs are great."], correct=2),
    dict(options=["Sara is a cute girl.","Sure, you can.","I can't wait!"], correct=1),
  ]),
  dict(title="第三部分：言談理解", meta="每題5分，共25分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["Sleeping.","Playing a video game.","Watching a music video."], correct=2),
    dict(options=["Monday.","Tuesday.","Wednesday."], correct=1),
    dict(options=["6:30 a.m.","7 p.m.","7:30 p.m."], correct=2),
    dict(options=["At a park.","At the woman's place.","In a museum."], correct=0),
    dict(options=["It's on Thursday.","It's on Saturday.","It's at six o'clock."], correct=1),
  ]),
]
