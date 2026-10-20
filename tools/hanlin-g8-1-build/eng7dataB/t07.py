# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEF".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=7, h1="第7回・Unit 4", subtitle="What Time Is the Concert?")
I = "images/test7/"
CROPS = [P("carol", 14, 40, 270, 330, 480)]
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共20分", items=[
    V("A: T___e a look at the picture. This is my new teacher. B: She is beautiful.", "Take"),
    V("A: Are you with your brother? B: Yes. We're playing a game t___r in the dining room.", "together"),
    V("A: Are you James Lee? B: Yes. A: This box is for you. Please s___n your name here.", "sign"),
    V("My classmates are all coming to my party this Saturday. E___y is welcome.", "Everybody"),
    V("M___y is the first（第一的）day of the week in Taiwan（臺灣）.", "Monday"),
    V("A: Let's go to the movies this afternoon. B: Sorry. I can't go with you. I'm not f___e.", "free"),
    V("Raymond is a p___r singer. Many people are his fans.", "popular"),
    V("A: What are you doing? B: I'm watching a K-pop band's new music v___o. They can really dance.", "video"),
    V("A: Is today W___y? B: No. That's tomorrow（明天）. Today is Tuesday.", "Wednesday"),
    V("A: Let's go to the park this w___d. B: I can go with you on Saturday, but I can't go on Sunday.", "weekend"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共26分", items=[
    M("A: ___ Katie and Mandy playing basketball? B: Yes, they are.", "Is|Are|Can|Be", "B"),
    M("Fred's party is ___ Thursday.", "for|in|on|at", "C"),
    M("The meet-and-greet is ___ 7 p.m.", "at|on|in|above", "A"),
    M("A: Are you free ___ this Tuesday? B: Yes, we are.", "at|in|on|×", "D"),
    M("A: Hey, are you ready ___ the movie? B: Yes. I can't wait.", "to|at|for|on", "C"),
    M("A: ___ is Dad doing? B: He is ___ in his room.", "What; sleep|What; sleeping|Where; sleep|Where; sleeping", "B"),
    M("A: Look! Our new classmate, Mary, ___ rope there. B: She's really good.", "can jump|let's jump|is jumping|are jumping", "C"),
    M("A: Isn't Bill studying in the classroom? B: Yes, ___.", "he is|he isn't|he's|is studying", "A"),
    M("A: What time is the basketball game? B: It's at ___ in the morning.", "17:30|8 a.m.|11 p.m.|nine o'clock", "D"),
    M("Grandma ___ watching TV. She is talking on the phone now.", "are|is|aren't|isn't", "D"),
    M("A: What ___ is it today? B: It's ___.", "day; Friday|day; on Friday|time; this Friday|time; Friday", "A"),
    M("A: ___ is it now? B: It's ___ eleven thirty.", "What day; at|What time; at|What day; on|What time; ×", "D"),
    M("A: Let's go ___ basketball. B: I can't. I'm ___ for my sister.", "play; wait|playing; wait|play; waiting|can play; waiting", "C"),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共8分", items=[
    M("A: What day is it today? B: ___", "It's Thursday.|It's a good day.|It's on Thursday.|It's six o'clock.", "A"),
    M("A: What time is your party? B: ___", "It's today.|It's at seven thirty.|This weekend.|It's on Friday.", "B"),
    M("A: Let's go to Wayne's concert this Saturday. B: Sure. ___", "I see.|Let's hurry.|Really?|I can't wait.", "D"),
    M("A: ___ B: Sorry, I can't. My English class is on Sunday.", "Are you free now?|Lisa's party is this week.|Let's go to the zoo this Sunday.|Is your English class on Sunday?", "C"),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="每題2分，共10分",
    passage="(On the phone)\nRoger: Are you studying, Betty?\nBetty: No, ___1___.\nRoger: ___2___ are you doing?\nBetty: I'm at Jimmy's meet-and-greet. I'm ___3___ on stage now.\nRoger: Who's Jimmy?\nBetty: He's my favorite singer. Oh my! He's looking at me, and we're ___4___ hands. Oh, ___5___ signing a picture for me.\nRoger: How nice!",
    items=[
      dict(options=["I'm not", "it's not", "you aren't", "she isn't"], correct=0),
      dict(options=["How", "Who", "What", "Where"], correct=2),
      dict(options=["go", "going", "be", "being"], correct=1),
      dict(options=["using", "shaking", "reporting", "washing"], correct=1),
      dict(options=["he's", "she's", "you're", "he can"], correct=0),
  ]),
  dict(type="reading", title="五、根據圖片內容，選出正確的答案", meta="每題3分，共12分", passages=[
    dict(label="", text="", image=I+"carol.png", items=[
      M("It's one fifteen in the afternoon. What is Carol doing?", "Eating.|Dancing.|Singing.|Sleeping.", "A"),
      M("Where is Carol at 8:45 p.m.?", "At home.|At a concert.|At school.|At her friend's house.", "B"),
      M("Carol and her friends are having a birthday（生日）party. What time can it be?", "11:50 a.m.|2:36 p.m.|3:17 p.m.|7:38 p.m.", "C"),
      M("It's time for bed for Carol. What time is it?", "It's eleven.|It's seven twenty.|It's four oh six.|It's eleven fifty-five.", "A"),
    ]),
  ]),
  dict(type="reading", title="六、閱讀測驗", meta="每題3分，共6分", passages=[
    dict(label="", text="It's Friday night. It's Eddie's favorite time. Eddie and his father are sitting on the sofa and watching a baseball game. Their favorite team is great. They are very happy. Now, Eddie's favorite player, Jason Lin, is waving to the fans. Eddie is jumping up and down and waving at the TV.\n【字詞】team 隊伍　player 球員　wave 揮（手）", items=[
      M("Where are Eddie and his father?", "In the kitchen.|In the bathroom.|At a baseball game.|In the living room.", "D"),
      M("Which is true?（何者為真？）", "Today is Friday.|Eddie is waving at his fans.|Eddie is playing baseball with his father.|Jason is watching TV with Eddie.", "A"),
    ]),
  ]),
  dict(type="guided", title="七、依提示作答", meta="每題3分，共9分", items=[
    G("My sisters are <u>singing at the concert</u> now.", "（依畫線部分造原問句）", "What are your sisters doing now?"),
    G("Today is Tuesday.", "（造原問句）", "What day is it today? / What day is today? / What day is it?"),
    G("It is six forty now. / It is evening now.", "（合併兩句）", "It is six forty in the evening now. / It's six forty in the evening now."),
  ]),
  dict(type="translation", title="八、翻譯", meta="每題3分，共9分", items=[
    T("爺爺不是在散步嗎？", "Isn't Grandpa taking a walk?"),
    T("我們正擁有個美好的時光。", "We are having a good time. / We're having a good time. / We are having a great time."),
    T("在那樂團裡的那些可愛男孩正在和他們的粉絲握手。", "The cute boys in the band are shaking hands with their fans. / Those cute boys in the band are shaking hands with their fans."),
  ]),
]
