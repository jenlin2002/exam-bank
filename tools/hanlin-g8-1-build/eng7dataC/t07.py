# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEFG".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=7, h1="第7回・Unit 4", subtitle="What Time Is the Concert?")
I = "images/test7/"
CROPS = [P("look", 14, 71, 54, 364, 156)]
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共20分", items=[
    V("A: Are you free this w___d? B: Yes. I'm free this Saturday and Sunday.", "weekend"),
    V("Look! The cute dog is sh___ing hands with its owner（主人）.", "shaking"),
    V("The concert is on Tuesday, not on Th___y.", "Thursday"),
    V("A: It's 7:30. Are you r___y for school? B: Yes. Let's go.", "ready"),
    V("A: The cake is small. It's not enough for e___y. B: That's fine. I'm not hungry.", "everybody"),
    V("A: What are you watching? B: My favorite singer's new music v___o. He really can sing.", "video"),
    V("A: Is Nelson very p___r with girls? B: Yes, he is! He's nice, tall, and handsome.", "popular"),
    V("ONI is my favorite girl b___d. All the girls in ONI can sing and dance.", "band"),
    V("Albert is a g___t husband and dad. He's good to his wife and daughters.", "great"),
    V("A: Let's go for a walk t___r at the park now. B: Sure. Let's take（帶）Lucky to the park, too.", "together"),
  ]),
  dict(type="vocab", title="二、寫出下列動詞的現在分詞", meta="每題1分，共6分", items=[
    V("wash →", "washing"), V("come →", "coming"), V("run →", "running"), V("use →", "using"), V("write →", "writing"), V("sit →", "sitting"),
  ]),
  dict(type="mc", title="三、文法選擇", meta="每題2分，共20分", items=[
    M("A: Is David reading a comic book? B: Yes, he ___.", "read|is|reading|is reading", "B"),
    M("A: ___ is it? B: It's Monday.", "What|How|What time|What day", "D"),
    M("A: ___ Grandfather eating in the dining room? B: Oranges.", "What's|Who's|Where's|How's", "A"),
    M("A: What ___ the boys doing there? B: They are drawing pictures.", "can|am|are|is", "C"),
    M("A: ___ Betty watching the ball game? B: In the living room.", "Is|What's|Where's|Who's", "C"),
    M("A: Who ___ singing now? B: Nancy.", "am|is|are|be", "B"),
    M("A: ___ is it? B: It's 9:10.", "What day|How old|What time|What", "C"),
    M("The concert is ___ Friday night.", "at|in|for|on", "D"),
    M("A: What time is your dance class? B: It's ___ four thirty ___ the afternoon.", "in; in|at; on|in; at|at; in", "D"),
    M("The basketball game is ___ this evening.", "in|×|at|on", "B"),
  ]),
  dict(type="mc", title="四、對話選擇", meta="每題2分，共8分", items=[
    M("A: ___ B: Yes, she is.", "Can Jenny cook?|What is Jenny doing?|Is Jenny playing with her cat?|Who is Jenny talking to?", "C"),
    M("A: ___ B: It's at ten o'clock.", "What time is it?|What day is today?|Isn't it on Tuesday?|What time is the party?", "D"),
    M("Isn't the basketball game in the morning? B: ___", "No. It's at 9 a.m.|Yes. It's at 9 a.m.|Yes. It's at 9 p.m.|No. It's not at night.", "B"),
    M("A: What day is OBA's concert? B: ___", "It's Sunday today.|It's on Sunday.|I'm free on Sunday.|Isn't today Sunday?", "B"),
  ]),
  dict(type="guided", title="五、看圖回答問題（數字須拼出）", meta="每題3分，共9分", image=I+"look.png", items=[
    G("1. What day is Sam's welcome party?", "", "It's on Wednesday. / It is on Wednesday."),
    G("2. What time is Sam's welcome party?", "", "It's at six forty-five. / It is at six forty-five."),
    G("3. What is the girl doing?", "", "She is studying English. / She's studying English. / She is reading English. / She's reading English."),
  ]),
  dict(type="guided", title="六、依提示作答", meta="每題3分，共9分", items=[
    G("My brother's baseball game is <u>on Monday</u>.", "（依畫線部分造原問句）", "What day is your brother's baseball game? / When is your brother's baseball game?"),
    G("Their cousins are <u>playing ball</u>.", "（依畫線部分造原問句）", "What are their cousins doing?"),
    G("David is waiting <u>in front of the house</u>.", "（依畫線部分造原問句）", "Where is David waiting? / Where's David waiting?"),
  ]),
  dict(type="translation", title="七、翻譯", meta="每題3分，共6分", items=[
    T("本週五的英文課在幾點呢？", "What time is the English class this Friday?"),
    T("那位受歡迎的歌手正在和他的歌迷握手嗎？", "Is the popular singer shaking hands with his fans? / Is that popular singer shaking hands with his fans?"),
  ]),
  dict(type="cloze", title="八、克漏字選擇", meta="每題2分，共10分",
    passage="___1___ is Saturday today. Joe and his family are at the park. Joe is playing baseball with his sister. Joe's brother is looking at the beautiful flowers and ___2___ pictures of them. Joe's parents ___3___ taking a walk and ___4___ to each other. They are all ___5___ a good time.\n\n【字詞】flower 花朵",
    items=[
      dict(options=["It", "This", "This week", "The weekend"], correct=0),
      dict(options=["taking", "doing", "signing", "shaking"], correct=0),
      dict(options=["be", "is", "can", "are"], correct=3),
      dict(options=["talk", "talking", "is taking", "am talking"], correct=1),
      dict(options=["taking", "doing", "having", "meeting"], correct=2),
  ]),
  dict(type="reading", title="九、閱讀測驗", meta="每題3分，共12分", passages=[
    dict(label="", text="Here's Amy's plan for the week.\nSun. 06:30　Go to a farm with friends\nSun. 18:30　Watch a ball game at Jerry's house\nMon. 17:30　Go to Tommy's concert\nTues. 19:30　Go to Sandy's party\nWed. 17:00　Have dinner with my parents\nThurs. 20:00　Watch Tommy's music videos\nFri. 08:00　Wash Dad's car\nFri. 19:30　Watch a movie at home\nSat. 16:00　Wash my car\n【字詞】plan 計畫　dinner 晚餐", items=[
      M("Today is Wednesday, and it's five-thirty in the afternoon. Who is Amy with?", "Anna.|Jerry.|Sandy.|Her mom and dad.", "D"),
      M("It's 6:30 p.m. on Sunday. Where is Amy?", "On a farm.|At a party.|At a concert.|At Jerry's house.", "D"),
      M("What can Tommy be?", "A nurse.|A writer.|A singer.|A police officer.", "C"),
      M("It's eight o'clock on Friday night. What is Amy doing?", "Watching a movie.|Washing her dad's car.|Watching music videos.|Watching a baseball game.", "A"),
    ]),
  ]),
]
