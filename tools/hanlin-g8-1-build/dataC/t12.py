LISTENING = True
META = dict(n=12, h1="第12回・聽力三", subtitle="Listening Test 3（Unit 5～Unit 6）", title="聽力三（Unit 5～6）")
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="35分，每題5分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test12c/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([1,0,1,1,1,0,2], 1)]),
  dict(title="第二部分：基本問答", meta="40分，每題5分・依據所聽到的內容，選出一個最適合的回應", track=2, items=[
    dict(options=["It's 3,280 dollars.","I'll pay for it.","Sorry. The price is too high."], correct=0),
    dict(options=["Sure. I love sailing a lot.","Yes, I'll go surfing with you.","That's right. The boat is mine."], correct=0),
    dict(options=["I take the metro.","I usually go there at 8 a.m.","I don't go to school on weekends."], correct=0),
    dict(options=["It took me around 20 minutes.","It took me three hours to drive there.","I spent 30 minutes riding my bike there."], correct=0),
    dict(options=["No, I don't work at a fire station.","Yes. There's one on the corner.","Yes, it's easy to get there by metro."], correct=1),
    dict(options=["Me too. I like swimming.","I also like mountain climbing.","I like hiking and camping, too."], correct=0),
    dict(options=["It's between the park and the hotel.","You can take a train to the bus station.","Go straight for two blocks and turn left."], correct=2),
    dict(options=["About two thousand dollars.","I won't spend that much money.","I spend 30 minutes having a meal."], correct=0),
  ]),
  dict(title="第三部分：言談理解", meta="25分，每題5分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["By car.","By train.","By metro."], correct=0),
    dict(options=["Five minutes.","Fifteen minutes.","Thirty minutes."], correct=1),
    dict(options=["The belt.","The sweater.","The cap and the belt."], correct=0),
    dict(options=["Near a library.","Near a metro station.","Near Spring Department Store."], correct=1),
    dict(options=["Eighty dollars.","One hundred dollars.","Two hundred and forty dollars."], correct=0),
  ]),
]
