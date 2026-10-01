LISTENING = True
META = dict(n=4, h1="第4回・聽力一", subtitle="Listening Test 1（Unit 1～Unit 2）", title="聽力一（Unit 1～2）")
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="28分，每題4分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test4b/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([0,0,2,1,0,1,1], 1)]),
  dict(title="第二部分：基本問答", meta="32分，每題4分・依據所聽到的內容，選出一個最適合的回應", track=2, items=[
    dict(options=["Who are you looking for?","This is he speaking.","Yes, he is mad."], correct=1),
    dict(options=["Yes, they were really heavy.","Yes, and it was really cold.","No, I didn't have it."], correct=1),
    dict(options=["It's warm here in autumn.","I love sunny days.","It's mine, too."], correct=2),
    dict(options=["No, they're not yours.","That's my cousin, Jackie.","They're Ivy's, I think."], correct=2),
    dict(options=["Sure. Here you are.","Yes, you can buy them.","Our gloves are the same."], correct=0),
    dict(options=["He spoke to my teacher.","He was mad at me.","Because I was late."], correct=1),
    dict(options=["Sure, we can go after it ends.","No. We might be late for the class.","No. We can't eat during class."], correct=1),
    dict(options=["Did she get our postcard?","When did you send it?","Let's write her a thank-you card."], correct=2),
  ]),
  dict(title="第三部分：言談理解", meta="40分，每題4分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["Windy.","Rainy.","Cloudy."], correct=0),
    dict(options=["Take an umbrella.","Get a jacket.","Check the weather."], correct=1),
    dict(options=["She isn't good at math.","She called the wrong number.","She doesn't like the lessons."], correct=1),
    dict(options=["She's selling the man a car.","She's giving a gift to the man.","She's pulling the man's leg."], correct=2),
    dict(options=["Mathematics.","Chinese.","History."], correct=2),
    dict(options=["Nathan's.","The man's.","The woman's."], correct=0),
    dict(options=["Doing a report.","Talking on the phone.","Looking for Mr. Smith."], correct=1),
    dict(options=["The weather is not good.","The man is old.","It's time for a meal."], correct=1),
    dict(options=["June, July, and August.","March, April, and May.","December, January, and February."], correct=0),
    dict(options=["Eating.","Checking the weather.","Ordering food."], correct=2),
  ]),
]
