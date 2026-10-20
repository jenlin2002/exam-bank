# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEFG".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=6, h1="第6回・Unit 3", subtitle="Open the Magic Door")
I = "images/test6/"
CROPS = [P("signs", 12, 403, 604, 715, 676)]
IMG = '<br><img src="' + I + '{}" alt="題目附圖" style="width:100%;max-width:480px;display:block;margin:6px 0;border-radius:8px;">'
BX = '<div style="border:1px solid var(--paper-line);border-radius:6px;padding:4px 8px;margin:2px 0;">{}</div>'
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共20分", items=[
    V("Students! Don't talk; be q___t.", "quiet"),
    V("Boys and girls, f___w me to Room D now. Let's go.", "follow"),
    V("A: Can I read your comic books? B: S___re. They are on my desk.", "Sure"),
    V("Be c___l of Arthur. He is not a good person.", "careful"),
    V("We can see m___y beautiful pictures in the museum.", "many"),
    V("Go w___sh your hands now. They are dirty（髒的）.", "wash"),
    V("It's t___e for bed. Please go to sleep now.", "time"),
    V("A: Who are the m___n in the car? B: They are my uncle, father, and brother.", "men"),
    V("A: Let's play basketball at the park a___r class this afternoon. B: Okay.", "after"),
    V("A: Can't you see the s___n on the wall? You can't eat or drink here. B: Oh, sorry.", "sign"),
  ]),
  dict(type="mc", title="二、選擇", meta="每題2分，共20分", items=[
    M("Look at ___. Who are they?", "them|they|their|they're", "A"),
    M("A: ___ draw on the desk, Betty. B: Sorry.", "No|Not|Don't|Isn't", "C"),
    M("A: Nick, ___ nice to your cousins. B: OK.", "are|is|be|do", "C"),
    M("Look. It's Sandy. Let's ___ hello to her.", "say|can say|don't say|can't say", "A"),
    M("Hey, let's ___ run in the museum. It's not safe.", "no|aren't|don't|not", "D"),
    M("Please ___ sad.", "not|don't be|no|don't", "B"),
    M("A: Let's play basketball at school. B: Sorry, I ___.", "am not|can't play|not play|can't", "D"),
    M("A: Can you wake ___ up at six o'clock（6點）, please? B: Yes, I can do that.", "our|us|we|we're", "B"),
    M("___ this phone, you can open this door.", "From|Of|To|With", "D"),
    M("You can talk to Julie ___ Mike. They are nice people.", "or|but|too|for", "A"),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共6分", items=[
    M("A: ___ Time for class. B: Oh my! Wait for me.", "Hurry!|Be careful!|Can you see me?|You can open your book.", "A"),
    M("A: Wecome to my home. ___ B: Thank you.", "Don't eat here.|Please come in.|Let's go to the park.|Don't go to the museum.", "B"),
    M("A: I'm hungry. B: I'm hungry, too. ___ A: No, we can't.", "Don't eat here.|Listen, please.|Can we eat now?|Let's not eat the eggs.", "C"),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="每題2分，共12分",
    passage="Hi, students. I'm Mr. Barns. Welcome to my magic class. These are my class rules.\na. Listen to ___1___ in class.\nb. Don't eat ___2___ sleep in class.\nc. ___3___ your phone. Please don't use it in class.\nd. Be careful—don't put spells on your classmates. That's not ___4___.\nPlease ___5___ these rules, and we ___6___ have fun with magic.\n\n【字詞】put spells on... 對…施咒語　have fun 玩得愉快",
    items=[
      dict(options=["I", "we", "me", "my"], correct=2),
      dict(options=["×", "or", "but", "and"], correct=1),
      dict(options=["Look at", "Wait for", "Turn off", "Sing with"], correct=2),
      dict(options=["safe", "quiet", "magic", "special"], correct=0),
      dict(options=["use", "wash", "hurry", "follow"], correct=3),
      dict(options=["are", "can", "can't", "be"], correct=1),
  ]),
  dict(type="guided", title="五、依提示作答", meta="每題3分，共12分", items=[
    G("You can eat <u>the apples</u>.", "（將畫線部分改為代名詞）", "You can eat them."),
    G("The girl can't read. / The girl can't write.", "（合併句子）", "The girl can't read or write. / The girl cannot read or write."),
    G("Let's watch TV now.", "（改為否定句）", "Let's not watch TV now."),
    G("Sam, open your book.", "（句尾加上 please 改寫）", "Sam, open your book, please."),
  ]),
  dict(type="translation", title="六、翻譯", meta="每題3分，共9分（A、B 兩句寫在同一格，例：A: … B: …）", items=[
    T("我們不要相互爭吵了。", "Let's not fight with each other."),
    T("請等待輪到你的時候。", "Wait for your turn, please. / Please wait for your turn."),
    T("A：我可以跟 Jim 去博物館嗎？B：可以，你可以去。", "A: Can I go to the museum with Jim? B: Sure. / A: Can I go to the museum with Jim? B: Yes, you can. / A: Can I go to the museum with Jim? B: Yes, you can go. / A: Can I go to the museum with Jim? B: Sure, you can."),
  ]),
  dict(type="reading", title="七、閱讀測驗", meta="每題3分，共21分", passages=[
    dict(label="A.", text="(On the phone)\nTanya: Hello, Miffy. Where are you?\nMiffy: I'm at home with Barky.\nTanya: Let's go to Mr. Smith's Kitchen for dinner. Barky can come with us.\nMiffy: Can dogs go to Mr. Smith's Kitchen? Nice! Can Nila go, too?\nTanya: Well, dogs are welcome in Mr. Smith's Kitchen, but cats aren't welcome there. \"No cats\" is Mr. Smith's only rule. He is allergic to cats.\nMiffy: Ah, I see.\n【字詞】dinner 晚餐　only 唯一的　allergic 過敏的", items=[
      M("Where is Miffy?", "She's at home.|She's with Tanya.|She's at Mr. Smith's house.|She's at Mr. Smith's Kitchen.", "A"),
      M("Which is true?", "Nila is a dog.|Barky is a cat.|Nila can go to Mr. Smith's Kitchen.|Barky can go to Mr. Smith's Kitchen.", "D"),
      M("Which sign can people see at Mr. Smith's Kitchen?" + IMG.format("signs.png"), "(A)|(B)|(C)|(D)", "A"),
    ]),
    dict(label="B.", text="1. Do not run.\n2. Do not sleep.\n3. Do not eat or drink.\n4. Do not use your phone.\n5. Don't speak Chinese; speak English.\n6. Wait for your turn in games.\n7. Raise your hand, and you can talk.\n【字詞】speak 說　Chinese 中文　English 英語　raise 舉起　break 違反", items=[
      M("Where can you see these rules?", "At a zoo.|In class.|At an office.|On a farm.", "B"),
      M("Jane is hungry, but she can't have her cookies. What rule CAN'T Jane break?", "Rule 1.|Rule 2.|Rule 3.|Rule 7.", "C"),
      M(BX.format("Mr. Li: David, hands down. It's Mia's turn.<br>David: Sorry.") + "What is the rule?", "Rule 4.|Rule 5.|Rule 6.|Rule 7.", "C"),
      M(BX.format("Mr. Li: Becky, no Chinese now. And turn off your phone. Please follow <u>the rules</u>.<br>Becky: Okay, sorry.") + "What are <u>the rules</u>?", "Rules 2 and 4.|Rules 3 and 6.|Rules 4 and 5.|Rules 5 and 6.", "C"),
    ]),
  ]),
]
