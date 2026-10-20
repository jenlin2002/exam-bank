# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEFG".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=8, h1="第8回・Review Test 2", subtitle="Unit 3～Unit 4 總複習")
I = "images/test8/"
CROPS = [P("cook", 16, 44, 296, 183, 427)]
RESP = "Don't run in the classroom, please.|No, you can't. Please be quiet.|What day is Sue's baseball game?|What are they doing?|It's at three in the afternoon.|We're taking a walk.|No. Today's Friday."
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共14分", items=[
    V("S___y and Sunday are the weekend.", "Saturday"),
    V("A: Hey, don't f___t with your brother. Be nice to him. B: Sorry.", "fight"),
    V("Please f___w the rule. Don't eat in the museum.", "follow"),
    V("A: Robert, what are you doing? B: I'm s___ying English. A: Good boy.", "studying"),
    V("My favorite day of the w___k is Friday.", "week"),
    V("Sammy, sit down. It's not your t___n. Please wait.", "turn"),
    V("Look at the s___n. You can't use your phone here.", "sign"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共30分", items=[
    M("___ eat in the classroom.", "Don't|Can't|No|Not", "A"),
    M("A: ___ is it? B: It's ten ___ night.", "What time; in|What day; at|What time; at|What day; in", "C"),
    M("___ quiet. Don't talk.", "Are|Is|Am|Be", "D"),
    M("A: The girl is your big fan. ___ you sign the picture for ___? B: Sure.", "Can; her|Can; she|Are; she|Are; her", "A"),
    M("My son is drawing a picture ___ markers.", "for|at|with|to", "C"),
    M("A: Let's ___ write on the table. B: Okay.", "no|not|can't|aren't", "B"),
    M("A: Is the boy jumping rope? B: No, he ___.", "isn't|can't|aren't|am not", "A"),
    M("Linda can ___ songs.", "write|are writing|writing|is writing", "A"),
    M("A: ___ can we go on Sunday? B: We can go to Ann's party.", "How|What|Where|Who", "C"),
    M("Jacob's concert is ___ this Wednesday.", "at|in|for|×", "D"),
    M("Let's go to Grandma's house at ___.", "Sunday|this evening|the morning|twelve o'clock", "D"),
    M("The students are ___ and ___.", "talk; walk|talk; walking|talking; walk|talking; walking", "D"),
    M("A: What ___ you doing? B: I am reading a book.", "is|are|am|be", "B"),
    M("It's 1 a.m. Everyone ___ now.", "is sleeping|are sleeping|sleep|sleeping", "A"),
    M("A: What time is the party? B: It's ___ 8 p.m.", "of|on|in|at", "D"),
  ]),
  dict(type="mc", title="三、依句意填入適當的對應句代號", meta="每題2分，共14分・以下各題都從同一組七個句子中選出最適合的一句。", items=[
    M("A: What time is the movie? B: ______", RESP, "E"),
    M("A: Is it Thursday today? B: ______", RESP, "G"),
    M("A: ______ B: They're eating and drinking.", RESP, "D"),
    M("A: ______ B: Sorry.", RESP, "A"),
    M("A: ______ B: It's on Monday.", RESP, "C"),
    M("A: What are you and Eric doing? B: ______", RESP, "F"),
    M("A: Can I talk on the phone at this place? B: ______", RESP, "B"),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="每題2分，共12分",
    passage="Dora: ___1___ at the big card.\nHarry: Wow! It's beautiful! ___2___\nDora: It's for Jean's birthday party.\nHarry: What ___3___ is the party?\nDora: It's ___4___ five thirty.\nHarry: Oh no! ___5___ now. Let's hurry!\nDora: Wait. The party is not today.\nHarry: Not today? ___6___ is it?\nDora: It's this Friday.\nHarry: Oops!\n\n【字詞】birthday 生日",
    items=[
      dict(options=["Take a walk", "Take a look", "Take a picture", "Have a good time"], correct=1),
      dict(options=["What is it for?", "How is it?", "Where is it from?", "Who is it from?"], correct=0),
      dict(options=["day", "time", "week", "clock"], correct=1),
      dict(options=["at", "on", "in", "of"], correct=0),
      dict(options=["It's at 5 p.m.", "It's 5 p.m.", "It's in the morning", "It's not 5:30"], correct=1),
      dict(options=["What day", "What", "What time", "Where"], correct=0),
  ]),
  dict(type="guided", title="五、看圖詳答問題（數字須拼出）", meta="每題3分，共6分", image=I+"cook.png", items=[
    G("1. What time is it?", "", "It's six forty-five. / It's six forty-five now. / It is six forty-five."),
    G("2. What is the woman doing?", "（cook）", "She is cooking. / She's cooking."),
  ]),
  dict(type="guided", title="六、依畫線部分造原問句", meta="每題3分，共6分", items=[
    G("Julie is <u>dancing and singing</u> in her room.", "（依畫線部分造原問句）", "What is Julie doing in her room? / What's Julie doing in her room?"),
    G("The dog can eat <u>these apples</u>.", "（依畫線部分造原問句）", "What can the dog eat?"),
  ]),
  dict(type="translation", title="七、翻譯", meta="每題3分，共9分", items=[
    T("在教室請安靜。", "Please be quiet in the classroom. / Be quiet in the classroom, please."),
    T("請勿在公車上飲食。", "Please don't eat or drink on the bus. / Don't eat or drink on the bus, please."),
    T("你們放學後可以去新的公園打棒球。", "You can go to the new park and play baseball after school. / You can go play baseball at the new park after school."),
  ]),
  dict(type="reading", title="八、閱讀測驗", meta="每題3分，共9分", passages=[
    dict(label="", text="It's four o'clock on Sunday afternoon. Mark and his family are at the park. Mark is riding a bike with his sister, Penny. Mark's brother, Charlie, is dancing with his grandma. Mark's grandpa is playing basketball with John, Mark's dad. And Mark's mom, Sharon, is reading under a tree. They are all very happy.\n【字詞】bike 腳踏車　which 哪一個　true 真實的", items=[
      M("Who is playing basketball?", "Mark's sister and brother.|Mark's mom and dad.|Mark's grandma and grandpa.|Mark's dad and grandpa.", "D"),
      M("What is Mark's grandma doing?", "Dancing.|Reading.|Riding a bike.|Playing basketball.", "A"),
      M("Which is NOT true?", "It's Sunday.|It's 4 a.m.|Mark's at the park.|Mark's mom is under a tree.", "B"),
    ]),
  ]),
]
