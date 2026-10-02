LISTENING = True
META = dict(n=5, h1="第5回・聽力一", subtitle="Listening Test 1（Starter Unit～Unit 2）", title="聽力一（Starter Unit～Unit 2）", tracks=[1,2,3])
CROPS = [(f"p1_q{i}", 9, (170, 311 + 252*(i-1), 748, 311 + 252*(i-1) + 205)) for i in range(1, 8)]
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="28分，每題4分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test5/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([1,2,2,0,0,2,2], 1)]),
  dict(title="第二部分：基本問答", meta="32分，每題4分・依據所聽到的內容，選出一個最適合的回應", track=2, items=[
    dict(options=["Not bad. And you?","Nice to meet you, too.","Good night, my friend."], correct=1),
    dict(options=["They are office workers.","They are fine. Thank you.","They are right next to the sofa."], correct=1),
    dict(options=["We are under 18 years old.","I'm 15, and my brother is 10.","The woman is 46, and her daughter is 13."], correct=2),
    dict(options=["It's above the house.","Isn't he behind the car?","That's not Kellen's dog."], correct=1),
    dict(options=["She is hungry and sad.","She's twenty-seven years old.","She's Kate and Zoe's aunt, Janet."], correct=2),
    dict(options=["Yes, and my grandpa is, too.","No. She is a 60-year-old police officer.","No. My grandma is not an office worker."], correct=0),
    dict(options=["No, it's not my favorite book.","Yes, she is. She is a very good writer.","Yes. She's from my favorite comic book."], correct=1),
    dict(options=["She's next to the door.","It's the girl's favorite picture.","She's Mia, my favorite singer."], correct=2),
  ]),
  dict(title="第三部分：言談理解", meta="40分，每題5分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["Gray.","White.","Brown."], correct=0),
    dict(options=["Inside the car.","Behind the car.","In front of the car."], correct=2),
    dict(options=["A student.","A police officer.","A junior high school teacher."], correct=2),
    dict(options=["Yes, it is.","No, it is not.","Yes, and it is beautiful."], correct=1),
    dict(options=["Four years old.","Five years old.","Six years old."], correct=0),
    dict(options=["In the bedroom.","In the classroom.","In the dining room."], correct=0),
    dict(options=["Paul's aunt.","Paul's cousin.","Paul's daughter."], correct=1),
    dict(options=["A song.","A book.","A person."], correct=0),
  ]),
]
