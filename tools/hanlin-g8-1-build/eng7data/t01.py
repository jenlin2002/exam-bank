META = dict(n=1, h1="第1回・Starter Unit", subtitle="Starter Unit")
I = "images/test1/"
CROPS = [("p1",1,(630,1140,740,1288)), ("p2",1,(626,1292,748,1442)), ("p3",1,(626,1462,780,1602)), ("tree",2,(645,490,1102,842))]
BOX = '<div style="background:#fff;border:1px solid var(--paper-line);border-radius:8px;padding:10px 14px;font-style:italic;margin-bottom:8px;">{}</div>'
SECTIONS = [
  dict(type="vocab", title="一、依例轉換大小寫", meta="【A部分 基礎題】每題1分，共4分・例：bdinw → BDINW（大小寫要正確）", items=[
    dict(q="AGLQU →", answer="aglqu", exact=True), dict(q="ckptx →", answer="CKPTX", exact=True),
    dict(q="EORSV →", answer="eorsv", exact=True), dict(q="fhjmz →", answer="FHJMZ", exact=True),
  ]),
  dict(type="guided-multi", title="二、挑錯並改正", meta="每題2分，共8分・先填錯誤的編號（可打 1、2、3），再寫出正確的寫法", items=[
    dict(zh="My names Jim.　（① My　② names　③ Jim）", lines=["錯誤編號：{{②/2}}　改正為：{{name's}}"]),
    dict(zh="Good evening, yvonne.　（① Good　② evening　③ yvonne）", lines=["錯誤編號：{{③/3}}　改正為：{{Yvonne}}"]),
    dict(zh="No, he's not anurse.　（① No　② he's　③ not　④ anurse）", lines=["錯誤編號：{{④/4}}　改正為：{{a nurse}}"]),
    dict(zh="its her bag.　（① its　② her　③ bag）", lines=["錯誤編號：{{①/1}}　改正為：{{It's}}"]),
  ]),
  dict(type="vocab", title="三、寫出下列數字的讀法", meta="每題1分，共4分", items=[
    dict(q="50 →", answer="fifty"), dict(q="26 →", answer="twenty-six"), dict(q="47 →", answer="forty-seven"), dict(q="93 →", answer="ninety-three"),
  ]),
  dict(type="vocab", title="四、文意字彙", meta="每題1分，共5分", items=[
    dict(q="Two and six is e___t.", answer="eight"),
    dict(q="One minus（減去）one is z___o.", answer="zero"),
    dict(q="A: W___t is her name? B: It's Phoebe Derry.", answer="What"),
    dict(q="A: Where's my watch? B: Y___r watch is on the desk.", answer="Your"),
    dict(q="A: Mr. and Mrs. Cox are next to a red car. Is it t___r car? B: No, it's not. It's my car.", answer="their"),
  ]),
  dict(type="mc", title="五、文法選擇", meta="每題2分，共22分", items=[
    dict(q="This dog is small. ___ name is Alita.", options=["It","Its","It's","It is"], correct=1),
    dict(q="Vivian is my sister. ___ a good girl.", options=["I'm","He's","She's","You're"], correct=2),
    dict(q="A: What's ___ name? B: ___ Ella.", options=["you're; I'm","you're; Your","your; You're","your; I'm"], correct=3),
    dict(q="You are ___ daughter（女兒）. She is your mother.", options=["its","not","her","your"], correct=2),
    dict(q="He ___ a teacher, and I ___ a nurse.", options=["am; are","am; is","are; am","is; am"], correct=3),
    dict(q="That boy is Amy's friend. ___ is Kevin.", options=["He's","His","His name","His name's"], correct=2),
    dict(q="___ is ___ good friend.", options=["His; her","He; she","His; she","He; her"], correct=3),
    dict(q="A: ___ your grandma? B: She's OK. Thank you.", options=["How","Where","How's","Where's"], correct=2),
    dict(q="A: ___, my name's Isabelle. And your name? B: Hi, Isabelle. I'm Dave.", options=["Hello","Bye","Thanks","Good night"], correct=0),
    dict(q="A: ___ he your brother? B: Yes. I'm ___ sister.", options=["Is; her","Is; his","Are; my","Are; your"], correct=1),
    dict(q="A: ___ is Miss Hall? B: She is thirty-one.", options=["How","What","Where","How old"], correct=3),
  ]),
  dict(type="mc", title="六、對話選擇", meta="每題2分，共8分", items=[
    dict(q="A: ___ B: I'm ten.", options=["How are you, Ian?","What's your name?","How old are you, Ian?","What's on the desk, Ian?"], correct=2),
    dict(q="A: Your cat is cute（可愛的）. ___ B: Leo.", options=["How is it?","Where is it?","How old is it?","What's its name?"], correct=3),
    dict(q="A: What's your number? B: ___", options=["I'm number 5.","Hello, Christine.","It's under the chair.","Hi, I'm Jenny Humphrey."], correct=0),
    dict(q="A: Hello. I'm Leo. What's your name? B: Hi. ___", options=["You're Leo.","I am a student.","My name's Sara.","I'm fine. Thank you."], correct=2),
  ]),
  dict(type="guided-multi", title="七、看圖填入正確的人稱代名詞或代名詞所有格", meta="每格1分，共7分", items=[
    dict(zh="", image=I+"p1.png", lines=["{{She}} is Doris. {{Her}} phone number is 2257-3388."]),
    dict(zh="", image=I+"p2.png", lines=["Hi, I'm Eric. Look at this boy. {{He}} is {{my}} brother. {{His}} name is Andy."]),
    dict(zh="", image=I+"p3.png", lines=["Look at the picture. Tim and Emma are brother and sister, and Brad is {{their}} father. {{They}} are a happy family（家庭）."]),
  ]),
  dict(type="guided", title="八、依提示作答", meta="每題2分，共4分", items=[
    dict(prompt="Her student number is <u>89</u>.", hint="（依畫線部分造原問句）", answer="What is / What's her student number?"),
    dict(prompt="His name is Mark.", hint="（以 he 為首改寫）", answer="He is Mark."),
  ]),
  dict(type="guided", title="九、重組", meta="每題2分，共6分", items=[
    dict(prompt="name / What / her / is / ?", hint="（重組句子）", answer="What is her name?"),
    dict(prompt="grandpa / How old / their / is / ?", hint="（重組句子）", answer="How old is their grandpa?"),
    dict(prompt="friend / You're / good / my / .", hint="（重組句子）", answer="You're my good friend."),
  ]),
  dict(type="translation", title="十、整句式翻譯", meta="每題2分，共6分（A、B 兩句寫在同一格，例：A: … B: …）", items=[
    dict(zh="A：你叫什麼名字？B：我是 Lisa。", answer="A: What's your name? B: I'm Lisa. / A: What's your name? B: My name is Lisa."),
    dict(zh="A：你幾歲？B：我十歲。（請用英文寫出數字）", answer="A: How old are you? B: I am ten. / A: How old are you? B: I'm ten."),
    dict(zh="A：我們的外婆幾歲？B：她八十三歲。（請用英文寫出數字）", answer="A: How old is our grandma? B: She is eighty-three. / A: How old is our grandmother? B: She's eighty-three."),
  ]),
  dict(type="mc", title="一、單題", meta="【B部分 活用題】每題2分，共10分", items=[
    dict(q="A: Hi! ___ What's your name? B: I'm Mike.", options=["I'm Jay.","Good-bye.","How is Mike?","You are Ted."], correct=0),
    dict(q="A: How old are they? B: ___", options=["They are Nicole and Zac.","They're brother and sister.","They are fine. Thank you.","The girl is 15, and the boy is 17."], correct=3),
    dict(q="Which sentence is correct?（哪一個句子是正確的？）", options=["How areyou, Jade?","She is Serena Brown.","Good morning, patty.","Good bye, Snow White。"], correct=1),
    dict(q="A: Hello! I'm Doc. B: ___", options=["Hello! You're Doc.","Hi! My name's Doc.","Hello! Snow White.","Hi! I'm Snow White."], correct=3),
    dict(q="A: Hello, I'm Ruby. And you? B: ___", options=["Angel Clark.","I'm twelve.","She's Amy Lee.","Your name is Wendy."], correct=0),
  ]),
  dict(type="cloze", title="二、克漏字選擇", meta="每題2分，共8分",
    passage="Sneezy: Hello, ___1___. What's your name?\nBunny: Hi, ___2___. My name's Bunny.\nSneezy: Nice to meet you, Bunny.\nBunny: Nice to meet you, too, Sneezy.\nSneezy: Bunny, who's that tall boy?\nBunny: Oh, he is my friend. ___3___\nSneezy: Wow! It's a good name.\nBunny: Yes, ___4___.\n\n【字詞】Nice to meet you. 很高興認識你。　too 也",
    items=[
      dict(options=["Sneezy","I'm Sneezy","I am Bunny","you are Sneezy"], correct=1),
      dict(options=["Sneezy","I'm Bunny","you're Sneezy","I'm nineteen"], correct=0),
      dict(options=["You are Happy.","Her name's Happy.","His name is Happy.","My name is Happy."], correct=2),
      dict(options=["I am","it is","he is","you are"], correct=1),
  ]),
  dict(type="reading", title="三、依下列圖表選出適當的答案", meta="每題2分，共8分", passages=[
    dict(label="", text="", image=I+"tree.png", items=[
      dict(q="He is Lucy's brother. What is his name?", options=["Tom.","Jeff.","Bill.","Chris."], correct=1),
      dict(q="How old is Alex's grandmother?", options=["She is forty-five.","She is fifty.","She is seventy-two.","She is seventy-four."], correct=3),
      dict(q="Which is correct?（哪一個是正確的？）", options=["Bill is Chris's father.","Peggy is Jeff's mother.","Chris is Alex's brother.","Tom is Jill's grandfather."], correct=1),
      dict(q=BOX.format("A: How old is your grandfather?<br>B: He's seventy-two.<br>A: And your father?<br>B: He's forty-two.") + "B is ___.", options=["Jeff","Bill","Chris","Alex"], correct=2),
    ]),
  ]),
]
