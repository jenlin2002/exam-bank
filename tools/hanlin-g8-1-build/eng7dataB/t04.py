# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEF".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=4, h1="第4回・Review Test 1", subtitle="Starter Unit～Unit 2 總複習")
I = "images/test4/"
CROPS = [P("pics", 8, 84, 391, 660, 451)]
IMG = '<br><img src="' + I + '{}" alt="題目附圖" style="width:100%;max-width:560px;display:block;margin:6px 0;border-radius:8px;border:1px solid var(--paper-line);">'
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共20分", items=[
    V("That girl is my cousin. Her dad is my u___e.", "uncle"),
    V("My mom is an office w___r. Her office is really big.", "worker"),
    V("Katy is a w___r. Her books are good.", "writer"),
    V("The dog is in f___t of the tree, not behind it.", "front"),
    V("My b___y brother is one year old.", "baby"),
    V("The new sofa is inside the l___g room.", "living"),
    V("My brother is eight. He is an e___y school student.", "elementary"),
    V("Lucy and I are c___es. Mr. Winston is our teacher.", "classmates"),
    V("I love（愛）my parents and sisters. They are very d___r to me.", "dear"),
    V("George is a good p___n. He is very nice.", "person"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共26分", items=[
    M("A: ___ is Rachel Jones? B: She is my aunt.", "What|Who|Where|How", "B"),
    M("Our teacher, Charlie, ___ tall and handsome.", "is|am|be|are", "A"),
    M("The watch is old ___. It's my father's watch.", ", blue|special|but good|and young", "C"),
    M("A: ___ are Ray and Matt? B: Ray is twenty-one, and Matt is sixteen.", "How|What|Who|How old", "D"),
    M("A: ___ Frank's sister's name? B: ___ name's Emily.", "Who's; Her|What's; Her|What's; His|Who's; He's", "B"),
    M("This is a picture of my family. In the picture, we are ___ each other.", "next to|above|between|inside", "A"),
    M("A: Wow! Your new house is big, ___. B: Thank you.", "old and sad|new, beautiful|new but beautiful|new, and beautiful", "D"),
    M("A: Is your dog three ___? B: No. It is five.", "year|years|year old|years old", "D"),
    M("A: Are ___ your comic books? B: No, ___ are not.", "this; they|these; they|that; it|those; it", "B"),
    M("A: Who are the people? B: They are Mr. White's ___.", "son|brush|daughters|pencil boxes", "C"),
    M("A: Who's that boy? B: He is ___ son.", "Troy and Helen's|Troy's and Helen's|Troy's and Helen|Troy and Helen", "A"),
    M("A: ___ your grandma and grandpa at the park? B: Yes, ___.", "Are; they're|Are; they aren't|Aren't; they're|Aren't; they are", "D"),
    M("A: Is that ___ bag? B: No, ___.", "brown; it is|a brown; it is|brown; that isn't|a brown; it isn't", "D"),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共10分", items=[
    M("A: Where's Nini? B: ___", "She is not hungry.|She's a police officer.|She is forty.|Maybe she is in her office.", "D"),
    M("A: Who's that woman? B: She's Ethan's sister, Kelly. A: ___", "I see.|Maybe.|Really.|Nice to meet you, too.", "A"),
    M("A: Mark is a nurse, not a student. B: ___ He's very young.", "Who's he?|Really?|Good morning, Mark.|That's very special.", "B"),
    M("A: ___ That's Leo Cooper's song. B: It is beautiful.", "Stand up.|Look!|Listen!|Come!", "C"),
    M("A: ___ B: That is my teacher.", "Who is she?|What is that?|Are they writers?|Is she a good teacher?", "A"),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="每題2分，共12分",
    passage="Jacob: Welcome, Patrick. Come ___1___ my parents. Mom and Dad, ___2___ Patrick.\nPatrick: Nice to meet you, Mr. and Mrs. Davis.\nJacob's dad: ___3___\nJacob: Come. This is my room. It's ___4___ my parents' bedroom.\nPatrick: Your room is white and big.\nJacob: Yes. White is my ___5___ color.\nPatrick: Hey, ___6___ under your bed?\nJacob: It's my cat, Lulu.",
    items=[
      dict(options=["look", "meet", "say", "watch"], correct=1),
      dict(options=["this is", "it is", "they are", "you are"], correct=0),
      dict(options=["Thank you.", "I see.", "We are fine.", "Nice to meet you, too."], correct=3),
      dict(options=["on", "next to", "between", "in front"], correct=1),
      dict(options=["young", "big", "favorite", "handsome"], correct=2),
      dict(options=["what's that", "how is it", "who are they", "what are those"], correct=0),
  ]),
  dict(type="reading", title="五、閱讀測驗", meta="每題2分，共14分", passages=[
    dict(label="A.", text="Hello, Willy,\n　How are you? Look at this picture. The rabbit is Bunny, my new pet. The ball is her favorite. And the bird is my pet, too. His name is Roy. He is Bunny's friend. Aren't <u>they</u> cute?\n　　　　　　　　Linda\n\nHello, Linda,\n　Bunny and Roy are cute. Look at my picture. The girl next to me is my cousin. Her name is Lois. She is my new classmate, too. She's beautiful. My brother, Danny, is behind Lois. He is shy but cute.\n　　　　　　　　Willy\n【字詞】pet 寵物　cute 可愛的　shy 害羞的", items=[
      M("Which（哪一個）is the picture from Linda?" + IMG.format("pics.png"), "(A)|(B)|(C)|(D)", "B"),
      M("Who are <u>they</u>?", "Bunny and Roy.|Linda and Willy.|Linda and the ball.|Bunny, Roy, and Willy.", "A"),
      M("Who is Lois?", "She's Linda's pet.|She's Linda's friend.|She's Willy's cousin.|She's Danny's classmate.", "C"),
      M("Which is true（真實的）?", "Three people are in Willy's picture.|Danny is Linda's brother.|The rabbit and the bird are brother and sister.|In Willy's picture, Lois is behind Danny.", "A"),
    ]),
    dict(label="B.", text="Hi, my name is Anita. I'm a junior high school student. I'm fourteen years old. My dad is a police officer. He is forty-six years old. My mom is a housewife. She is forty-one years old. My brother, Tony, is a student. He is ten years old. My sister, Lily, is five years old. Justin is my brother and sister's favorite singer. He is handsome. My favorite singer is Richard. He is handsome, too.", items=[
      M("How old is Anita's brother?", "He's five.|He's ten.|He's fourteen.|He's forty-one.", "B"),
      M("What is Anita's father?", "He's a student.|He's a singer.|He's a police officer.|He's an office worker.", "C"),
      M("Which is true?", "Justin is Anita's brother.|Richard is Lily's favorite singer.|Justin and Richard are handsome.|Anita's sister is a junior high school student.", "C"),
    ]),
  ]),
  dict(type="guided", title="六、依提示作答", meta="每題3分，共6分", items=[
    G("Judy's cousin is a housewife.", "（改成 yes-no 問句）", "Is Judy's cousin a housewife?"),
    G("My new notebooks are <u>on the table</u>.", "（依畫線部分造原問句）", "Where are your new notebooks?"),
  ]),
  dict(type="translation", title="七、翻譯", meta="每題3分，共12分", items=[
    T("我們是五口之家。", "We are a family of five. / We're a family of five."),
    T("山姆（Sam）和妮娜（Nina）是夫妻嗎？", "Are Sam and Nina husband and wife?"),
    T("那隻黃色的鳥在你的上方。", "The yellow bird is above you. / That yellow bird is above you."),
    T("飯廳的牆壁是紫色的，但廚房的牆壁不是。", "The dining room walls are purple, but the kitchen walls aren't. / The dining room walls are purple, but the kitchen walls are not. / The walls of the dining room are purple, but the walls of the kitchen aren't."),
  ]),
]
