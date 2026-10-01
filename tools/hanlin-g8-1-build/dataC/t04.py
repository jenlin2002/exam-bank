LISTENING = True
META = dict(n=4, h1="第4回・聽力一", subtitle="Listening Test 1（Unit 1～Unit 2）", title="聽力一（Unit 1～2）")
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="35分，每題5分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test4c/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([0,2,1,1,0,2,1], 1)]),
  dict(title="第二部分：基本問答", meta="40分，每題5分・依據所聽到的內容，選出一個最適合的回應", track=2, items=[
    dict(options=["Magic club.","Autumn.","History."], correct=2),
    dict(options=["It's warm and sunny.","It was rainy and cool.","It often snows in winter."], correct=0),
    dict(options=["I can play soccer, too.","Yours is new, but ours isn't.","I'm not sure. Maybe it's Mia's."], correct=2),
    dict(options=["I joined the robot design club.","We have great teachers in our club.","There are many clubs in our school."], correct=0),
    dict(options=["All right. When can I call back?","Sorry. You have the wrong number.","This is Kevin Hill from YKW Office."], correct=0),
    dict(options=["I hate vacations.","Sorry. I'm not free that day.","I usually take a trip with friends."], correct=2),
    dict(options=["I showed it to my sister.","My sister gave it to me.","I sent it to my sister last month."], correct=1),
    dict(options=["We usually have a lot of rain.","It's my favorite time of the year.","There was heavy rain this morning."], correct=0),
  ]),
  dict(title="第三部分：言談理解", meta="25分，每題5分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["Judy.","Ellie.","Sandy."], correct=1),
    dict(options=["Hailey's parents.","Hailey's teachers.","Cooks at Mike's Kitchen."], correct=0),
    dict(options=["They are living in Taiwan now.","The woman doesn't like water sports.","Fall is the man's favorite season."], correct=0),
    dict(options=["A jacket.","A soccer ball.","A box of postcards."], correct=2),
    dict(options=["He walked his dogs.","He washed his car.","He gave a lesson in a music school."], correct=1),
  ]),
]
