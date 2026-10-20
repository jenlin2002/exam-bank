# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEFG".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


LISTENING = True
META = dict(n=13, h1="第13回・聽力三", subtitle="Listening Test 3（Unit 5～Unit 6）", title="聽力三（Unit 5～6）")
CROPS = [P(f"p1_q{i+1}", 25, 84, 152.1 + 125.85*i, 700, 252.8 + 125.85*i) for i in range(7)]
SECTIONS = [
  dict(title="第一部分：辨識句意", meta="每題5分，共35分・依據所聽到的內容，選出符合描述的圖片", track=1,
    items=[dict(q="", image=f"images/test13/p1_q{i}.png", options=["A","B","C"], correct=c) for i, c in enumerate([1,1,0,0,2,2,2], 1)]),
  dict(title="第二部分：基本問答", meta="每題5分，共40分・依據所聽到的內容，選出一個最適合的回答", track=2, items=[
    dict(options=["Here is one example.","Be careful. That's a black bear.","The animals are under the tall tree."], correct=1),
    dict(options=["It is a holiday in Taiwan.","It's on November twenty-eighth.","Today is November twenty-eighth."], correct=1),
    dict(options=["Really? Are you hungry, too?","The food is very healthy for you.","I am hungry. I am eating cookies now."], correct=2),
    dict(options=["It's February.","My birthday is next month.","It is my favorite day of the month."], correct=0),
    dict(options=["Yes, there is, but it's small.","Not really. My kitchen is clean.","Yes, there is some food on the table."], correct=0),
    dict(options=["It's in April.","It's August 29.","It's on the third Sunday of June."], correct=1),
    dict(options=["Yes, birds are cute.","No. They are cows, not birds.","Yes, there's one, and it's eating bugs."], correct=2),
    dict(options=["Really? Good to know.","What's the lucky animal?","They can help each other."], correct=0),
  ]),
  dict(title="第三部分：言談理解", meta="每題5分，共25分・依據所聽到的內容和問題，選出一個最適合的答案", track=3, items=[
    dict(options=["On December 21.","On December 23.","On December 25."], correct=1),
    dict(options=["Only baby elephants.","Baby elephants and their fathers.","Baby elephants and their mothers."], correct=2),
    dict(options=["September 22.","October 10.","October 22."], correct=1),
    dict(options=["Taking a walk on a farm.","Taking pictures with the animals.","Eating dinner with the animals."], correct=0),
    dict(options=["He's talking to his wife.","He's helping Christine.","He's washing his wife's car."], correct=2),
  ]),
]
