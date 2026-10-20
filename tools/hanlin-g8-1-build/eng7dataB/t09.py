# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEF".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


LISTENING = True
META = dict(n=9, h1="第9回・聽力二", subtitle="Listening Test 2（Unit 3～Unit 4）", title="聽力二（Unit 3～4）")
CROPS = [P(f"p1_q{i+1}", 17, 84, 150 + 111.5*i, 674, 246 + 111.5*i) for i in range(7)]
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="每題4分，共28分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test9/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([0,2,0,0,1,1,2], 1)]),
  dict(title="第二部分：基本問答", meta="每題4分，共32分・依據所聽到的內容，選出一個最適合的回答", track=2, items=[
    dict(options=["Turn off the phone, please.","Yes, you can.","Yes, that is my phone."], correct=1),
    dict(options=["It's at 10 a.m.","It's on Friday.","It's Saturday afternoon now."], correct=1),
    dict(options=["It's 1:06.","It's Monday morning.","It's at 2 p.m. on Tuesday."], correct=0),
    dict(options=["Thank you, Mrs. Page.","Yes, he is sleeping.","Sorry, Mrs. Page."], correct=2),
    dict(options=["They are great.","They are watching a video.","They are in the living room."], correct=1),
    dict(options=["Please turn it on now.","We can watch TV together.","I can take a look."], correct=2),
    dict(options=["Yes, he is.","Yes, his bedroom is big.","Yes, he is listening to music."], correct=0),
    dict(options=["Yes, he is shaking.","David is.","Tim is signing pictures."], correct=1),
  ]),
  dict(title="第三部分：言談理解", meta="每題4分，共40分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["It's eleven fifty.","It's eleven twelve.","It's twelve o'clock."], correct=0),
    dict(options=["Studying English.","Watching videos.","Watching TV."], correct=0),
    dict(options=["In the museum.","At the park.","In the classroom."], correct=2),
    dict(options=["It's at 6 p.m.","It's at 6:30 p.m.","It's at 7 p.m."], correct=1),
    dict(options=["A gift.","A pencil box.","A game."], correct=0),
    dict(options=["They can't run or jump.","They can't sit on the chair.","They can't look at the picture."], correct=0),
    dict(options=["He's studying.","He's playing games.","He's reading."], correct=2),
    dict(options=["It's on Friday.","It's on Saturday.","It's on Sunday."], correct=1),
    dict(options=["At an office.","At a concert.","At a museum."], correct=2),
    dict(options=["It's Tuesday.","It's Wednesday.","It's Thursday."], correct=1),
  ]),
]
