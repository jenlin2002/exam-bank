LISTENING = True
META = dict(n=12, h1="第12回・聽力三", subtitle="Listening Test 3（Unit 5～Unit 6）", title="聽力三（Unit 5～6）")
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="28分，每題4分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test12b/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([1,2,2,1,0,1,0], 1)]),
  dict(title="第二部分：基本問答", meta="32分，每題4分・依據所聽到的內容，選出一個最適合的回應", track=2, items=[
    dict(options=["It wasn't cheap at all.","It was on sale.","I spent eight hundred dollars on it."], correct=1),
    dict(options=["You can get there on foot.","It's across from my house.","Walk along this street for ten minutes."], correct=2),
    dict(options=["I want to take it off.","I'll put it on the bed.","No, thanks. I don't like the color."], correct=2),
    dict(options=["About thirty to forty minutes.","I usually take the metro to work.","I work from 9 a.m. to 5 p.m."], correct=0),
    dict(options=["I spent five hundred dollars on it.","I'm not going there.","I'm flying to London with my family."], correct=2),
    dict(options=["Yes, I take a bus to school.","No, the buses are seldom on time.","Yes, there's one across from it."], correct=2),
    dict(options=["I'll wait for your call.","Why do you go jogging?","I go jogging every day."], correct=0),
    dict(options=["It's very expensive.","No. It's very low.","Yes, it cost me a lot."], correct=1),
  ]),
  dict(title="第三部分：言談理解", meta="40分，每題4分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["At a museum.","At a restaurant.","At a clothes shop."], correct=2),
    dict(options=["They are lost.","They're looking for a map.","They're on their way home."], correct=0),
    dict(options=["Showing the man a map.","Asking the man the way.","Taking a taxi with the man."], correct=1),
    dict(options=["By taxi.","On foot.","By motorcycle."], correct=0),
    dict(options=["At a supermarket.","At a restaurant.","At a bank."], correct=0),
    dict(options=["One hundred dollars.","Four hundred dollars.","Five hundred dollars."], correct=0),
    dict(options=["A tie.","Shorts.","Pants."], correct=1),
    dict(options=["He died.","He works on a ship now.","He left the company for another job."], correct=2),
    dict(options=["To save time.","To save money.","To save trouble."], correct=0),
    dict(options=["On a bus.","On the metro.","On a ship."], correct=0),
  ]),
]
