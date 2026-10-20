# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEFG".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=1, h1="第1回・Starter Unit", subtitle="Starter Unit")
I = "images/test1/"
CROPS = [P(f"pair{i+1}", 1, 88, y0, 392, y0 + 76) for i, y0 in enumerate([402, 480, 558, 636])]
PIC = '<img src="' + I + 'pair{}.png" alt="題目附圖" style="width:100%;max-width:420px;display:block;margin:4px 0;border-radius:8px;">'
LR = "左圖|右圖"
SECTIONS = [
  dict(type="vocab", title="一、依照字母順序寫出空格所缺少的大寫或小寫字母", meta="每個字母0.5分，共6分・依序寫出兩個缺少的字母，例：w ＿ ＿ z → xy（大小寫要正確）", items=[
    V("w ＿ ＿ z →", "xy", exact=True), V("＿ H I ＿ →", "GJ", exact=True), V("＿ c ＿ e →", "bd", exact=True),
    V("＿ M ＿ O →", "LN", exact=True), V("＿ T ＿ V →", "SU", exact=True), V("p ＿ ＿ s →", "qr", exact=True),
  ]),
  dict(type="vocab", title="二、將下列單字大寫改小寫，小寫改大寫", meta="每題1分，共6分（大小寫要正確）", items=[
    V("LEMON →", "lemon", exact=True), V("work →", "WORK", exact=True), V("happy →", "HAPPY", exact=True),
    V("BRIDGE →", "bridge", exact=True), V("quiet →", "QUIET", exact=True), V("CALENDAR →", "calendar", exact=True),
  ]),
  dict(type="mc", title="三、勾選出符合描述的圖片", meta="每題2分，共8分", items=[
    M(PIC.format(1) + "She is my teacher.", LR, "A"),
    M(PIC.format(2) + "They are Mr. and Mrs. Lee.", LR, "A"),
    M(PIC.format(3) + "A: How old is he? B: He is seventy-five.", LR, "B"),
    M(PIC.format(4) + "A: How old are you? B: I'm thirty.", LR, "B"),
  ]),
  dict(type="vocab", title="四、將下列數字以英文拼出", meta="每題1分，共6分", items=[
    V("18 =", "eighteen"), V("20 =", "twenty"), V("4 =", "four"), V("11 =", "eleven"), V("40 =", "forty"), V("39 =", "thirty-nine"),
  ]),
  dict(type="vocab", title="五、寫出下列人稱代名詞的所有格", meta="每題1分，共6分", items=[
    V("it →", "its"), V("you →", "your"), V("she →", "her"), V("he →", "his"), V("I →", "my"), V("we →", "our"),
  ]),
  dict(type="vocab", title="六、依例寫出下列「人稱代名詞＋be 動詞」的縮寫式", meta="每題1分，共5分・例：he → he's", items=[
    V("you →", "you're"), V("it →", "it's"), V("she →", "she's"), V("I →", "I'm"), V("we →", "we're"),
  ]),
  dict(type="guided-multi", title="七、依句意完成填空", meta="每格2分，共12分", items=[
    GM("", "A: Hi. I {{am}} Toby. And you? B: Ryan."),
    GM("", "A: How are you? B: We {{are}} fine, thank you."),
    GM("", "A: {{What's/What is}} your name? B: {{My}} name is Betty."),
    GM("", "A: How {{old}} are Mia and Joe? B: {{They're/They are}} thirty-two."),
  ]),
  dict(type="mc", title="八、文法選擇", meta="每題2分，共22分", items=[
    M("They ___ Amy and Jack.", "am|are|is|×", "B"),
    M("___ your book.", "It|It's|Its|Is", "B"),
    M("___ is my sister. Her name is Emily.", "She|She's|Her|His", "A"),
    M("Vincent is ___ father.", "Ben and Ivy|they|they're|their", "D"),
    M("He is my brother. ___ name is Mike.", "His|He's|He is|He", "A"),
    M("A: ___ his name? B: Dennis.", "What|How|What's|How's", "C"),
    M("A: How ___ your mother? B: She ___ fine, thanks.", "are; is|is; are|are; are|is; is", "D"),
    M("A: ___ you? B: I am nine.", "How are|How old are|How is|How old is", "B"),
    M("A: What is ___ name? B: My name is Cody.", "my|you|your|you're", "C"),
    M("It is her cat. ___ name is Fluffy.", "It|Its|It's|It is", "B"),
    M("___ grandmother is seventy-three.", "We're|Our|She|She is", "B"),
  ]),
  dict(type="mc", title="九、對話選擇", meta="每題2分，共4分", items=[
    M("A: ___ B: I'm Jane.", "Hello, Jane.|How are you?|Bye, Jane.|What's your name?", "D"),
    M("A: How old is Jason? B: ___", "He's fine.|He's Jason.|He's seven.|He's my brother.", "C"),
  ]),
  dict(type="guided-multi", title="十、選出錯誤並改正", meta="每題2分，共10分・先填錯誤處的代號（A、B、C），再寫出正確的寫法", items=[
    GM("", "<u>Heis</u>(A) not <u>my</u>(B) <u>brother</u>(C).", "錯誤處：{{A}}　改正為：{{He is/He's}}"),
    GM("", "A: <u>how's</u>(A) your mom<u>?</u>(B) B: <u>She's</u>(C) fine.", "錯誤處：{{A}}　改正為：{{How's}}"),
    GM("", "What <u>is</u>(A) <u>its</u>(B) name<u>.</u>(C)", "錯誤處：{{C}}　改正為：{{?}}"),
    GM("", "<u>My</u>(A) name <u>is</u>(B) <u>william</u>(C).", "錯誤處：{{C}}　改正為：{{William}}"),
    GM("", "<u>She</u>(A) is twelve, and <u>i</u>(B) am eleven<u>.</u>(C)", "錯誤處：{{B}}　改正為：{{I}}"),
  ]),
  dict(type="guided", title="十一、依提示作答", meta="每題3分，共9分", items=[
    G("She is Brittany.", "（用 Her... 改寫）", "Her name is Brittany."),
    G("How old is your dad?", "（用 51 歲回答）", "My dad is fifty-one. / He is fifty-one. / He's fifty-one. / My dad's fifty-one."),
    G("His name is <u>Mike</u>.", "（依畫線部分造原問句）", "What is his name? / What's his name?"),
  ]),
  dict(type="translation", title="十二、翻譯", meta="每題2分，共6分", items=[
    T("Gary 幾歲？", "How old is Gary?"),
    T("他是 Kevin。", "He is Kevin. / He's Kevin."),
    T("他們的爺爺 66 歲。", "Their grandpa is sixty-six. / Their grandfather is sixty-six."),
  ]),
]
