# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEFG".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=4, h1="第4回・Review Test 1", subtitle="Starter Unit～Unit 2 總複習")
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共22分", items=[
    V("A: The dog is not in front of the door. It is b___d the door.", "behind"),
    V("A: Where is my ruler? B: Isn't it i___e your pencil case? A: Oh, yes. It's in there.", "inside"),
    V("A: Listen! Is this Celine's song? B: Yes, it is. Celine is my favorite s___r.", "singer"),
    V("The house is big; it is for a big f___y.", "family"),
    V("My mother is not a h___fe; she is a nurse.", "housewife"),
    V("A: Are your p___ts doctors? B: No. My father is a writer, and my mother is a teacher.", "parents"),
    V("My brother is thirteen. He is a j___r high school student.", "junior"),
    V("Aunt Dora is in the dining room, not in the k___n.", "kitchen"),
    V("A: Are you Mr. Nelson's d___er? B: Yes. I am Jessie Nelson. Mr. Nelson is my father.", "daughter"),
    V("A: Isn't Henry your c___te? B: No, he isn't. I'm in Smith High School. He is in Lewis High School.", "classmate"),
    V("The watch is sp___l to David. It's a gift from his grandma.", "special"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共24分", items=[
    M("A: ___ are you? B: I am seventeen.", "How|What|Who|How old", "D"),
    M("A: ___ your cat's name? B: Creamy.", "What's|Who's|Where's|How's", "A"),
    M("A: ___ Sara? B: She is Oliver's aunt.", "How's|What's|Who's|Where's", "C"),
    M("A: ___ Ryan and Kelly brother and sister? B: No.", "Is|Are|Am|Be", "B"),
    M("___ classroom number is 705.", "Their|They're|They are|These", "A"),
    M("A: Isn't your grandfather 68 ___ old? B: Yes, he ___.", "years; isn't|years; is|year; isn't|year; is", "B"),
    M("___ their cousin, Ivy, nice and beautiful?", "Am|Are|Is|Be", "C"),
    M("A: ___ in the bag? B: It's a gift for you.", "Who is|What is|Who are|What are", "B"),
    M("My desk is brown, ___ Jason's desk ___.", "but; is|but; isn't|and; aren't|×; isn't", "B"),
    M("A: Welcome to my room. B: Wow! It is ___ room.", "big|blue big|a big blue|and a big", "C"),
    M("A: What are ___ in your bag? B: ___ my new notebooks.", "those; They're|that; It's|it; That's|these; That's", "A"),
    M("A: Aren't these your markers? B: Yes, ___. They are ___ markers.", "they're; my|these are; my|they are; their|they are; our", "D"),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共10分", items=[
    M("A: The woman is very beautiful. B: ___", "It really is.|Isn't she nice?|You are welcome.|You're beautiful, too.", "D"),
    M("A: ___ B: They are cookies from Grandma.", "Who are they?|Are these cookies?|What are these?|Where are Grandma's cookies?", "C"),
    M("A: Where's Kiki? B: ___", "Is her name Kiki?|She's one year old.|Isn't she on the sofa?|She's very young.", "C"),
    M("A: Is he our new teacher? B: Yes. A: ___ B: He's thirty-two.", "How is he?|How old is he?|Is he tall?|What's his name?", "B"),
    M("A: ___ B: They are in the box.", "What are those?|Look at the oranges.|Are those oranges?|Where are the oranges?", "D"),
  ]),
  dict(type="guided-multi", title="四、依句意完成填空", meta="每格2分，共10分", items=[
    GM("", "A: {{What}} are these on the table? B: They {{are}} gifts from my grandma and grandpa. A: Your grandma and grandpa are (r){{really}} nice to you."),
    GM("", "A: Where's my umbrella? It's not in my bag. B: (M){{Maybe}} it's near the door. A: Oh, yes. It's right next {{to}} the door."),
  ]),
  dict(type="guided", title="五、依提示作答", meta="每題3分，共9分", items=[
    G("Who is that person?", "（將名詞改為複數句）", "Who are those people?"),
    G("Your pencils are <u>on the table</u>.", "（依畫線部分造原問句）", "Where are my pencils?"),
    G("Is he Lucy and Mike's cousin?", "（否定簡答＋詳答）", "No, he isn't. He isn't their cousin. / No, he isn't. He isn't Lucy and Mike's cousin. / No, he's not. He's not their cousin."),
  ]),
  dict(type="translation", title="六、翻譯", meta="每題3分，共9分", items=[
    T("那隻老鼠就在椅子的下方。", "The mouse is right under the chair. / That mouse is right under the chair."),
    T("那些女人是警察嗎？", "Are those women police officers? / Are the women police officers?"),
    T("我的毛筆是新的，但我哥哥的毛筆不是。", "My brush is new, but my brother's brush isn't. / My brush is new, but my brother's brush isn't new. / My brush is new, but my brother's brush is not."),
  ]),
  dict(type="cloze", title="七、克漏字選擇", meta="每題2分，共10分",
    passage="Mr. Page: Welcome to my house, Lillian. This is my ___1___.\nLillian: Nice to meet you, Mrs. Page. I'm Lillian.\nMrs. Page: Hi, Lillian. ___2___ I'm Amelia.\nLillian: Nice name. Your house is beautiful.\nMrs. Page: Thanks. Come ___3___ at our rabbit. He's Buddy.\nLillian: Wow! He is white and gray. They are my favorite ___4___. What are these in his bowl?\nMr. Page: They are apples for Buddy.\nLillian: ___5___\n\n【字詞】bowl 碗",
    items=[
      dict(options=["son", "wife", "uncle", "father"], correct=1),
      dict(options=["I am fine.", "Thank you.", "I am nice, too.", "Nice to meet you, too."], correct=3),
      dict(options=["jump", "listen", "look", "talk"], correct=2),
      dict(options=["years", "colors", "names", "persons"], correct=1),
      dict(options=["I see.", "They're tall.", "No, it's not.", "He really is."], correct=0),
  ]),
  dict(type="reading", title="八、閱讀測驗", meta="每題2分，共6分", passages=[
    dict(label="", text="My name is Linda. I am thirty-eight years old. I am a mother and housewife. My husband, Kevin, is a doctor. He is forty-one. He is tall and nice. Our son, Roger, is an elementary school student. Look at this picture. Today is his birthday. This is his cake. He is very happy.\n（圖：一個男孩站在插著蠟燭的蛋糕後面）\n【字詞】today 今天　birthday 生日　cake 蛋糕　which 哪一個　true 真實的", items=[
      M("Who is Linda?", "She's Roger's aunt.|She's Kevin's wife.|She's Kevin's mother.|She's Roger's cousin.", "B"),
      M("Who is in the picture?", "Linda's son.|Linda's cousin.|Linda's husband.|Linda's brother.", "A"),
      M("Which is true?", "Kevin is 51 years old.|Kevin is Roger's uncle.|Roger's mother is a doctor.|Roger's father is a nice person.", "D"),
    ]),
  ]),
]
