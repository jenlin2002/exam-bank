# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEF".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)

META = dict(n=1, h1="第1回・Starter Unit", subtitle="Starter Unit")
I = "images/test1/"
CROPS = [P("desk", 1, 216, 336, 450, 472)]
SECTIONS = [
  dict(type="vocab", title="一、將以下單字做大小寫互換", meta="每題1分，共6分・例：MILK → milk（大小寫要正確）", items=[
    V("change →", "CHANGE", exact=True), V("BOARD →", "board", exact=True), V("prize →", "PRIZE", exact=True),
    V("VINEGAR →", "vinegar", exact=True), V("sixty →", "SIXTY", exact=True), V("JUICE →", "juice", exact=True),
  ]),
  dict(type="vocab", title="二、拼寫出下列數字的英文", meta="每題1分，共6分", items=[
    V("0 →", "zero"), V("3 →", "three"), V("16 →", "sixteen"), V("42 →", "forty-two"), V("56 →", "fifty-six"), V("97 →", "ninety-seven"),
  ]),
  dict(type="vocab", title="三、看圖填入單字", meta="每題1分，共6分・依圖中編號①～⑥寫出物品的英文", image=I+"desk.png", items=[
    V("① (d)___", "desk"), V("② (e)___", "eraser"), V("③", "pencil"), V("④", "clock"), V("⑤", "ruler"), V("⑥", "book"),
  ]),
  dict(type="guided-multi", title="四、依例填空", meta="每格1分，共8分・例：She is Nina. = Her name is Nina.", items=[
    GM("", "You {{are}} Steve. = {{Your}} name is Steve."),
    GM("", "I {{am}} Penny. = {{My}} name is Penny."),
    GM("", "He {{is}} Brian. = {{His}} name is Brian."),
    GM("", "It {{is}} Coco. = {{Its}} name is Coco."),
  ]),
  dict(type="mc", title="五、文法選擇", meta="每題2分，共22分", items=[
    M("A: How old are you and Bob? B: ___ are thirteen.", "I|You|We|You and Bob", "C"),
    M("A: What's ___ name? B: I'm Zoe.", "my|you|your|you're", "C"),
    M("That boy's name ___ Matt.", "×|is|am|are", "B"),
    M("They ___ Maggie and Tyler.", "×|is|am|are", "D"),
    M("A: How's your dad? B: ___ fine.", "He's|I'm|You're|His", "A"),
    M("___ is my friend. ___ name's Mark.", "He; He's|His; His|He's; Its|He; His", "D"),
    M("Look! This is ___ pen.", "Amy|she|her|she's", "C"),
    M("A: James ___ my name. B: Hi, James.", "am|is|are|×", "B"),
    M("A: What's Diane's phone number? B: ___ 2274-0504.", "She's|Her|It's|Its", "C"),
    M("___ my sister. ___ Ruby.", "She's; Her|She's; She's|Her; She's|Her; Her", "B"),
    M("Jack and Jill are brother and sister. ___ father is Mr. Lee.", "Their|They|They're|That's", "A"),
  ]),
  dict(type="mc", title="六、對話選擇", meta="每題2分，共10分", items=[
    M("A: ___ That is a rabbit. B: It is cute（可愛的）.", "Look!|Listen!|Come!|Go!", "A"),
    M("A: ___ B: Hi, Judy. I'm Leo.", "How are you?|Good morning, Leo.|Good evening. How is Leo?|Hi, I'm Judy. What's your name?", "D"),
    M("A: What's that girl's name? B: ___", "I am Betty.|She's Betty.|She's your sister.|Your name's Betty.", "B"),
    M("A: ___ B: It's one-one-two-eight.", "How is it?|What's your name?|How old are you?|What's your student number?", "D"),
    M("A: ___, Andy? B: Two. She's young（年輕的）.", "How is your grandma|What is her name|How old is your sister|What is your mom's phone number", "C"),
  ]),
  dict(type="cloze", title="七、克漏字選擇", meta="每題2分，共12分",
    passage="Jane: Hello, ___1___ Jane. ___2___ your name?\nGeorge: ___3___, Jane. My ___4___ George.\nJane: This is my brother. ___5___ name is Leo.\nGeorge: ___6___, Leo?\nLeo: Fine.",
    items=[
      dict(options=["I'm", "he's", "my", "you're"], correct=0),
      dict(options=["Who", "What", "How's", "What's"], correct=3),
      dict(options=["Goodbye", "Sorry", "Hi", "Go"], correct=2),
      dict(options=["name", "name's", "is", "be"], correct=1),
      dict(options=["He", "Her", "He's", "His"], correct=3),
      dict(options=["Stand up", "Good evening", "How are you", "What is your phone number"], correct=2),
  ]),
  dict(type="guided-multi", title="八、選出錯誤處並加以改正", meta="每題2分，共6分・先填錯誤處的代號（A、B、C），再寫出正確的寫法", items=[
    GM("", "<u>How</u>(A) <u>are</u>(B) you<u>.</u>(C)", "錯誤處：{{C}}　改正為：{{?}}"),
    GM("", "<u>Hi</u>(A), <u>My</u>(B) name is Patrick<u>.</u>(C)", "錯誤處：{{B}}　改正為：{{my}}"),
    GM("", "<u>Her</u>(A) <u>name</u>(B) is <u>sophie</u>(C).", "錯誤處：{{C}}　改正為：{{Sophie}}"),
  ]),
  dict(type="guided", title="九、重組句子", meta="每題2分，共6分", items=[
    G("my / is / Babe / dog / .", "（重組句子）", "Babe is my dog."),
    G("I / Laura / Hello / , / am / .", "（重組句子）", "Hello, I am Laura."),
    G("number / is / student / your / What / ?", "（重組句子）", "What is your student number?"),
  ]),
  dict(type="guided", title="十、依提示作答", meta="每題3分，共9分", items=[
    G("My name is Chris.", "（用 I... 改寫句子）", "I'm Chris. / I am Chris."),
    G("His name is <u>Lucas</u>.", "（依畫線部分造原問句）", "What's his name? / What is his name?"),
    G("How old are they?", "（以二十歲回答，數字需拼出）", "They are twenty. / They're twenty."),
  ]),
  dict(type="translation", title="十一、翻譯", meta="每題3分，共9分（A、B 兩句寫在同一格，例：A: … B: …）", items=[
    T("我的父親三十八歲。", "My dad is thirty-eight. / My father is thirty-eight."),
    T("A：你妹妹叫什麼名字？B：她的名字叫安（Ann）。", "A: What's your sister's name? B: Her name is Ann. / A: What's your sister's name? B: Her name's Ann. / A: What is your sister's name? B: Her name is Ann."),
    T("他是我的狗。他的名字叫洛基（Rocky）。", "It's my dog. Its name is Rocky. / He's my dog. His name is Rocky. / It is my dog. Its name is Rocky. / He is my dog. His name is Rocky."),
  ]),
]
