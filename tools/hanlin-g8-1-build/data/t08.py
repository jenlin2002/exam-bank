LISTENING = True
META = dict(n=8, h1="第8回・聽力二", subtitle="Listening Test 2（Unit 3～Unit 4）", title="聽力二（Unit 3～4）", tracks=[4,5,6])
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="28分，每題4分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test8/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([2,1,0,0,1,2,2], 1)]),
  dict(title="第二部分：基本問答", meta="32分，每題4分・依據所聽到的內容，選出一個最適合的回應", track=2, items=[
    dict(options=["Yes, it's eleven fifty.","Yes, it's ten past ten.","Yes, it's almost ten o'clock."], correct=0),
    dict(options=["Don't make fun of me.","I am trying to fix the car.","I was wiping the window."], correct=1),
    dict(options=["I want to be a lawyer.","I plan to mop the stairs first.","I seldom dream when I sleep."], correct=0),
    dict(options=["Yes. I gave it up last month.","Yes. I enjoy working at the factory.","Yes. I have a job interview next week."], correct=1),
    dict(options=["Here's your jacket. Put it on.","Just cool down and take it easy.","You finally caught some butterflies."], correct=1),
    dict(options=["I'm not that good at singing.","My dream is to become a singer.","I made up my mind to join the singing contest."], correct=0),
    dict(options=["Yes. Growing up here can be difficult.","Yes. I want to be a farmer and grow a lot of fruits.","Yes. Just remember to move it into the sun during the day."], correct=2),
    dict(options=["I was talking with a relative.","There was nothing under the sofa.","I want to thank you for catching the mouse."], correct=0),
  ]),
  dict(title="第三部分：言談理解", meta="40分，每題5分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["He was eating dinner.","He was seeing the doctor.","He was watching his favorite movie."], correct=1),
    dict(options=["At half past one.","At eleven o'clock.","At a quarter to two."], correct=2),
    dict(options=["She was a lawyer.","She was a secretary.","She was the man's boss."], correct=1),
    dict(options=["It is wrong to buy animals.","Having a pet is a lot of work.","Keeping a pet is always a good idea."], correct=1),
    dict(options=["Keep dreaming.","Plan his own future.","Help her with the cleaning."], correct=2),
    dict(options=["A dentist.","A soldier.","A mail carrier."], correct=0),
    dict(options=["She was a truck driver.","She is having a job interview.","She learned to drive not long ago."], correct=1),
    dict(options=["A reporter.","An engineer.","A factory worker."], correct=0),
  ]),
]
