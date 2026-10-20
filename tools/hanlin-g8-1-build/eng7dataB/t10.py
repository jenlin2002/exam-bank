# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEF".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=10, h1="第10回・Unit 5", subtitle="What's the Date?")
BX = '<div style="border:1px solid var(--paper-line);border-radius:6px;padding:4px 8px;margin:2px 0;">{}</div>'
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共22分", items=[
    V("My family and I are sitting a___d the dining table.", "around"),
    V("A___t is the month right after July.", "August"),
    V("Today is D___r 24. It's Christmas Eve.", "December"),
    V("Dogs are my favorite a___ls.", "animals"),
    V("It's New Year's Day, and it's a h___y. We're not going to school today.", "holiday"),
    V("J___y is the first month of the year.", "January"),
    V("A: Is your birthday this Saturday—April 17? B: No. It's n___t Saturday—April 24.", "next"),
    V("Tina is 14 years old. She is in her s___d year of junior high school.", "second"),
    V("Max is my classmate, and he is a___o my dear friend.", "also"),
    V("A: What are those numbers on your notebook? B: 928. It's my birthday, S___r twenty-eighth.", "September"),
    V("A: Your brother is very tall. Is he a junior high school student? B: No. He is o___y nine years old.", "only"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共24分", items=[
    M("Lisa Sawyer's concert is ___ October.", "at|on|in|on the", "C"),
    M("A: ___ the date today? B: It's June 9.", "What's|When's|How's|Where's", "A"),
    M("A: Is Father's Day ___ August 8? B: Yes, it is.", "at|in|on|of", "C"),
    M("A: ___ is Debbie's party? B: It's this Saturday.", "What|When|How|What time", "B"),
    M("Gina's birthday is on the twenty-sixth ___ July.", "at|for|of|on", "C"),
    M("Please wait for me in my office. It's ___ room on your left（左邊）.", "third|three|the third|the three", "C"),
    M("A: What's the ___ of Mother's Day this year? B: It's May 13.", "day|date|time|month", "B"),
    M("A: Hey, dinner is ready. Don't eat those cookies. B: I'm not eating them. I'm ___ looking at them.", "only|also|too|first", "A"),
    M("Boys, go wash your hands ___ dinner.", "on|at|before|in front of", "C"),
    M("A: Let's eat turkey together ___ the night ___ Thanksgiving. B: Sure.", "on; in the|on; of|at; in|at; at", "B"),
    M("A: ___ is the Christmas party? B: It's at 7 p.m. this Friday.", "What|How|What date|When", "D"),
    M("Today is Mia's ___ birthday.", "twentieth|twenty|the twenty|the twentieth", "A"),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共8分", items=[
    M("A: ___ B: Today is November 29.", "What day is it?|What time is it?|What's the date?|Is the party in November?", "C"),
    M("A: My favorite color is purple. ___ B: My favorite color is yellow.", "How is that?|What are you?|What color is it?|How about you?", "D"),
    M("A: Lily's birthday is coming. B: ___ A: It's on June 30.", "Can I go there?|When is it?|What day is it?|What time is it?", "B"),
    M("A: Isn't the concert in December? B: ___ A: I see. It's around the time of Thanksgiving in November.", "Yes, it's on December 12.|No. It's on New Year's Day.|No. It's a month before Christmas.|Yes, it's on the third Sunday of December.", "C"),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="每題2分，共10分",
    passage="Nora: What's the date today, Lucas?\nLucas: ___1___\nNora: ___2___ is Thanksgiving?\nLucas: November 25. It's on ___3___ Thursday of November.\nNora: Wow! ___4___ Let's have a Thanksgiving dinner.\nLucas: Sure. Let's celebrate the ___5___ together on that day.\nNora: OK.\n\n【字詞】celebrate 慶祝",
    items=[
      dict(options=["It's on Thursday.", "It's November 20.", "The party is today!", "It's on November 25."], correct=1),
      dict(options=["How", "What", "When", "Where"], correct=2),
      dict(options=["four", "the four", "fourth", "the fourth"], correct=3),
      dict(options=["It's next week!", "It's in December!", "I'm not free that day.", "How about today?"], correct=0),
      dict(options=["date", "eve", "holiday", "month"], correct=2),
  ]),
  dict(type="reading", title="五、閱讀測驗", meta="每題3分，共18分", passages=[
    dict(label="A.", text="【Janet's Schedule】\nMon. July 2　My birthday\nTues. July 3　English class\nWed. July 4　Basketball game\nThurs. July 5　Betty's birthday\nFri. July 6　Sam's concert\nSat. July 7　Linda's welcome party\n【字詞】schedule 行程表", items=[
      M("When is Janet's birthday?", "It's on a Tuesday in July.|It's on the second day of July.|It's on the second Monday of July.|It's on the day before Betty's birthday.", "B"),
      M(BX.format("Bill: Janet, are you ready for the basketball game?<br>Janet: Yes. I can't wait. Let's play.") + "What's the date today?", "July 4.|July 5.|July 6.|July 7.", "A"),
      M("Today is July 6. Which is true?（何者為真？）", "Today is Wednesday.|Janet is in English class.|Janet can see Sam today.|Today is Betty's birthday.", "C"),
    ]),
    dict(label="B.", text="Hi, my name is Victor. Beth is my sister. She is the first child in my family. She is tall and beautiful, and she is nice to everyone. It's June 10 today. Beth's birthday is in two days. Look! These tickets are my gift for her. We're going to Adam Q's concert together. He's our favorite singer. I can't wait for her birthday.\n【字詞】child 小孩　in 在…之後　ticket 票", items=[
      M("What's the date today?", "It's July 10.|It's the tenth of June.|It's July 12.|It's the twenty-second of June.", "B"),
      M("What are the tickets for?", "Victor's party.|A museum.|Adam Q's concert.|Beth's birthday party.", "C"),
      M("Which is NOT true?（何者為非？）", "Beth is nice to Victor.|Victor is Beth's big brother.|Beth is a tall and beautiful person.|Adam Q is Beth's favorite singer.", "B"),
    ]),
  ]),
  dict(type="guided", title="六、依提示作答", meta="每題3分，共9分", items=[
    G("What's the date today?", "（以十一月十二日回答；日期用序數拼寫）", "It's November twelfth. / It is November twelfth. / It's the twelfth of November."),
    G("The baseball game is <u>on May 27</u>.", "（依畫線部分造原問句）", "When is the baseball game? / When's the baseball game?"),
    G("When is the dinner party?", "（以二月的第三個星期六回答）", "It's on the third Saturday of February. / It is on the third Saturday of February."),
  ]),
  dict(type="translation", title="七、翻譯", meta="每題3分，共9分", items=[
    T("她的生日是聖誕節前一天。", "Her birthday is the day before Christmas. / Her birthday is on the day before Christmas."),
    T("元旦是個重要的一天。", "New Year's Day is an important day."),
    T("讓我們致上我們的感謝。", "Let's give our thanks."),
  ]),
]
