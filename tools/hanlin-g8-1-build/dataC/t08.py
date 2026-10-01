LISTENING = True
META = dict(n=8, h1="第8回・聽力二", subtitle="Listening Test 2（Unit 3～Unit 4）", title="聽力二（Unit 3～4）")
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="35分，每題5分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test8c/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([0,1,1,2,1,2,0], 1)]),
  dict(title="第二部分：基本問答", meta="40分，每題5分・依據所聽到的內容，選出一個最適合的回應", track=2, items=[
    dict(options=["I was tired all the time.","I went to bed at ten last night.","I was too scared, so I couldn't sleep."], correct=2),
    dict(options=["I caught fish at sea.","I'm mopping the floor.","I was fixing my computer."], correct=2),
    dict(options=["Yes, the woman saw him.","Yes, he took things to different places.","Yes, he was driving the truck at that time."], correct=2),
    dict(options=["I like art very much.","I want to be a reporter.","I love to make cookies."], correct=2),
    dict(options=["Working with him is great.","He became a soldier last year.","Growing fruit. He's a good farmer."], correct=2),
    dict(options=["I want to become a salesman.","It's difficult to find a dream job.","I don't want to move to another city."], correct=0),
    dict(options=["Yes, I looked for it last week.","Yes. I was worrying about it.","Yes. I found it in my desk drawer."], correct=2),
    dict(options=["Yes, someone is playing the violin.","Yes. I'm poor at playing the violin.","Yes. It's fun for me to play the violin."], correct=2),
  ]),
  dict(title="第三部分：言談理解", meta="25分，每題5分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["Ms. Hill's boss.","Ms. Hill's secretary.","A worker at AMT Company."], correct=1),
    dict(options=["She went to bed after 11 p.m.","She slept for eight hours every night.","She had terrible dreams every night."], correct=2),
    dict(options=["A dentist.","A reporter.","A truck driver."], correct=0),
    dict(options=["She fed cats with Bella this morning.","Her piano class starts at half past six.","She walked her dog at the park today."], correct=2),
    dict(options=["He doesn't have a place to practice dancing.","He doesn't like dancing in front of his family.","He is nervous when he dances in front of people."], correct=2),
  ]),
]
