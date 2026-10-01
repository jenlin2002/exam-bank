LISTENING = True
META = dict(n=12, h1="第12回・聽力三", subtitle="Listening Test 3（Unit 5～Unit 6）", title="聽力三（Unit 5～6）", tracks=[7,8,9])
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="28分，每題4分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test12/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([2,0,1,1,2,1,0], 1)]),
  dict(title="第二部分：基本問答", meta="32分，每題4分・依據所聽到的內容，選出一個最適合的回應", track=2, items=[
    dict(options=["They went on foot.","Sometimes they go by taxi.","They got off the train at the wrong stop."], correct=0),
    dict(options=["It is not easy to take them off.","They cost me a thousand dollars.","I spent forty minutes cleaning them."], correct=1),
    dict(options=["We are jogging at a park now.","We'll go biking near the river bank.","We spent an hour fixing the scooter."], correct=1),
    dict(options=["It took me four hours.","I didn't pay anything for it. It was free.","It cost me around three hundred dollars."], correct=0),
    dict(options=["I was a clerk at a toy store.","I like going surfing at Blue Beach.","I try not to spend too much money on clothes."], correct=1),
    dict(options=["The price of things there is very high.","We are going to have a great shopping experience.","The one on the corner of First Street and Park Road."], correct=2),
    dict(options=["No. That restaurant is really expensive.","Yes, the restaurant is right next to the hotel.","No. It takes only ten minutes to walk there."], correct=2),
    dict(options=["Yes. Everything there is on sale.","There are three department stores in this city.","Just go straight for two blocks. It's on the right."], correct=2),
  ]),
  dict(title="第三部分：言談理解", meta="40分，每題5分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["Go sailing.","Go surfing.","Go jogging."], correct=2),
    dict(options=["At a pool.","At a bookstore.","At a fire station."], correct=0),
    dict(options=["She's going to buy a skirt for Evelyn.","She's going to shop for clothes with Dylan.","She's going to wear Evelyn's dress tomorrow."], correct=2),
    dict(options=["He's looking for a bus stop.","He doesn't have a map with him.","He's trying to send something at the post office."], correct=0),
    dict(options=["On foot.","By metro.","By motorcycle."], correct=1),
    dict(options=["A tie, a blue shirt, and a pair of jeans.","A tie, a black shirt, and a pair of jeans.","A tie, a blue shirt, and a pair of black pants."], correct=2),
    dict(options=["She'll take the white coat.","She'll stop buying new clothes.","She'll come back to the store soon."], correct=2),
    dict(options=["He spent five hundred dollars.","They didn't cost him anything.","He paid one thousand dollars for them."], correct=0),
  ]),
]
