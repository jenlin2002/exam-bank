LISTENING = True
META = dict(n=4, h1="第4回・聽力一", subtitle="Listening Test 1（Unit 1～Unit 2）", title="聽力一（Unit 1～2）", tracks=[1,2,3])
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="28分，每題4分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test4/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([0,2,1,0,2,1,2], 1)]),
  dict(title="第二部分：基本問答", meta="32分，每題4分・依據所聽到的內容，選出一個最適合的回應", track=2, items=[
    dict(options=["It's Timothy's.","Kyle can play soccer.","You lent yours to Maya."], correct=0),
    dict(options=["Speaking.","This is she.","This is Thea."], correct=2),
    dict(options=["I hate snowy days.","Autumn is my favorite.","It can be cold here in spring."], correct=1),
    dict(options=["That was from Kai.","It's mine, not yours.","I wrote it, but I didn't send it."], correct=0),
    dict(options=["Please hold on.","Sorry about that.","What's up, Johnny?"], correct=0),
    dict(options=["I was like a fish in water.","It was cloudy and windy.","It seldom snows during this time."], correct=1),
    dict(options=["Yes. I did it before you came home.","Yes. Let's do the homework together.","Yes. I helped my brother with his homework."], correct=0),
    dict(options=["My eraser. Did you see it?","I'm looking at the clouds in the sky.","I'm watching a very interesting TV show."], correct=0),
  ]),
  dict(title="第三部分：言談理解", meta="40分，每題5分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["Jack's.","George's.","The woman's."], correct=1),
    dict(options=["Fall.","Winter.","Summer."], correct=1),
    dict(options=["Before she went out.","After she went back home.","When she was at the festival."], correct=2),
    dict(options=["TV shows.","School clubs.","School subjects."], correct=1),
    dict(options=["The woman's number.","Some food from a shop.","An order from the woman."], correct=1),
    dict(options=["It's nice and sunny in January.","It can be very cold there sometimes.","There is only one season on Moon Island."], correct=0),
    dict(options=["A jacket.","A computer.","A baseball glove."], correct=2),
    dict(options=["PE.","Math.","History."], correct=0),
  ]),
]
