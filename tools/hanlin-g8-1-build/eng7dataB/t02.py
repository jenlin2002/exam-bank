# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEF".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=2, h1="第2回・Unit 1", subtitle="Who's That Handsome Boy?")
I = "images/test2/"
CROPS = [P("trees", 4, 84, 514, 722, 652), P("wang", 4, 486, 762, 700, 930)]
IMG = '<br><img src="' + I + '{}" alt="題目附圖" style="width:100%;max-width:560px;display:block;margin:6px 0;border-radius:8px;border:1px solid var(--paper-line);">'
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題1分，共10分", items=[
    V("A: Who's that in the picture? B: It's my b___y brother. He's one year old.", "baby"),
    V("My father and A___t Judy are brother and sister.", "Aunt"),
    V("A: Listen! That's Martin's song. B: Wow! Martin is my favorite（最喜愛的）s___r.", "singer"),
    V("Jake is my d___r friend. He's like（像）a brother to me.", "dear"),
    V("Larry is my cousin. His father is my u___e.", "uncle"),
    V("A: Is Jane old? B: No. She is y___g; she is twelve years old.", "young"),
    V("Mrs. Robinson is my mother. I'm her d___r.", "daughter"),
    V("Irene is fourteen years old. She is a j___r high school student.", "junior"),
    V("A: Who is that h___e boy? B: That's Molly's brother. He is very good-looking（好看的）.", "handsome"),
    V("They are Mr. and Mrs. Green. They are h___d and wife.", "husband"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共28分", items=[
    M("A: Are you a police officer? B: Yes, ___.", "I am|you are|I'm|you're", "A"),
    M("A: ___ are they? B: They are Mr. and Mrs. Jones.", "Where|What|Who|How", "C"),
    M("Look! They are Kate and Gina. ___ beautiful.", "They|They're|Their|She's", "B"),
    M("Is your brother ___?", "student|two years|tall|tall boy", "C"),
    M("A: ___ Scott's cousin? B: No, she's not.", "Who is|Are you|Is Mr. Smith|Is Miss Smith", "D"),
    M("A: ___ Heather? B: She's Ben's wife.", "How's|Is she|Who's|Are you", "C"),
    M("A: Who's that woman? B: She is ___.", "forty|short|my doctor|not a singer", "C"),
    M("A: Is she Mrs. Ford? B: No, ___.", "she isn't|it isn't|she's Mrs. Ford|Mrs. Ford isn't", "A"),
    M("A: Is our new teacher old? B: No, ___. He is twenty-four years old.", "we're not|he's|he is|he's not", "D"),
    M("Natalie is my student. Hugo ___ student, too.", "is a|is my|is their|isn't my", "B"),
    M("A: How old is Marie? B: She is sixty-two ___.", "old|years|year old|years old", "D"),
    M("A: Is Paul a nice boy? B: No, ___. He's very naughty（頑皮的）.", "he is|he's a nice boy|he's not nice|he isn't a boy", "C"),
    M("Look at this picture. This is my family. We are a family ___ four.", "to|for|of|at", "C"),
    M("Ben is ___ son, and they are a family.", "Sam and Sara|Sam and Sara's|Sam's and Sara|Sam's and Sara's", "B"),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共10分", items=[
    M("A: ___ B: He's one year old.", "How is your brother?|Who is he?|How old is your brother?|Is Zac a student?", "C"),
    M("A: Hi, I'm Gale. ___ B: I am Debbie. Nice to meet you, too.", "I am an office worker.|How are you?|Nice to meet you.|Who are you?", "C"),
    M("A: That woman is a singer. B: ___ Is she good?", "Really?|Yes, she is.|Hello!|Her name's Lori.", "A"),
    M("A: ___ Who's he? B: Oh, he's Ian Curt.", "Is that a woman?|How is Ian Curt?|That boy is Eric Jones!|Look at that boy.", "D"),
    M("A: ___ B: That's Meg, Brian's sister.", "How is she?|Who is that girl?|Nice to meet you, Meg.|Are they Brian and his sister?", "B"),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="每題2分，共10分",
    passage="Ann: Ken, who's ___1___?\nKen: That's Josh. He's my ___2___; he is my uncle's only son.\nAnn: Is he a student at our school?\nKen: No. He is a ___3___; his comic books are good.\nAnn: ___4___ He looks very young. How old is he?\nKen: He is twenty-five.\nAnn: ___5___\n\n【字詞】only 唯一的　looks 看起來",
    items=[
      dict(options=["boy", "that boy", "a boy", "his"], correct=1),
      dict(options=["cousin", "brother", "grandfather", "classmate"], correct=0),
      dict(options=["cook", "nurse", "writer", "housewife"], correct=2),
      dict(options=["Listen!", "Hello.", "Where?", "Really?"], correct=3),
      dict(options=["I see.", "Yes, he is.", "Oh no!", "Nice to meet you."], correct=0),
  ]),
  dict(type="reading", title="五、閱讀測驗", meta="每題3分，共12分", passages=[
    dict(label="A.", text="Sue: Hey, Tom. Look! Who's she?\nTom: She is my cousin.\nSue: What's her name?\nTom: Her name is Alice White.\nSue: Is she our new classmate?\nTom: Yes. And her mother is our new teacher.\nSue: Wow!", items=[
      M("Who is Alice White?", "She is Tom's aunt.|She is Sue's cousin.|She is Tom's teacher.|She is Sue's classmate.", "D"),
      M("Tom and Sue's new teacher is Tom's ___.", "aunt|doctor|cousin|classmate", "A"),
    ]),
    dict(label="B.", text="Look at this family tree. This is the Hill family. Kevin and Amanda are husband and wife. Fred is their son. Rachel's husband is Zack. They are mother and father to Ray and Sharon. Kevin and Rachel are Mr. and Mrs. Hill's son and daughter. Kevin is a baseball coach at Apple Elementary School. Ray and Sharon are on Kevin's baseball team, and Fred is, too.\n【字詞】coach 教練　team 隊", items=[
      M("Who is NOT on the baseball team?", "Fred.|Rachel.|Ray.|Sharon.", "B"),
      M("Which（哪一個）family tree is correct（正確的）?" + IMG.format("trees.png"), "(A)|(B)|(C)|(D)", "C"),
    ]),
  ]),
  dict(type="guided", title="六、依提示作答", meta="每題3分，共9分", items=[
    G("The beautiful woman is <u>my sister</u>.", "（依畫線部分造原問句）", "Who is the beautiful woman? / Who's the beautiful woman?"),
    G("Is your uncle a police officer?", "（用 office worker 回答）", "No, he's not. He is an office worker. / No, he isn't. He is an office worker. / No, he's not. He's an office worker. / No, he isn't. He's an office worker."),
    G("No, I'm not Andy's wife. I am his sister.", "（造原問句）", "Are you Andy's wife?"),
  ]),
  dict(type="guided", title="七、看圖作答", meta="每題3分，共9分", image=I+"wang.png", items=[
    G("How old is Ted's aunt?", "（數字需拼出）", "She is thirty-six years old. / She's thirty-six years old. / She is thirty-six. / She's thirty-six."),
    G("Is Ted's father a writer?", "（請詳答）", "No, he's not. He's a police officer. / No, he's not a writer. / No, he isn't. He's a police officer. / No, he is not. He is a police officer."),
    G("Is Mr. Wang young?", "（請詳答）", "No, he's not. He is old. / No, he's not young. / No, he isn't. He is old. / No, he isn't. He's old."),
  ]),
  dict(type="translation", title="八、翻譯", meta="每題4分，共12分（A、B 兩句寫在同一格，例：A: … B: …）", items=[
    T("我的堂姊是一位家庭主婦，而我姊姊也是。", "My cousin is a housewife, and my sister is, too. / My cousin is a housewife, and my sister is a housewife, too."),
    T("A：你和強尼（Johnny）是家人嗎？B：不，我們不是。", "A: Are you and Johnny family? B: No, we are not. / A: Are you and Johnny family? B: No, we aren't. / A: Are you and Johnny family? B: No, we're not."),
    T("A：你兒子麥克（Mike），是名作家嗎？B：不是。他是位國小老師。", "A: Is your son, Mike, a writer? B: No. He is an elementary school teacher. / A: Is your son, Mike, a writer? B: No. He's an elementary school teacher."),
  ]),
]
