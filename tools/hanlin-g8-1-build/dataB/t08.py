LISTENING = True
META = dict(n=8, h1="第8回・聽力二", subtitle="Listening Test 2（Unit 3～Unit 4）", title="聽力二（Unit 3～4）")
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="28分，每題4分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test8b/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([1,1,1,0,1,1,0], 1)]),
  dict(title="第二部分：基本問答", meta="32分，每題4分・依據所聽到的內容，選出一個最適合的回應", track=2, items=[
    dict(options=["Let's hang them in the sun.","Let's put them in the drawer.","Let's put them on."], correct=0),
    dict(options=["I tried to call you back.","I was mopping the floor at that time.","I am doing the dishes."], correct=1),
    dict(options=["Becoming a soldier is my dream.","I grew up in the USA.","I am a dentist."], correct=0),
    dict(options=["Fine. I can stop.","Yes, I can keep some food on the table.","OK, but it's difficult to find one now."], correct=2),
    dict(options=["Great! I got my dream job.","Terrible. I decided to leave my job.","A reporter interviewed me at work."], correct=0),
    dict(options=["Sorry. I can't drive.","Right. Let's take a rest.","Okay. Then keep driving."], correct=1),
    dict(options=["Yes, it's three forty-five.","Yes, it's two forty-five.","Yes, it's three fifteen."], correct=1),
    dict(options=["I love meeting people, too.","Yes, there are beautiful butterflies.","Don't worry. Everyone is nice here."], correct=2),
  ]),
  dict(title="第三部分：言談理解", meta="40分，每題4分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["She doesn't want to sing.","She is hungry.","She can't fall asleep."], correct=2),
    dict(options=["At seven thirty.","At eight o'clock.","At eight thirty."], correct=1),
    dict(options=["He's a farmer.","He's a salesman.","He's a truck driver."], correct=1),
    dict(options=["A secretary.","A mail carrier.","A lawyer."], correct=0),
    dict(options=["He needs to sleep.","He needs to do some work.","He needs to catch the bus home."], correct=0),
    dict(options=["The man's secretary.","The man's doctor.","The man's relative."], correct=2),
    dict(options=["The boy is taking a shower.","The boy is mopping the floor.","The boy fell down and broke a tub."], correct=1),
    dict(options=["She enjoys doing it.","She wants to be healthy.","There are only stairs in her building."], correct=2),
    dict(options=["She believes in Santa Claus.","She is making fun of the man.","She saw Santa Claus through the window."], correct=1),
    dict(options=["She believes in the man.","She has a gift for the man.","She wants to give the man a job."], correct=0),
  ]),
]
