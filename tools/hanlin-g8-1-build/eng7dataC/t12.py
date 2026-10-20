# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEFG".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=12, h1="第12回・Review Test 3", subtitle="Unit 5～Unit 6 總複習")
I = "images/test12/"
CROPS = [P("class", 24, 43, 53, 245, 299)]
RESP = "No, there aren't any bears.|Yes. There are many rats.|It's on February 2.|Isn't there a white horse on the farm?|When is Mother's Day this year?|No. It's this month."
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共22分", items=[
    V("September 25 is an i___t day to me; it's my father's birthday.", "important"),
    V("My name is on the b___k of the notebook, and there is a picture on the front.", "back"),
    V("A: Are there two tigers behind the tree? B: No. There's o___y one.", "only"),
    V("A: What is that big gray a___l? B: Oh, that's an elephant.", "animal"),
    V("I am so hungry. Is there any f___d here?", "food"),
    V("O___r is the tenth month of the year.", "October"),
    V("Vicky's two sisters are thirteen years old, and she is eight. She is the t___d daughter in her family.", "third"),
    V("In today's w___d, people can take pictures with a phone.", "world"),
    V("BTS is a good e___le of a K-pop boy band. They are very popular with young people.", "example"),
    V("C___s is a big holiday in December. It's my family's favorite holiday, too.", "Christmas"),
    V("It's dinner time. Let's sit a___d the table and have dinner.", "around"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共20分", items=[
    M("A: Are ___ any students at school now? B: No. Today is a holiday.", "they|there|those|these", "B"),
    M("A: ___ the date today? B: January 23.", "What's|How's|When's|Where's", "A"),
    M("Teacher's Day is ___ September.", "in|on|of|at", "A"),
    M("There are ___ monkeys near the bus, but there are some zebras around it.", "these|any|not some|no", "D"),
    M("The basketball game is on ___ of April.", "twelve|twelfth|the twelfth|the twelve", "C"),
    M("There aren't ___ apples in the box, but there are ___ oranges.", "no; some|some; any|any; many|many; any", "C"),
    M("A: Are there any lions ___ there? B: Yes. There are five.", "with|of|to|over", "D"),
    M("A: When is Mary's party? B: It's ___ July 6.", "in|on|at|from", "B"),
    M("A: Is Betty's concert in November? B: Yes, and Arthur's concert is ___ that month. A: Great. I can go to two concerts in November.", "also|around|only|before", "A"),
    M("A: Is there a car in front of the house? B: No, ___.", "there aren't|there isn't|there's no|it isn't", "B"),
  ]),
  dict(type="mc", title="三、依句意填入適當的代號", meta="每題2分，共12分・以下各題都從同一組六個句子中選出最適合的一句。", items=[
    M("A: Are there any rats in the house? B: ______", RESP, "B"),
    M("A: When is the movie? B: ______", RESP, "C"),
    M("A: Are there any bears in the zoo? B: ______", RESP, "A"),
    M("A: ______ B: It's on May eleventh.", RESP, "E"),
    M("A: ______ B: Yes, there is. There is one there.", RESP, "D"),
    M("A: Is the baseball game next month? B: ______", RESP, "F"),
  ]),
  dict(type="guided", title="四、看圖回答問題", meta="每題3分，共12分", image=I+"class.png", items=[
    G("1. What's between the students' desks?", "（用 There is... 回答）", "There is a cat between their desks. / There is a cat between the students' desks. / There's a cat between their desks. / There's a cat between the students' desks."),
    G("2. Is there a dog in front of the teacher?", "（簡答）", "Yes, there is."),
    G("3. Are there any rulers on Amy's desk?", "（先簡答，再詳答）", "No, there aren't. There aren't any rulers on her desk. / No, there aren't. There aren't any rulers on Amy's desk."),
    G("4. Are there five people in the classroom?", "（先簡答，再用「三位」詳答）", "No, there aren't. There are three people. / No, there aren't. There are three people in the classroom."),
  ]),
  dict(type="guided", title="五、依提示作答", meta="每題4分，共12分", items=[
    G("The English class is <u>on April 4</u>.", "（依畫線部分造原問句）", "When is the English class? / When's the English class?"),
    G("Yes, there are many rats on the farm.", "（造原問句）", "Are there any rats on the farm? / Are there many rats on the farm?"),
    G("There are tigers under the tall tree.", "（用 any 改寫為否定句）", "There aren't any tigers under the tall tree. / There are not any tigers under the tall tree."),
  ]),
  dict(type="cloze", title="六、克漏字選擇", meta="每題2分，共10分",
    passage="Debby: Hey! There is a museum here. The museum is ___1___ big.\nMiss Chen: Look at the poster. There is a mummy show in the museum ___2___ June 1 to August 10.\nDebby: ___3___ today?\nMiss Chen: It's June 3.\nDebby: Great! We are ___4___. We can see mummies here today.\nMiss Chen: That's ___5___. Let's go inside and take a look now.\n\n【字詞】poster 海報　show 展覽",
    items=[
      dict(options=["now", "so", "only", "maybe"], correct=1),
      dict(options=["at", "in", "on", "from"], correct=3),
      dict(options=["What is", "When is", "What day is", "What's the date"], correct=3),
      dict(options=["full", "first", "lucky", "important"], correct=2),
      dict(options=["new", "okay", "cute", "right"], correct=3),
  ]),
  dict(type="reading", title="七、閱讀測驗", meta="每題4分，共12分", passages=[
    dict(label="", text="Hello, everyone. Welcome to Jay's Animal Park. Look over there. Those brown bears are Jimmy and Jimbo. They're sleeping now. There are two elephants under the tree. They are Jamie and her daughter, Jasmine. They are very friendly. You guys can take pictures with them. Oh, and that tiger is Jared. It's time for his food, and he's hungry now. Don't stand near his cage. That is <u>dangerous</u>. Don't become his food! Now, let's go to Area C. Today is Joanne's second birthday. Let's say happy birthday to her. Who is Joanne? She's my favorite monkey.\n【字詞】friendly 友善的　cage 籠子　become 成為　area 區域　which 哪一個", items=[
      M("What are the people doing?", "Taking a walk at an animal park.|Eating food with a tiger.|Taking pictures with some animals.|Cleaning the cages for some animals.", "A"),
      M("The house is <u>dangerous</u>. = The house is ___.", "not bad|not cute|not safe|not clean", "C"),
      M("Which is right?", "Joanne the monkey is two years old.|People can't take pictures with the animals.|There are no bears in the animal park.|The elephants in the zoo are mother and son.", "A"),
    ]),
  ]),
]
