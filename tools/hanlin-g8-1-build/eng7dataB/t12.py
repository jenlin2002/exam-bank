# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEF".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=12, h1="第12回・Review Test 3", subtitle="Unit 5～Unit 6 總複習")
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共22分", items=[
    V("N___r is between October and December.", "November"),
    V("There are many a___ls in the zoo, and the horses are my favorite.", "animals"),
    V("F___y is the second month of the year.", "February"),
    V("My grandma is 80 years old, but she is very h___y. She can run and dance.", "healthy"),
    V("Jerry and Erin are hungry, but there isn't any f___d for them in the kitchen.", "food"),
    V("They are my dear family; they are very i___t to me.", "important"),
    V("Can you c___n up the living room? It's a mess（亂七八糟）.", "clean"),
    V("B___rs are big. Bugs, fish, and honey（蜂蜜）are their food.", "Bears"),
    V("This Friday is a h___y. There's no school on that day.", "holiday"),
    V("There are ten girls and one boy in this class. James is the o___y boy.", "only"),
    V("There aren't many tigers in the w___d now. They are endangered（瀕臨滅絕的）.", "world"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共26分", items=[
    M("Christmas is on a Thursday ___ this year.", "on|in|×|of", "C"),
    M("There ___ some birds above the tree. Can you see?", "is|are|not|can't", "B"),
    M("A: Look! There is a cute boy ___ over there. B: Wow! He's good.", "×|dance|dancing|can dance", "C"),
    M("A: Are there two rats? B: No, ___.", "it isn't|they aren't|there isn't|there aren't", "D"),
    M("Boys and girls, time for dinner. Let's sit ___ the table and eat.", "above|about|in front|around", "D"),
    M("Today is New Year's Eve. It's my favorite time ___ the year.", "with|of|on|for", "B"),
    M("Can you please turn off the music? Thanks ___ you, I can't sleep.", "to|for|of|at", "A"),
    M("A: Is the turkey good? B: Yes. A: ___ the fish? B: It's good, too.", "What is|How are|How about|Where is", "C"),
    M("A: What's the ___ today? B: It's ___ December 12.", "day; on|date; on|day; in|date; ×", "D"),
    M("March is ___ month of the year.", "three|the three|third|the third", "D"),
    M("A: ___ is Anne's birthday? B: It's ___ June 17.", "When; on|What time; on|What day; in|What; ×", "A"),
    M("What's the date ___ Thanksgiving next year?", "in|of|on|to", "B"),
    M("A: Are there ___ zebras? B: No, there aren't ___ zebras.", "any; some|many; some|any; any|any; many", "C"),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共8分", items=[
    M("A: Are pandas（熊貓）from Asia? B: ___ They are from Asia.", "No, there aren't.|You're right.|They're over there.|You are a big help to me.", "B"),
    M("A: Are you free now? B: ___ I am studying English.", "Not really.|I'm only playing.|That's new to me.|Everyone is thinking about that.", "A"),
    M("A: Hey, what's that? B: A pencil case. ___ A: It's really beautiful.", "It's nice, right?|I can't wait.|Let's look around.|It's jumping up and down.", "A"),
    M("A: Where's Teddy? B: ___", "Over there.|At seven.|On the twenty-first.|He is lucky.", "A"),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="每題2分，共8分",
    passage="Happy Burger's Party Time\nHi, friends. Our ___1___ birthday is next month. Come and celebrate it with us. ___2___ The party is on the night of April 3. You can have nice and special burgers and drinks, and the ___3___ is all free. Please come ___4___ 7 p.m. Let's have a great time.\n\n【字詞】burger 漢堡　celebrate 慶祝　free 免費的",
    items=[
      dict(options=["ten", "the ten", "tenth", "the tenth"], correct=2),
      dict(options=["When is the holiday?", "We are having a good time.", "There's a birthday party for it.", "Let's have a party in the morning."], correct=2),
      dict(options=["back", "food", "example", "world"], correct=1),
      dict(options=["in", "on", "before", "for"], correct=2),
  ]),
  dict(type="reading", title="五、閱讀測驗", meta="每題3分，共18分", passages=[
    dict(label="A.", text="Kevin: Is today September twenty-sixth?\nJulie: No. It's the twenty-seventh.\nKevin: Oh! It's the day before Teacher's Day.\nJulie: Right. And it's also my sister's birthday. There is a birthday party at my house at two this afternoon. Are you coming?\nKevin: Sure.", items=[
      M("What is the date of Teacher's Day?", "It's September 26.|It's September 27.|It's September 28.|It's September 29.", "C"),
      M("When is Julie's sister's birthday party?", "It's today.|It's on September 26.|It's the day after Teacher's Day.|It's on the twenty-eighth of September.", "A"),
    ]),
    dict(label="B.", text="(Nick is live streaming on his phone.)\nHi, everyone. I am Nick. Here is my brother, Aaron. Aaron and I are at the zoo now. There are two tigers, three elephants, and four lions in this area. And there are some zebras, too. The tigers are walking around now. They are hungry and waiting for food. There are also many monkeys in the zoo. Oh, look! There are two monkeys in the tree. The big <u>one</u> is jumping up and down, and the small one is eating a banana. The animals are cute. We are happy at the zoo.\n【字詞】live stream 直播　area 區域", items=[
      M("There aren't any ___ in this area in the zoo.", "tigers|lions|horses|elephants", "C"),
      M("What is \"<u>one</u>\"?", "A lion.|A tiger.|A zebra.|A monkey.", "D"),
      M("The tigers are walking around. Why?（為什麼？）", "They are full.|They are hungry.|They are happy.|They are nervous.", "B"),
      M("Which is NOT true?（何者為非？）", "Nick is using his phone.|Nick is with his brother.|There aren't any zebras in the zoo.|Nick can see some tigers and lions.", "C"),
    ]),
  ]),
  dict(type="guided", title="六、依提示作答", meta="每題3分，共9分", items=[
    G("It's <u>October 10</u>.", "（依畫線部分造原問句）", "What's the date today? / What's the date? / What's today's date? / What is the date today?"),
    G("No, there aren't. There aren't any elephants near the tree.", "（造原問句）", "Are there any elephants near the tree?"),
    G("There is a turkey. / The turkey is on the farm.", "（合併兩句）", "There is a turkey on the farm. / There's a turkey on the farm."),
  ]),
  dict(type="translation", title="七、翻譯", meta="每題3分，共9分", items=[
    T("有兩隻鳥在這匹斑馬的背上。", "There are two birds on the zebra's back. / There are two birds on this zebra's back."),
    T("那個節日是在八月的第二個星期二。", "The holiday is on the second Tuesday of August. / That holiday is on the second Tuesday of August."),
    T("他的生日是父親節的前一天。", "His birthday is the day before Father's Day. / His birthday is on the day before Father's Day."),
  ]),
]
