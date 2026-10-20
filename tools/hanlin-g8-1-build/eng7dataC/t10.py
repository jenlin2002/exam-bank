# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEFG".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=10, h1="第10回・Unit 5", subtitle="What's the Date?")
I = "images/test10/"
CROPS = [P("cal", 20, 44, 673, 721, 877), P("pics", 20, 71, 476, 170, 619)]
BX = '<div style="border:1px solid var(--paper-line);border-radius:6px;padding:4px 8px;margin:2px 0;">{}</div>'
RESP = "How about you?|What's the date today?|When is it?|It's in May, not July.|It's on the twenty-fourth."
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共22分", items=[
    V("In the USA, Thanksgiving is in N___r.", "November"),
    V("A: What is your favorite a___l? B: Dogs.", "animal"),
    V("New Year's Eve is the day before J___y first.", "January"),
    V("Please wash your hands b___re dinner.", "before"),
    V("Judy is my aunt, and she is a___o my English teacher.", "also"),
    V("A: Amy Jones is my favorite writer. She's o___y fourteen. B: Wow, she's really young.", "only"),
    V("June is the sixth m___th of the year.", "month"),
    V("The students are sitting a___d the table and waiting for cookies.", "around"),
    V("Today is my b___y. I'm eighteen years old now.", "birthday"),
    V("A: Dad, what's that on the farm? It's black and white. B: It is a c___w. And it's eating grass（草）.", "cow"),
    V("Andy is really l___ky. He can go to NCT's concert for free（免費的）.", "lucky"),
  ]),
  dict(type="vocab", title="二、依例寫出下列數字的序數", meta="每題1分，共5分・例：10 → tenth", items=[
    V("3 →", "third"), V("5 →", "fifth"), V("9 →", "ninth"), V("12 →", "twelfth"), V("40 →", "fortieth"),
  ]),
  dict(type="mc", title="三、文法選擇", meta="每題2分，共22分", items=[
    M("A: ___ is the date today? B: June 22.", "When|What|How|What time", "B"),
    M("A: ___ is the baseball game? B: This Saturday.", "When|What|What date|What time", "A"),
    M("William's concert is ___ May 8.", "at|in|on|to", "C"),
    M("Today is ___.", "in March|tenth|on March tenth|March tenth", "D"),
    M("Mother's Day is ___ the second Sunday ___ May.", "on; on|×; on|at; in|on; of", "D"),
    M("This Tuesday is my ___ birthday.", "sixteen|the sixteen|sixteenth|the sixteenth", "C"),
    M("In Taiwan（臺灣）, Father's Day is ___ August.", "at|in|on|×", "B"),
    M("A: What's the ___ of Teacher's Day? B: September 28.", "date|day|time|month", "A"),
    M("A: It's 7 a.m. now. You are very early（早的）. B: Yes. I am ___ student at school today.", "one|the one|first|the first", "D"),
    M("Janet's birthday is the day ___ Christmas Eve. It's on December 23.", "on|in front of|before|of", "C"),
    M("A: Let's go to Leo's party ___ the night ___ New Year's Eve. B: Sure.", "for; of|on; of|at; in|in; on", "B"),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="每題2分，共10分",
    passage="Amy: ___1___\nTed: It's September 22.\nAmy: Ben's birthday is ___2___ September 28.\nTed: That's right. It's ___3___ Monday.\nAmy: Yes. That day is ___4___ Teacher's Day.\nTed: Well, Ben's book bag is very old. Maybe we can get a new book bag for him.\nAmy: Good idea. ___5___ is Ben's birthday party? Let's go to his party together.\nTed: Sure. It's on the afternoon of September 27.\n\n【字詞】get 買　idea 點子",
    items=[
      dict(options=["What day is it?", "What time is it?", "What's the date today?", "When is Ben's birthday?"], correct=2),
      dict(options=["in", "on", "at", "of"], correct=1),
      dict(options=["in", "at", "that", "next"], correct=3),
      dict(options=["only", "also", "maybe", "really"], correct=1),
      dict(options=["When", "What day", "What week", "What time"], correct=0),
  ]),
  dict(type="mc", title="五、依句意填入適當的對應句代號", meta="每題2分，共8分・以下各題都從同一組五個句子中選出最適合的一句。", items=[
    M("A: ______ B: It's November 29.", RESP, "B"),
    M("A: Justin is my favorite singer. ______ B: My favorite singer is Avril.", RESP, "A"),
    M("A: Amber's birthday is coming. B: Really? ______ A: It's on June 17, next Monday.", RESP, "C"),
    M("A: Is Nick's meet-and-greet on June 25? B: No. ______", RESP, "E"),
  ]),
  dict(type="guided", title="六、依提示作答", meta="每題3分，共9分", items=[
    G("It is <u>July 16</u>.", "（依畫線部分造原問句）", "What's the date today? / What's today's date? / What is the date today? / What's the date?"),
    G("When is the basketball game?", "（四月二十日；日期用序數拼寫）", "It's on April twentieth. / It is on April twentieth."),
    G("<u>November</u> is the eleventh month of the year.", "（依事實將畫線部分用 February 改寫整句）", "February is the second month of the year."),
  ]),
  dict(type="guided-multi", title="七、引導式翻譯", meta="每格1分，共9分", items=[
    GM("聖誕節在十二月二十五日，而且它是個重要的節日。", "{{Christmas}} is {{on}} {{December}} {{twenty-fifth}}, and it's an {{important}} {{holiday}}."),
    GM("我在公園附近。你呢？", "I'm (a){{around}} the park. {{How}} {{about}} you?"),
  ]),
  dict(type="guided", title="八、看圖詳答日期（日期用英文拼寫）", meta="每題3分，共6分", image=I+"pics.png", items=[
    G("1. When is the movie?", "", "It's on October twenty-third. / It is on October twenty-third."),
    G("2. This is a coupon（折價券）. When can Mrs. Smith use it?", "", "She can use it on March fourteenth."),
  ]),
  dict(type="reading", title="九、根據 David 八月的計畫表，選出正確的答案", meta="每題3分，共9分", passages=[
    dict(label="", text="", image=I+"cal.png", items=[
      M("When is Lily's birthday?", "August first.|August thirteenth.|August thirtieth.|August thirty-first.", "C"),
      M(BX.format("A: Are you ready for Jay's concert?<br>B: Yes. I can't wait. Let's go.") + "What's the date today?", "It's August second.|It's August twelfth.|It's August twentieth.|It's August twenty-second.", "B"),
      M("Which is NOT true?", "Billy's baseball game is on August third.|David's birthday is on the first day of August.|The school party is on the night of August eigth.|Father's Day is on the second Wednesday of August.", "C"),
    ]),
  ]),
]
