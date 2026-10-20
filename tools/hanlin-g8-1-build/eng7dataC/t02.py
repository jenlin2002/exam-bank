# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEFG".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=2, h1="第2回・Unit 1", subtitle="Who's That Handsome Boy?")
I = "images/test2/"
CROPS = [P("tree", 4, 44, 52, 366, 262)]
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共20分", items=[
    V("A: Look at my f___y picture. B: Who is the girl next to you? A: She's my big sister, Lucy.", "family"),
    V("A: Is this girl your sister? B: No. She's my aunt. A: R___y? She's very young. B: Haha! She's 26.", "Really"),
    V("Mike is my c___te. He and I are in Class（班）D.", "classmate"),
    V("Christie is y___ng. She is twelve years old.", "young"),
    V("That's Peter's c___n, Meg. She's his aunt's daughter.", "cousin"),
    V("Jeremy is Mr. Wilkins's s___n. Mr. Wilkins is Jeremy's father.", "son"),
    V("A: Who's that on TV? B: He's Adam, a s___r. His songs are very good.", "singer"),
    V("A: Is your car old? B: No. It is n___w.", "new"),
    V("I'm fourteen years old, and my b___y sister, Lisa, is three.", "baby"),
    V("A: Is Tina your daughter? B: Yes, she is. A: She is very b___ful. B: Thank you.", "beautiful"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共20分", items=[
    M("A: ___ is she? B: She is Sabrina, Carl's wife.", "Who|What|How|Where", "A"),
    M("A: Isn't Nick an office worker? B: No, he ___.", "not|is|aren't|isn't", "D"),
    M("A: Is the woman ___ grandma? B: Yes, she is.", "she's|Linda is|Linda's|Linda", "C"),
    M("A: ___ is Jason? B: He is 15 years old.", "Who|How|How old|What", "C"),
    M("A: Are you ___? B: Yes, I am.", "boy|good boy|a good boy|boy and girl", "C"),
    M("A: Are Jane and Karen tall? B: Yes, ___.", "they are|she is|we are|I am", "A"),
    M("A: ___ he your uncle? B: Yes, he ___.", "Is; is|Are; is|Is; are|Are; are", "A"),
    M("A: Are you Tom and Jerry? B: Yes, ___.", "you are|I am|we are|he is", "C"),
    M("Jack is a nurse, and ___, too.", "Shelly is a nurse|Shelly is a doctor|Shelly isn't a nurse|Shelly isn't a doctor", "A"),
    M("A: Is Lucky three ___? B: No. He's four.", "year|years|year old|years old", "D"),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共10分", items=[
    M("A: ___ B: He is 41 years old.", "How is he?|How old is he?|Who is he?|What is his name?", "B"),
    M("A: Who is that woman? B: That's Sara's mother. A: ___ She's very young.", "I see.|Is she old?|No, she isn't.|Who's Sara?", "A"),
    M("A: My cousin is a housewife. B: ___", "She's Luke's wife.|Is she a housewife?|Is your cousin a student?|My cousin is a housewife, too.", "D"),
    M("A: ___ B: He's Bill Birkens, Charlie's uncle.", "Who am I?|Who's he?|Who's Bill's uncle?|Who's that woman?", "B"),
    M("A: Hi, I'm Victor. Nice to meet you. B: ___", "Thank you.|Are you Victor?|I'm fine. And you?|Nice to meet you, too.", "D"),
  ]),
  dict(type="guided-multi", title="四、根據圖中的家庭樹填入正確的親屬關係或人名", meta="每格1分，共10分", image=I+"tree.png", items=[
    GM("", "Sam is Max's {{uncle}}."),
    GM("", "Jean is Max's {{aunt}}."),
    GM("", "Elsa is Daniel's {{cousin}}."),
    GM("", "{{Sam}} is Rita's son."),
    GM("", "Sandy's {{daughter}} is Ellen."),
    GM("", "Anna's grandfather is {{Kenny}}."),
    GM("", "Kenny and Rita are husband and {{wife}}."),
    GM("", "Sam and Sandy are {{brother}} and {{sister}}."),
    GM("", "Daniel's {{grandmother/grandma}} is Rita."),
  ]),
  dict(type="guided-multi", title="五、克漏字填空", meta="每題2分，共14分", items=[
    GM("Hi. My name ___1___ Teddy. Look ___2___ this picture of my family. This is my father, Joel. He is a teacher. This is my mother, Emily. She is a teacher, ___3___. This girl is my sister, Jessica. She's nine years ___4___, and she's an ___5___(e) school student. Oh, and that's her dog, Mumbo. Isn't he cute? The young man here is my brother. His name is George. ___6___(H) a writer and a very good cook. We are a happy family ___7___ six.<br>【字詞】cute 可愛的　man 男人",
       "1. {{is}}　2. {{at}}　3. {{too}}　4. {{old}}", "5. {{elementary}}　6. {{He's/He is}}　7. {{of}}"),
  ]),
  dict(type="guided", title="六、依提示作答", meta="每題3分，共12分", items=[
    G("your / twenty-one / Is / years / ? / old / sister", "（重組句子）", "Is your sister twenty-one years old?"),
    G("worker / is / . / an / Danny / not / office", "（重組句子）", "Danny is not an office worker."),
    G("They are <u>Mike and his baby sister</u>.", "（依畫線部分造原問句）", "Who are they? / Who are the boy and girl?"),
    G("Is his mother a doctor?", "（先否定簡答，再用 police officer 詳答）", "No, she isn't. She is a police officer. / No, she's not. She is a police officer. / No, she isn't. She's a police officer. / No, she's not. She's a police officer."),
  ]),
  dict(type="translation", title="七、翻譯", meta="每題4分，共8分", items=[
    T("看看這張照片。這個男生是個國中生嗎？", "Look at this picture. Is this boy a junior high school student?"),
    T("我親愛的爸爸又高又帥。", "My dear father is tall and handsome. / My dear dad is tall and handsome."),
  ]),
  dict(type="reading", title="八、閱讀測驗", meta="每題2分，共6分", passages=[
    dict(label="", text="Woman: Mirror, Mirror. Who is nice and beautiful?\nMirror: Snow White is nice and beautiful.\nWoman: Am I not nice and beautiful?\nMirror: No, you aren't. And Snow White is a 17-year-old girl. How old are you?\nWoman: Um... I'm 71.\nMirror: Snow White is nice. Are you nice?\nWoman: Yes, I am.\nMirror: No. You're bad.\nWoman: What? You are a bad old mirror!\nMirror: I'm old, but I'm not bad. I'm honest.\n【字詞】mirror 鏡子　but 但是　honest 誠實的", items=[
      M("Who is young and nice?", "The mirror.|The woman.|Snow White.|The woman and Snow White.", "C"),
      M("How old is Snow White?", "Seven years old.|Seventy years old.|Seventeen years old.|Seventy-one years old.", "C"),
      M("To the woman, the mirror is ___.", "old and bad|nice and old|good and new|young and beautiful", "A"),
    ]),
  ]),
]
