META = dict(n=2, h1="第2回・Unit 1", subtitle="Who's That Handsome Boy?")
I = "images/test2/"
CROPS = [("p1",4,(85,88,205,184)), ("p2",4,(80,188,198,302)), ("tree1",4,(185,612,420,750)), ("tree2",4,(594,690,1097,1055))]
BOX = '<div style="background:#fff;border:1px solid var(--paper-line);border-radius:8px;padding:10px 14px;font-style:italic;margin-bottom:8px;">{}</div>'
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="【A部分 基礎題】每題1分，共7分", items=[
    dict(q="A: Is the boy your c___e? B: No. I'm in Class（班級）708, and he's in Class 709.", answer="classmate"),
    dict(q="My cousin's father is my u___e.", answer="uncle"),
    dict(q="My brother is one year old. He is a ba___y.", answer="baby"),
    dict(q="Sam and Peggy are h___d and wife.", answer="husband"),
    dict(q="Mrs. Dai's son is handsome, and her d___r is very beautiful.", answer="daughter"),
    dict(q="Tim's my brother, and Gina's my sister; they are my f___y.", answer="family"),
    dict(q="Cynthia is a w___r. Her books are good.", answer="writer"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共20分", items=[
    dict(q="A: Is she Emma? B: Yes, ___.", options=["she's","she is","Emma is","she isn't"], correct=1),
    dict(q="A: Is Spot a big dog? B: No. ___", options=["Spot is.","He is big.","He's a dog.","He is small."], correct=3),
    dict(q="A: ___ Cindy? B: My sister.", options=["Who's","How's","What's","Where's"], correct=0),
    dict(q="A: Are you Jason's cousin? B: No, ___.", options=["he isn't","I am not","Jason isn't","you are not"], correct=1),
    dict(q="A: ___ is in the classroom? B: George and Jeff are.", options=["Who","How","What","Where"], correct=0),
    dict(q="A: How old is Jimmy? B: He is 22 ___.", options=["year","years","year-old","years old"], correct=3),
    dict(q="A: Is Zoe ___? B: No, she's not.", options=["cook","a cook","a good","good cook"], correct=1),
    dict(q="A: Isn't he Leo? B: No, he ___.", options=["is","are","isn't","aren't"], correct=2),
    dict(q="A: ___ you their student? B: Yes, ___.", options=["Is; I'm","Is; you are","Are; I am","Are; we are"], correct=2),
    dict(q="A: ___ are they? B: They are Alan and Joanna.", options=["How","Who","What","Where"], correct=1),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共10分", items=[
    dict(q="A: Who is that girl? B: ___", options=["Isn't she Janet?","She's 17 years old.","She is a nice girl, too.","Her name is Tina, not Sue."], correct=0),
    dict(q="A: ___ B: No. I'm a nurse. My mother is a teacher.", options=["Are you a nurse, Lucy?","Are you a teacher, Lucy?","What is your mother's name?","Is your mother a teacher, Lucy?"], correct=1),
    dict(q="A: ___ B: He is 48 years old.", options=["What is his name?","Where's your cousin?","How old is your father?","Who is that handsome boy?"], correct=2),
    dict(q="A: Eric, is this your uncle? B: ___", options=["No. Eric is my cousin.","Yes. Joe is my brother.","Yes. This is my cousin.","Yes. And his name's Joe."], correct=3),
    dict(q="A: Is she a doctor? B: ___", options=["She's nice.","Yes, she is.","Yes, she's Nancy.","She's my grandma."], correct=1),
  ]),
  dict(type="guided-multi", title="四、依提示完成句子", meta="每題1分，共7分", items=[
    dict(zh="", lines=["A: Is Mark a police officer? B: Yes, he {{is}}."]),
    dict(zh="", lines=["A: {{Are}} you Jan's cousin? B: No, I'm not."]),
    dict(zh="", lines=["A: Is that tall woman young? B: No. {{She's}} old."]),
    dict(zh="", lines=["A: {{Who}} is the short girl? B: She is my sister, Annie."]),
    dict(zh="", lines=["A: {{Is}} she your grandma? B: No. She's my aunt."]),
    dict(zh="", lines=["A: Nice to meet you. B: Nice to meet you, {{too}}."]),
    dict(zh="", lines=["A: How old is your baby brother? B: He is one year {{old}}."]),
  ]),
  dict(type="cloze", title="五、克漏字選擇", meta="每題2分，共8分",
    passage="Wendy: Hi, Teresa.\nTeresa: ___1___ How are you today?\nWendy: I'm fine. Thank you. And you?\nTeresa: Not bad. And this is?\nWendy: Oh, ___2___ my cousin, Angel.\nTeresa: Hi, Angel. ___3___ Nice to meet you.\nAngel: Nice to meet you, too. Hmm... are you a doctor?\nTeresa: No, I'm not. I'm a nurse.\nAngel: ___4___ I'm a nurse, too.\n\n【字詞】today 今天",
    items=[
      dict(options=["Oh no!","Good-bye.","Hello, Wendy.","Nice to meet you, Wendy."], correct=2),
      dict(options=["it is","who's","what's","this is"], correct=3),
      dict(options=["I'm Teresa.","This is Teresa.","What's your name?","Is Angel your name?"], correct=0),
      dict(options=["Really?","And you?","That's OK.","Thank you."], correct=0),
  ]),
  dict(type="guided", title="六、看圖回答問題", meta="每題2分，共4分", items=[
    dict(prompt="How old is Kate?", hint="（看圖回答）", image=I+"p1.png", answer="She is thirty years old."),
    dict(prompt="Who is Alex?", hint="（看圖回答）", image=I+"p2.png", answer="He is Mr. and Mrs. Lee's son."),
  ]),
  dict(type="guided", title="七、依提示作答", meta="每題2分，共6分", items=[
    dict(prompt="How old is your brother?", hint="（用「九歲」詳答）", answer="He is nine years old. / He is nine."),
    dict(prompt="She is his wife. / She is Carol.", hint="（用同位語合併句子）", answer="She is his wife, Carol. / She is Carol, his wife."),
    dict(prompt="Are you her grandpa?", hint="（否定回答；先簡答後詳答）", answer="No, I'm not. I'm not her grandpa."),
  ]),
  dict(type="translation", title="八、整句式翻譯", meta="每題3分，共12分（A、B 兩句寫在同一格，例：A: … B: …）", items=[
    dict(zh="A：你是小學老師嗎？B：不。我是國中老師。", answer="A: Are you an elementary school teacher? B: No. I am a junior high school teacher. / A: Are you an elementary school teacher? B: No. I'm a junior high school teacher."),
    dict(zh="A：那個美麗的女人是誰？B：她是伯朗太太的表妹。（伯朗：Brown）", answer="A: Who is that beautiful woman? B: She is Mrs. Brown's cousin. / A: Who's that beautiful woman? B: She's Mrs. Brown's cousin."),
    dict(zh="A：他們的阿姨是歌手嗎？B：是的，她是。", answer="A: Is their aunt a singer? B: Yes, she is."),
    dict(zh="Ben 的姊姊是一名家庭主婦，不是一位警察。", answer="Ben's sister is a housewife, not a police officer."),
  ]),
  dict(type="mc", title="一、單題", meta="【B部分 活用題】每題2分，共12分", items=[
    dict(q="Look at the family tree. Are Frank and Lily brother and sister?", image=I+"tree1.png", options=["No. They are mother and son.","Yes, they are brother and sister.","No. They are husband and wife.","No. They are father and daughter."], correct=3),
    dict(q="A: Who are they? B: They are ___.", options=["her brother","my sister","her mom and dad","your cousin's dog"], correct=2),
    dict(q="___ Candy and Josh at the park?", options=["Am","Are","Is","×"], correct=1),
    dict(q="A: Aren't you an office worker, Tristan? B: Yes, ___.", options=["I am","I'm not","you are","you're not"], correct=0),
    dict(q="A: Who is Miss Lin, Jenny? B: ___", options=["My teacher.","I'm Jenny.","Miss Lin is Jenny.","Jenny is my friend."], correct=0),
    dict(q="A: Isn't he Amanda's uncle? B: No, ___.", options=["I am","I am not","he isn't","he is not my uncle"], correct=2),
  ]),
  dict(type="reading", title="二、依短文或圖表選出適當的答案", meta="每題2分，共14分", passages=[
    dict(label="【A】", text="Andy: Julie, is Jacob your cousin?\nJulie: Yes, he is.\nAndy: Is he a student at Sunny Junior High School?\nJulie: No, he's not, but my sister, Janice, is.\nAndy: Is Janice in Class 802?\nJulie: Yes.\nAndy: My brother, Jim, is in Class 802, too.\n\n【字詞】class 班級", items=[
      dict(q="Who is Jacob?", options=["He's Jim's brother.","He's Andy's cousin.","He's Julie's brother.","He's Janice's cousin."], correct=3),
      dict(q="Who is Jim's classmate?", options=["Andy.","Julie.","Jacob.","Janice."], correct=3),
    ]),
    dict(label="【B】Look at this family tree and answer the questions.", text="【字詞】answer 回答　questions 問題", image=I+"tree2.png", items=[
      dict(q="Who is Amy's grandma?", options=["Susan.","Jane.","Elaine.","Emily."], correct=0),
      dict(q="Who is a teacher?", options=["Leo.","Tom.","Emily.","Peter."], correct=3),
      dict(q="Mark's aunt is a ___.", options=["nurse","writer","doctor","singer"], correct=0),
      dict(q=BOX.format("A: Is your dad an office worker?<br>B: No, he is not. He is a police officer.") + "Who is B?", options=["Jane.","Amy.","Eric.","Mark."], correct=3),
      dict(q="Which（哪一個）is NOT true（真實的）?", options=["Tom is Eric's father.","Jane's aunt is Emily.","Sam's father is Peter.","Mark is Amy's cousin."], correct=0),
    ]),
  ]),
]
