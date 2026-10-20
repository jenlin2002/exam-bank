# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEF".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=3, h1="第3回・Unit 2", subtitle="Where Are My Pencils?")
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共20分", items=[
    V("A: Welcome to my home, Bill. Come in. B: Wow! Your h___e is big.", "house"),
    V("A: Oh, I am h___y. B: Here. Have an apple. A: Thank you.", "hungry"),
    V("Your notebook is in the l___g room, near the TV.", "living"),
    V("A: Where is the park? B: It is b___n the zoo and the school.", "between"),
    V("A: Brad, who are those p___e? B: They are our new classmates.", "people"),
    V("A: Look at the picture. They are my p___ts. B: Wow! Your father is tall, and your mother is beautiful.", "parents"),
    V("The car is small. It's not big e___h for a family of four.", "enough"),
    V("A: Oh, my eraser is not on the desk. B: M___e it is in your bag. I'm not sure（確定的）.", "Maybe"),
    V("The boy is shy（害羞的）. He is b___d his mother.", "behind"),
    V("A: Where's the white table? It's not in the kitchen. B: Ah, it's i___e Peter's room.", "inside"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共26分", items=[
    M("A: ___ are you, Amy? B: I am in the bathroom.", "What|Who|Where|How", "C"),
    M("My brothers aren't home. They are ___ the park.", "of|on|at|for", "C"),
    M("A: Look! What are ___? B: They are pens.", "that|this|pens|those", "D"),
    M("Look! Your markers ___ on the desk.", "are|is|be|am", "A"),
    M("A: Is Dad ___ the kitchen? B: No, he isn't.", "in|to|with|between", "A"),
    M("A: Isn't this picture beautiful? B: Yes. It ___.", "isn't|really|is really|really is", "D"),
    M("A: ___ Lucky? B: He's behind the door.", "Who's|What's|Where's|How's", "C"),
    M("The bus is ___ of our school.", "near|in|in front|next", "C"),
    M("My jump rope is black, but Tina's jump rope ___.", "is|isn't|are|aren't", "B"),
    M("A: Where's my bird, Kiki? B: Look up! It's right ___ you.", "to|on|of|above", "D"),
    M("A: Hey, are these your erasers? B: Yes, ___.", "they are|they're|that is|they aren't", "A"),
    M("___ are my pencils, and ___ are your pencils.", "These; that|These; those|This; that|This; those", "B"),
    M("A: Are ___ dolls? B: No. ___ pencil cases.", "those; They're|these; It's|that; That is|they; They aren't", "A"),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共8分", items=[
    M("A: ___ B: It's under the table.", "What is that?|Who is it?|Where is it?|Is it in the box?", "C"),
    M("A: Hi, Alex. B: Welcome, Nancy. ___", "Good-bye.|Come meet my wife.|We're fine.|Where are you?", "B"),
    M("A: ___ B: They are my rulers.", "Is this your ruler?|What's that?|Where are your rulers?|What are those?", "D"),
    M("A: Molly isn't home. B: ___ She's a workaholic（工作狂）.", "Where is her house?|Is she in her house?|Maybe she's at her office.|Her office is next to my house.", "C"),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="每題2分，共12分",
    passage="Ben: Is Mom home?\nZoe: No, ___1___.\nBen: Where is she?\nZoe: She's ___2___ Aunt Lisa's house.\nBen: I see. Hey, what are these?\nZoe: ___3___ are notebooks from Amy.\nBen: What are the notebooks ___4___?\nZoe: My birthday. They are a ___5___.\nBen: They are all purple.\nZoe: Yes. ___6___ I love the notebooks.\n\n【字詞】birthday 生日　all 全部　love 喜愛",
    items=[
      dict(options=["is not", "she is", "she's", "she isn't"], correct=3),
      dict(options=["on", "at", "to", "of"], correct=1),
      dict(options=["We", "That", "It", "They"], correct=3),
      dict(options=["to", "of", "for", "at"], correct=2),
      dict(options=["gift", "wall", "person", "number"], correct=0),
      dict(options=["Amy isn't a good girl.", "Purple is my favorite color.", "They are right next to each other.", "What's the color of your notebooks?"], correct=1),
  ]),
  dict(type="reading", title="五、閱讀測驗", meta="每題2分，共16分", passages=[
    dict(label="A.", text="Miss Smith has a new house. The house is behind the school and next to the park. Her house is small and white. Her sofa, table, and chairs are white. The walls in the rooms are white, too. Max, the black cat, is her good friend. His bed is the red box next to the door. Miss Smith's house is not big, but it is enough for Miss Smith and her cat. She is happy with her new house.\n【字詞】has 有", items=[
      M("Where is Miss Smith's new house?", "It's behind the park.|It's next to the park.|It's next to the school.|It's between the park and the school.", "B"),
      M("What may be（可能是）Miss Smith's favorite color?", "Black.|White.|Red.|Green.", "B"),
      M("Which is NOT true?（何者為非？）", "Miss Smith and Max are good friends.|The box next to the door is Max's bed.|The house is big enough for Miss Smith.|The walls are white, but the table and chairs aren't.", "D"),
    ]),
    dict(label="B.", text="Lynn: Wow! Your bedroom is big and blue. It is beautiful.\nRick: Thanks. This is my bed, and my brother's bed is next to the desk.\nLynn: Hey, what's the yellow and black thing on the desk? Is it a toy car?\nRick: ______ It is Bumblebee, my new pencil case.\nLynn: That's very special. And what's that on your brother's bed?\nRick: The green box? It's my brother's cookie box. Cookies are his favorite snack.\n【字詞】thing 東西　toy 玩具　snack 點心", items=[
      M("Where is Lynn?", "At home.|At school.|In Rick's house.|In her bedroom.", "C"),
      M("What is Bumblebee?", "It's a toy car.|It's a desk.|It's a box.|It's a pencil case.", "D"),
      M("What is most likely（最有可能）inside the green box?", "A toy car.|A gift.|Cookies.|Pencils.", "C"),
      M("Which（哪一個）is good for the blank（空格）?", "Yes, it's on the desk.|Yes. It's my favorite.|No, it's not a toy car.|No. It's not yellow and black.", "C"),
      M("Which is true?（何者為真？）", "Rick's bedroom is green.|Rick's toy car is on the desk.|The desk is next to Rick's bed.|Rick's bedroom is his brother's bedroom too.", "D"),
    ]),
  ]),
  dict(type="guided", title="六、依提示作答", meta="每題3分，共9分", items=[
    G("Jim and Dave's father is <u>in the kitchen</u>.", "（依畫線部分造原問句）", "Where is Jim and Dave's father? / Where's Jim and Dave's father?"),
    G("She is a housewife.", "（主詞用 they 改寫）", "They are housewives. / They're housewives."),
    G("Tom's sofa is gray. / Jerry's sofa isn't gray.", "（用 but 合併兩句）", "Tom's sofa is gray, but Jerry's sofa isn't. / Tom's sofa is gray, but Jerry's sofa isn't gray. / Tom's sofa is gray, but Jerry's sofa is not gray."),
  ]),
  dict(type="translation", title="七、翻譯", meta="每題3分，共9分（A、B 兩句寫在同一格，例：A: … B: …）", items=[
    T("A：那些女人在哪裡？B：在飯廳。", "A: Where are those women? B: In the dining room. / A: Where are those women? B: They are in the dining room."),
    T("客廳、浴室和臥室就在彼此的旁邊。", "The living room, the bathroom, and the bedroom are right next to each other. / The living room, bathroom, and bedroom are right next to each other."),
    T("A：這張咖啡色的桌子不是你的最愛嗎？B：對，它是。", "A: Isn't the brown table your favorite? B: Yes, it is. / A: Isn't this brown table your favorite? B: Yes, it is."),
  ]),
]
