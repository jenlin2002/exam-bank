# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEFG".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=3, h1="第3回・Unit 2", subtitle="Where Are My Pencils?")
I = "images/test3/"
CROPS = [P("look", 6, 48, 50, 610, 136), P("desk", 6, 56, 238, 245, 362), P("apt", 6, 60, 872, 375, 1060)]
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共20分", items=[
    V("The color of my new sofa is b___n.", "brown"),
    V("The d___ng room is next to the living room.", "dining"),
    V("These bananas are sp___l; they are purple, not yellow.", "special"),
    V("A: Are those Eva's pencils? B: M___e. I'm not sure（確定的）.", "Maybe"),
    V("The bedroom is a___ve the living room, not under it.", "above"),
    V("A: What's i___de the box? B: My books, pens, and a ruler.", "inside"),
    V("A: Your pencil case is very beautiful. B: Thanks. It is a g___t from my aunt.", "gift"),
    V("A: Where are those p___e next to your car? B: They are my cousins.", "people"),
    V("Mr. Wang is our f___te teacher. He is very nice to students.", "favorite"),
    V("A: Are you h___y? The apple is for you. B: Yes, I am. Thank you!", "hungry"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共20分", items=[
    M("A: ___ are the boys and girls? B: They're in the classroom.", "What|Who|Where|How", "C"),
    M("My grandpa is ___ Poland（波蘭）.", "on|in|at|of", "B"),
    M("Uncle William is not ___ the bathroom.", "in|to|of|on", "A"),
    M("A: ___ is that? B: It's a baseball.", "How|What|Who|This", "B"),
    M("A: What ___ these? B: ___ are cards for Grandma and Grandpa.", "is; They|is; It|are; This|are; Those", "D"),
    M("The school bus is ___ the tree and the car.", "in|of|at|between", "D"),
    M("Sammy's book is not ___ the desk. It's ___ her box.", "in; above|on; in|near; at|to; at", "B"),
    M("A: Are those your friends? B: ___, ___.", "Yes; they're|Yes; those are|No; they are|No; they're not", "D"),
    M("___ Sherry's pencils.", "It's|That's|This is|These are", "D"),
    M("The bag is beautiful, ___ it is very small.", "too|but|really|right", "B"),
  ]),
  dict(type="vocab", title="三、寫出下列名詞的複數形", meta="每題1分，共9分", items=[
    V("baby →", "babies"), V("game →", "games"), V("boy →", "boys"), V("box →", "boxes"), V("mouse →", "mice"),
    V("watch →", "watches"), V("housewife →", "housewives"), V("family →", "families"), V("woman →", "women"),
  ]),
  dict(type="mc", title="四、對話選擇", meta="每題2分，共6分", items=[
    M("A: ___ B: She's in the living room.", "Who is your mother?|How's your mother?|How old is your mother?|Where's your mother?", "D"),
    M("A: Oh no! My watch is not here. B: ___", "It's enough for you.|The watch is not for you.|They are next to each other.|Maybe it's in the bathroom.", "D"),
    M("A: ___ B: They are brushes.", "What is it?|How are they?|What are those?|Where are they?", "C"),
  ]),
  dict(type="guided", title="五、看圖回答問題", meta="每題2分，共6分", image=I+"look.png", items=[
    G("1. Are these erasers?", "（簡答＋詳答）", "No, they aren't. They are pencil cases. / No, they aren't. These are pencil cases. / No, they aren't. Those are pencil cases. / No, they aren't. They are pencil boxes. / No, they're not. They're pencil cases."),
    G("2. Where's the girl?", "", "She is in the kitchen. / She's in the kitchen."),
    G("3. Is the dog in front of the door?", "（簡答＋詳答）", "No, it isn't. It's behind the door. / No, it isn't. It's next to the door. / No, it isn't. It is behind the door. / No, it isn't. It is next to the door."),
  ]),
  dict(type="guided-multi", title="六、看圖填入表位置關係的字詞", meta="每格1分，共7分", image=I+"desk.png", items=[
    GM("", "The eraser is {{next}} {{to}} the picture."),
    GM("", "The ball is in {{front}} of the cat."),
    GM("", "The book is {{between}} the ruler and the pencil case."),
    GM("", "The box is {{under}} the desk."),
    GM("", "The cat is (b){{behind}} the ball."),
    GM("", "The pencils are {{in/inside}} the pencil case."),
  ]),
  dict(type="guided", title="七、依提示作答", meta="每題3分，共9分", items=[
    G("Those are <u>comic books</u>.", "（依畫線部分造原問句）", "What are those? / What are these?"),
    G("The cookies are <u>on the chair</u>.", "（依畫線部分造原問句）", "Where are the cookies?"),
    G("This is a table, and that is a sofa.", "（改為複數句）", "These are tables, and those are sofas."),
  ]),
  dict(type="translation", title="八、翻譯", meta="每題3分，共9分", items=[
    T("我們的房子就在彼此的隔壁。", "Our houses are right next to each other."),
    T("這間浴室的牆壁是灰色的嗎？", "Are the bathroom walls gray? / Are the walls of the bathroom gray?"),
    T("這間臥室小小的，但它足夠一個人住了。", "The bedroom is small, but it's enough for one person. / The bedroom is small, but it is enough for one person. / This bedroom is small, but it's enough for one person."),
  ]),
  dict(type="cloze", title="九、克漏字選擇", meta="每題2分，共8分",
    passage="(At Alan's birthday party)\nAlan: Hi, Leah. Welcome!\nLeah: Hi, Alan. Wow, your living room is big. And the walls are pink and purple. They are my favorite ___1___.\nAlan: Really? Nice. ___2___ Nick, this is Leah, my high school classmate.\nLeah: ___3___ I'm Leah.\nNick: Nice to meet you, too.\nAlan: Oh, Nick, where's Claire?\nNick: She is right there, ___4___ the door.\n\n【字詞】birthday party 生日派對",
    items=[
      dict(options=["sofas", "tables", "colors", "houses"], correct=2),
      dict(options=["Who are you?", "Good night.", "Come meet my friend.", "Nice to meet you, Nick."], correct=2),
      dict(options=["You are Nick.", "Good night.", "What's your name?", "Nice to meet you."], correct=3),
      dict(options=["inside", "on", "next to", "above"], correct=2),
  ]),
  dict(type="reading", title="十、閱讀測驗", meta="每題3分，共6分", passages=[
    dict(label="", text="Apartment for Rent\n★ 1 living room, 1 bedroom, and 1 bathroom\n★ Between Akins Junior High School and Oak Park\n★ Near Baldwin Farm\nCall Mr. Aaron Lindsey at 0922-422588.\n【字詞】apartment 公寓　rent 出租　call 打電話　which 哪一個　true 真實的", image=I+"apt.png", items=[
      M("Where is the apartment?", "It's on a farm.|It's in a school.|It's next to a park.|It's between a park and a farm.", "C"),
      M("Which is true?", "The table is next to the bed.|The table is in front of the TV.|Baldwin Farm's phone number is 0922-422588.|A TV, a desk, and two chairs are in the living room.", "B"),
    ]),
  ]),
]
