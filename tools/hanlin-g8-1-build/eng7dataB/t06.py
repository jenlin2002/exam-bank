# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEF".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=6, h1="第6回・Unit 3", subtitle="Open the Magic Door")
I = "images/test6/"
CROPS = [P("signs", 12, 84, 515, 640, 590)]
IMG = '<br><img src="' + I + '{}" alt="題目附圖" style="width:100%;max-width:560px;display:block;margin:6px 0;border-radius:8px;border:1px solid var(--paper-line);">'
BX = '<div style="border:1px solid var(--paper-line);border-radius:6px;padding:4px 8px;margin:2px 0;">{}</div>'
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共20分", items=[
    V("A: Look at that s___n. You can't stand there. B: OK.", "sign"),
    V("A: What is this p___e? B: It is a zoo.", "place"),
    V("Can you w___h the bag? It's very dirty（骯髒的）.", "wash"),
    V("A: Who are those m___n? B: They are my uncles.", "men"),
    V("Andy, Mike, don't f___t with each other. Calm down（冷靜）.", "fight"),
    V("A: What's that in the woman's h___d? B: She's holding（握著）an egg. She's a cook.", "hand"),
    V("Look! A big hole（洞）. Be ca___l.", "careful"),
    V("Don't play on the street（街道）. It's not s___e.", "safe"),
    V("It's t___e for bed. Go to sleep now.", "time"),
    V("A: Cory, p___e close the door for me. B: OK, Miss Lin.", "please"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共26分", items=[
    M("A: ___ sad, girls. B: But we can't help it（忍不住）.", "Not be|Can't|Don't be|Don't", "C"),
    M("A: Son, ___ thank Mr. Lee. B: Thank you, Mr. Lee.", "let|let it|let's|let you", "C"),
    M("A: ___ sit on your desk, Alex. B: Oh, sorry.", "Don't|No|Not|Don't be", "A"),
    M("A: ___ I watch TV, Mom? B: No, you can't.", "Am|Are|Isn't|Can", "D"),
    M("Mia, don't go now. Please wait ___ me.", "at|in|for|to", "C"),
    M("Let's ___ in front of the door. Let's go inside the house.", "stand|not stand|can't stand|or stand", "B"),
    M("A: ___ a good boy, Chris. B: Yes, Mrs. Wu.", "Is|Be|Do|Who's", "B"),
    M("The boy is behind that tall tree. I can't see ___.", "he|his|him|he's", "C"),
    M("Nancy can't be sleeping now. Please go and wake ___.", "up|her up|up her|the girls up", "B"),
    M("Boys, be quiet and listen ___ your mom.", "to|for|in|at", "A"),
    M("Here are some markers. You can draw ___ them.", "for|to|of|with", "D"),
    M("A: Let's go to Nina's house. B: Can my brother go with ___? A: Sure.", "I|we|us|our", "C"),
    M("A: Can we play games? B: No, you ___, but you ___ read books.", "can't; can|can't; can't|can; can't|can; can", "A"),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共8分", items=[
    M("A: ___, Jean. Time for school. B: Okay, Mom.", "Wake up|Stand there|What's this|Go to bed", "A"),
    M("A: Look! A monster（怪獸）! B: ___ Let's run.", "Sure.|Hurry!|Good-bye.|Wait.", "B"),
    M("A: Mom, can I play with your phone now, please? B: ___ It's still（仍然）your brother's time.", "I'm not sure.|Be nice to your brother.|I'm sad, too.|Wait for your turn, dear.", "D"),
    M("A: Shh! ___ We are in a museum. B: Sorry, Mr. Wang.", "Don't look.|Let's sing.|Be quiet.|Don't listen to them.", "C"),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="每題2分，共10分",
    passage="Happy School ___1___\n• ___2___ in the classroom.\n• Say \"hello\" and \"good morning\" to your teachers.\n• ___3___ nice to your classmates.\n• Do not fight ___4___ your classmates.\n• Do not shout ___5___ jump in class.\n\n【字詞】shout 喊叫",
    items=[
      dict(options=["Signs", "Times", "Rules", "Pictures"], correct=2),
      dict(options=["Don't run", "Turn off", "Don't follow", "Please open"], correct=0),
      dict(options=["Do", "Be", "Let's", "You're"], correct=1),
      dict(options=["to", "of", "at", "with"], correct=3),
      dict(options=["for", "after", "or", "but"], correct=2),
  ]),
  dict(type="reading", title="五、閱讀測驗", meta="每題3分，共15分", passages=[
    dict(label="A.", text="Billy: Lucas, look! A mummy!\nLucas: Billy, wait! You can't run here.\nBilly: Oh, OK. Hey, look! The picture is beautiful.\nGuard: Do not touch it, please.\nBilly: I'm sorry. I'm hungry, Lucas. Can I eat your cookies?\nGuard: Please do not eat or drink here.\nLucas: Billy, let's go home now.\n【字詞】touch 碰觸", items=[
      M("Where are Lucas and Billy?", "At a park.|In a zoo.|In a museum.|In a classroom.", "C"),
      M("Which（哪一個）is NOT a rule in this place?", "Do not run.|Do not talk.|Do not eat or drink.|Do not touch the pictures.", "B"),
    ]),
    dict(label="B.", text="【Place A】A GOOD PLACE FOR YOU\n• You can sit under the trees and eat.\n• You can talk and play with friends.\n\n【Place B】WE'RE OPEN\n• You can see beautiful pictures.\n• Draw with us, but don't eat or drink here.\n\n【Place C】NEW BOOKS!\n• You can read many good books here, but please be quiet.\n\n【Place D】COME NOW!\n• You can sing and dance.\n• You can play basketball.", items=[
      M("What sign can we see in Place B?" + IMG.format("signs.png"), "(A)|(B)|(C)|(D)", "D"),
      M(BX.format("Lynn: Shh! Don't talk here, Andy. Andy: Sorry.") + "Where are Lynn and Andy?", "At Place A.|At Place B.|At Place C.|At Place D.", "C"),
      M("Which of the four talks is at Place A?", "Peter: Look at the new books. Vicky: Wow! Let's sit here and read.|Ted: Wow! It is a beautiful place. The trees are tall. Kate: Let's go sit under that tree.|Hank: I am hungry. Carrie: Wait. You can't eat here.|Mark: Wow! No trees here. This place is big. Helen: Good. We can play baseball here.", "B"),
    ]),
  ]),
  dict(type="guided", title="六、依提示作答", meta="每題3分，共9分", items=[
    G("No, I can't jump rope.", "（造原問句）", "Can you jump rope?"),
    G("Let's not eat in class. Let's not talk in class.", "（合併兩句）", "Let's not eat or talk in class."),
    G("Please turn off <u>your phone</u>.", "（將畫線部分用代名詞受格改寫）", "Please turn it off."),
  ]),
  dict(type="translation", title="七、翻譯", meta="每題4分，共12分（A、B 兩句寫在同一格，例：A: … B: …）", items=[
    T("我們下課後跟著她一起去那座公園吧。", "Let's follow her to the park after class."),
    T("A：我可以使用這支電話嗎？B：當然。", "A: Can I use the phone? B: Sure. / A: Can I use the telephone? B: Sure. / A: Can I use this phone? B: Sure."),
    T("學生們，請安靜並且等待輪到你的機會。", "Students, please be quiet and wait for your turn."),
  ]),
]
