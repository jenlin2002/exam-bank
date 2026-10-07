LISTENING = True
META = dict(n=9, h1="第9回・聽力二", subtitle="Listening Test 2（Unit 3～Unit 4）", title="聽力二（Unit 3～4）")
CROPS = [(f"p1_q{i+1}", 17, (120, 232+192*i, 565, 382+192*i)) for i in range(7)]
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="28分，每題4分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test9/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([0,1,2,0,1,2,0], 1)]),
  dict(title="第二部分：基本問答", meta="32分，每題4分・依據所聽到的內容，選出一個最適合的回答", track=2, items=[
    dict(options=["No. It's Tuesday.","Yes, today is Thursday.","No. It's Monday today."], correct=2),
    dict(options=["It's on Monday.","It's at seven o'clock.","Everyone is having a good time."], correct=1),
    dict(options=["It's at the park.","It's six thirty-five.","It's this Wednesday."], correct=2),
    dict(options=["Oh! I'm sorry.","OK. I can turn it off.","Thanks, but I am not hungry."], correct=0),
    dict(options=["He is free.","He is not ready.","Isn't he sleeping?"], correct=2),
    dict(options=["Yes. Let's go.","Yes. It's time for bed.","Yes. The school is ready."], correct=0),
    dict(options=["Let's not talk to her.","She's at the zoo with Tina.","She's not studying English."], correct=1),
    dict(options=["OK. Let's wait here.","OK. The bus is coming.","Sure. We can walk home."], correct=2),
  ]),
  dict(title="第三部分：言談理解", meta="40分，每題5分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["Tuesday.","Wednesday.","Thursday."], correct=1),
    dict(options=["A sign.","A report.","A movie."], correct=2),
    dict(options=["Take a walk.","Go to a park.","Take a walk with the dog."], correct=2),
    dict(options=["It's on Monday.","It's on Friday.","It's on Saturday."], correct=1),
    dict(options=["The man's fan.","The man's student.","The man's daughter."], correct=0),
    dict(options=["9 p.m.","Ten at night.","Eleven in the morning."], correct=1),
    dict(options=["They are singing a song.","They are watching a music video.","They are fighting with each other."], correct=1),
    dict(options=["Class rules.","Party rules.","House rules."], correct=2),
  ]),
]
