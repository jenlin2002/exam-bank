LISTENING = True
META = dict(n=13, h1="第13回・聽力三", subtitle="Listening Test 3（Unit 5～Unit 6）", title="聽力三（Unit 5～6）")
CROPS = [(f"p1_q{i+1}", 25, (120, 232+192*i, 565, 382+192*i)) for i in range(7)]
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="28分，每題4分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test13/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([0,1,1,2,0,0,1], 1)]),
  dict(title="第二部分：基本問答", meta="32分，每題4分・依據所聽到的內容，選出一個最適合的回答", track=2, items=[
    dict(options=["Maybe bears.","That's a fox, not a dog.","There are no animals there."], correct=0),
    dict(options=["It's a holiday.","Today is June 17.","It's on November 28."], correct=2),
    dict(options=["It's right there.","It's a small elephant.","It's on the back of the tiger."], correct=2),
    dict(options=["No, there aren't any.","No, the rats are not gray.","No, they are not my favorite."], correct=0),
    dict(options=["Isn't it March 18?","It's on December 30.","It's on New Year's Eve."], correct=0),
    dict(options=["It is in May.","There are twelve.","There are thirty days."], correct=1),
    dict(options=["It's a nice table.","Thanks, but I am full.","They are very healthy."], correct=1),
    dict(options=["It's around April this year.","It's in the second month of the year.","He is having his second birthday next week."], correct=2),
  ]),
  dict(title="第三部分：言談理解", meta="40分，每題5分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["A lion.","A zebra.","An elephant."], correct=1),
    dict(options=["January.","October.","December."], correct=2),
    dict(options=["It's full.","It's cute.","It's clean."], correct=2),
    dict(options=["At a zoo.","At a park.","On a farm."], correct=2),
    dict(options=["December 29.","December 30.","December 31."], correct=0),
    dict(options=["Food.","A bug.","A zebra."], correct=1),
    dict(options=["It's July 4.","It's July 6.","It's July 8."], correct=1),
    dict(options=["A gift.","A rule.","A holiday."], correct=2),
  ]),
]
