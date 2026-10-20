# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEF".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=8, h1="第8回・Review Test 2", subtitle="Unit 3～Unit 4 總複習")
I = "images/test8/"
CROPS = [P("tv", 16, 40, 278, 345, 410)]
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共22分", items=[
    V("Be q___t, Cindy. Grandpa is sleeping.", "quiet"),
    V("A: I can't find（找到）my eraser. B: Here. You can u___e my eraser.", "use"),
    V("Dad is w___hing his car. It's dirty（髒的）.", "washing"),
    V("The students are f___wing the teacher. She is taking（帶…去）them to the school lab.", "following"),
    V("Robin is r___ting a baseball game on TV, and I'm watching it.", "reporting"),
    V("People are dancing and singing at Betty's p___y. They're having a great time.", "party"),
    V("David can fix（修理）the clock for you. He's good with his h___ds.", "hands"),
    V("Let's take a picture. E___y, come here and stand together.", "Everybody"),
    V("Look at the school r___es. Number 1 is \"Don't run in the classroom.\"", "rules"),
    V("The day after T___y is Wednesday.", "Tuesday"),
    V("I can't see the singer. M___y tall people are standing between me and the stage.", "Many"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共26分", items=[
    M("___ off the phone. It's show（表演）time.", "Take|Walk|Turn|Talk", "C"),
    M("It's time ___ bed. Go to your bedroom now.", "for|to|of|on", "A"),
    M("Boys, ___ in the lab. It's not safe.", "isn't running|do not run|can't run|aren't running", "B"),
    M("Look! Sue and Nancy ___ talking to Mr. Miller.", "×|not|are|is", "C"),
    M("A: Ben is sleeping. Please wake ___ up. B: OK, Miss Lin.", "it|he|his|him", "D"),
    M("A: Are you taking a walk? B: Yes, ___.", "it is|I am|I'm|I'm taking", "B"),
    M("Shh. Mr. Hill is looking at ___. Be quiet!", "us|we|our|I", "A"),
    M("A: What ___ is it? B: Let's see. It's ___ Monday.", "time; on|time; ×|day; ×|day; on", "C"),
    M("A: What time is it? B: It's ___.", "Thursday|on Thursday|at 2:30|2:30", "D"),
    M("___ do that here. Look at the sign: No Pictures, Please.", "Please|Not|You can't|Let's", "C"),
    M("A: ___ is Susan reading? B: She's reading in her bedroom.", "Where|What|Who|How", "A"),
    M("Let's ___ basketball ___ Saturday evening. Let's go to the movies.", "can't play; in|don't play; on the|not play; on|play; this", "C"),
    M("The teacher is coming. Let's ___ in the classroom.", "can go|go|is going|going", "B"),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共8分", items=[
    M("A: This is my pen, not your pen. B: ___", "No, I am not.|Oops! I'm sorry.|You can't use a pen.|No. It's a pen.", "B"),
    M("A: Dad, can I watch TV? B: No, you can't. ___", "Be careful.|You can do that now.|Take a look now.|Time for bed.", "D"),
    M("A: I'm free on Saturday. B: ___ Let's go see a movie.", "Great.|Wait.|Hurry!|Sure!", "A"),
    M("A: ___ B: It's at 7 p.m.", "What time is it?|What day is today?|What time is the English class?|Isn't the English class on Friday?", "C"),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="每題2分，共10分",
    passage="Joy: Are you ready ___1___ Dan's meet-and-greet?\nBen: Not really. So many people are here. Let's go home.\nJoy: Please ___2___.\nBen: Uh... okay.\n(on the stage)\nBen: We're almost there. I can see Dan. Hey, ___3___\nJoy: I'm looking for my marker. Dan can sign his name ___4___ the marker. Oh, it's almost my ___5___. I'm so happy!\n\n【字詞】so 很　almost 差不多　look for 尋找",
    items=[
      dict(options=["to", "in", "for", "of"], correct=2),
      dict(options=["don't go", "can't go", "don't be", "not going"], correct=0),
      dict(options=["are you drawing?", "what are you doing?", "is this your marker?", "what time is the meet-and-greet?"], correct=1),
      dict(options=["in", "at", "with", "on"], correct=2),
      dict(options=["turn", "day", "place", "sign"], correct=0),
  ]),
  dict(type="reading", title="五、閱讀測驗", meta="每題2分，共16分", passages=[
    dict(label="A.", text="【電視節目表】\n【字詞】news 新聞", image=I+"tv.png", items=[
      M("Brian is watching <i>Jay and Kate</i>. What time can it be?", "It's 6:30 p.m.|It's 7:15 p.m.|It's 8:40 p.m.|It's 9:10 p.m.", "D"),
      M("Joan is watching <i>The Mummies</i>. What day is it?", "It's Monday.|It's Friday.|It's Saturday.|It's Sunday.", "C"),
      M("It's Sunday. What time is <i>Hello Cat</i> on?", "At 6 p.m.|At 7 p.m.|At 8 p.m.|At 9 p.m.", "B"),
    ]),
    dict(label="B.", text="Jill: Hi, Leah. What are you doing here?\nLeah: I'm buying cookies. The cookies here are great. What are those in your bag?\nJill: Comic books. Today is Luke's birthday. <u>They</u> are for him.\nLeah: Really?\nJill: Yep. Are you free this evening? Let's go to Luke's party at his place together.\nLeah: What time is the party?\nJill: At 6:30 this evening.\nLeah: It's three now. Um... OK. I can go with you.\nJill: Good. Oh, what is your brother, Sam, doing now?\nLeah: He is studying English at home.\nJill: Can he come, too?\nLeah: Maybe. Look! That man is looking at you.\nJill: Oh, that's my father. He is waiting for me. See you at 6 p.m.\nLeah: OK. Bye!\n【字詞】buy 購買　birthday 生日", items=[
      M("Where is Luke's birthday party?", "At Jill's house.|At Luke's house.|At Leah's house.|At the cookie shop（店）.", "B"),
      M("What time is the birthday party?", "At 3 p.m.|At 6 p.m.|At 6:30 a.m.|At 6:30 p.m.", "D"),
      M("What are <u>They</u>?", "Parties.|Cookies.|Comic books.|English books.", "C"),
      M("What is Sam doing?", "He is studying English.|He is waiting for cookies.|He is waiting for his father.|He is reading comic books.", "A"),
      M("Which is true?（何者為真？）", "Jill is waiting for Leah.|Leah is buying cookies.|Jill can't go to Luke's party.|Jill's father is talking to Leah.", "B"),
    ]),
  ]),
  dict(type="guided", title="六、依提示作答", meta="每題3分，共9分", items=[
    G("Turn off the phone.", "（請在句首加入 Steve、句尾加入 please 改寫句子）", "Steve, turn off the phone, please."),
    G("Mia isn't studying. / Mia isn't watching music videos.", "（用 or 合併兩句）", "Mia isn't studying or watching music videos. / Mia is not studying or watching music videos."),
    G("It is eight fifteen now. / It is morning now.", "（合併兩句）", "It is eight fifteen in the morning now. / It's eight fifteen in the morning now."),
  ]),
  dict(type="translation", title="七、翻譯", meta="每題3分，共9分", items=[
    T("現在是晚上十點。", "It's 10 p.m. now. / It's 10 o'clock at night now. / It is ten p.m. now. / It's ten o'clock at night now. / It is 10 p.m. now."),
    T("這週五我們放學後一起去散步吧。", "Let's take a walk after school this Friday. / Let's take a walk together after school this Friday."),
    T("他們正在博物館裡有個很好的時光。（a... time）", "They are having a good time at the museum. / They are having a great time at the museum. / They're having a good time at the museum. / They're having a great time at the museum."),
  ]),
]
