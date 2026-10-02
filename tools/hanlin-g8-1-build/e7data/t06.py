META = dict(n=6, h1="第6回・Unit 3", subtitle="Open the Magic Door", lesson="Unit 3", ctitle="Open the Magic Door")
CROPS = [
  ("sec5_ex", 12, (82, 100, 250, 250)),
  ("sec5_1", 12, (100, 248, 250, 392)),
  ("sec5_2", 12, (110, 386, 245, 540)),
  ("b2_poster", 12, (781, 906, 1432, 1360)),
]
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="【A部分 基礎題】11分，每題1分", items=[
    dict(q="Please listen to the teacher and follow the r___es.", answer="rules"),
    dict(q="We can see many beautiful dolls in a doll m___m.", answer="museum"),
    dict(q="Do not f___t with your brother. Be nice to him.", answer="fight"),
    dict(q="Look at that tall g___y. Is he Mr. Wu?", answer="guy"),
    dict(q="Molly, be c___l with the eggs. Don't drop（使…落下）them.", answer="careful"),
    dict(q="U___e your pencil and draw your favorite place.", answer="Use"),
    dict(q="Hurry! It's t___e for school.", answer="time"),
    dict(q="Look at the s___n there. We can't eat here.", answer="sign"),
    dict(q="Students, please don't talk in c___s.", answer="class"),
    dict(q="This is a m___c pen. It can write or draw for you.", answer="magic"),
    dict(q="A: What's that in your h___d, Ivy? B: It's a small gift for you. Here. Open it!", answer="hand"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="24分，每題2分", items=[
    dict(q="___ happy, Frank.", options=["Be","Do","Can","Let's"], correct=0),
    dict(q="My two-year-old daughter can draw ___ a marker.", options=["to","at","with","for"], correct=2),
    dict(q="A: Can you wash Kiki and Spot for me? B: Sure. I can wash ___ after school.", options=["it","they","her","them"], correct=3),
    dict(q="Quincy, ___ stand up, please.", options=["don't","don't be","is not","you are not"], correct=0),
    dict(q="Let's ___ write ___ draw on the desk.", options=["no; and","no; or","not; for","not; or"], correct=3),
    dict(q="A: Tim is hungry. B: I can cook for ___.", options=["he","him","they","them"], correct=1),
    dict(q="A: ___ I eat the orange in the box? B: Sure.", options=["Be","Can","Am","Let's"], correct=1),
    dict(q="A: ___ go to the ball game. B: Oh yeah!", options=["Be","Do","Let","Let's"], correct=3),
    dict(q="A: Can we go to the park this afternoon, Mom? B: No, you ___.", options=["not","don't","can't","are not"], correct=2),
    dict(q="A: Can you wait ___ your turn? B: Sure.", options=["to","at","for","in"], correct=2),
    dict(q="___ you read this for me? I can't see.", options=["Are","Let","Can","Please"], correct=2),
    dict(q="A: Who can play baseball? B: Maybe Tom ___ Brad can.", options=["or","but","with","after"], correct=0),
  ]),
  dict(type="mc", title="三、對話選擇", meta="10分，每題2分", items=[
    dict(q="A: Is Jodie's jump rope at your place? B: ___ Maybe it is.", options=["Hurry!","Let's go.","I'm not sure.","Don't say that."], correct=2),
    dict(q="A: Where can the boys play basketball? B: ___", options=["In the park.","The boys can.","With their friends.","Eight in the morning."], correct=0),
    dict(q="A: ___ B: He can sing.", options=["What can he do?","Who can do this?","Where can he go?","What can he sing?"], correct=0),
    dict(q="A: ___ B: Oops, sorry.", options=["Let's go home.","Be a good student.","Is it time for school?","Don't eat or drink in the classroom."], correct=3),
    dict(q="A: ___ B: Yes, you can.", options=["Please be careful.","Can I eat those apples?","Let's go to Kelly's house.","Don't talk to me now, please."], correct=1),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="8分，每題2分",
    passage="（In the classroom）\nPeter: Good morning, Mr. Lee.\nMr. Lee: ___1___ You're late today.\nPeter: Sorry, my watch is slow.\nMr. Lee: Please ___2___ late again.\nPeter: Yes, Mr. Lee.\nMr. Lee: Now, it's time ___3___ class. Sit down and ___4___ your book.\nPeter: Okay.\n\n【字詞】late 遲的　today 今天　slow 慢的　again 再一次",
    items=[
      dict(options=["Not bad.","Be nice, Peter.","Morning, Peter.","Nice to meet you, Peter."], correct=2),
      dict(options=["don't","not","not be","don't be"], correct=3),
      dict(options=["to","for","on","in"], correct=1),
      dict(options=["open","can open","to open","not open"], correct=0),
  ]),
  dict(type="guided", title="五、依例看圖造句", meta="8分，每句2分（例：Read the book. / Let's read the book.）", image="images/test6/sec5_ex.png", imageWidth=170, items=[
    dict(prompt="圖1 (1) 用祈使句描述圖片。", hint="", image="images/test6/sec5_1.png", imageWidth=150, answer="Don't eat or drink. / Don't eat or drink here. / Please don't eat or drink."),
    dict(prompt="圖1 (2) 用 Let's 句型描述圖片。", hint="", answer="Let's not eat or drink. / Let's not eat or drink here."),
    dict(prompt="圖2 (1) 用祈使句描述圖片。", hint="", image="images/test6/sec5_2.png", imageWidth=150, answer="Be quiet. / Be quiet, please. / Please be quiet."),
    dict(prompt="圖2 (2) 用 Let's 句型描述圖片。", hint="", answer="Let's be quiet."),
  ]),
  dict(type="guided", title="六、依提示作答", meta="4分，每題2分", items=[
    dict(prompt="be / boy / good / a / , / Calvin / .", hint="（重組）", answer="Calvin, be a good boy."),
    dict(prompt="<u>Mary and I</u> are in front of <u>our parents</u>.", hint="（將畫線部分用代名詞改寫）", answer="We are in front of them."),
  ]),
  dict(type="translation", title="七、整句式翻譯", meta="9分，每題3分", items=[
    dict(zh="請不要叫醒你妹妹。", answer="Please don't wake up your sister. / Please don't wake your sister up. / Don't wake up your sister, please. / Don't wake your sister up, please."),
    dict(zh="我們下課後可以說說話嗎？", answer="Can we talk after class?"),
    dict(zh="讓我們在那個地方等吧。", answer="Let's wait at that place. / Let's wait in that place. / Let's wait there."),
  ]),
  dict(type="mc", title="一、單題", meta="【B部分 活用題】8分，每題2分", items=[
    dict(q="A: Mom, please wake ___ up at six o'clock（在六點）. B: Okay.", options=["me","I","my","we"], correct=0),
    dict(q="A: Can't you play cards? B: Yes, ___.", options=["I can","you can","I can't","you can't"], correct=0),
    dict(q="A: Can you turn off the TV for me? B: Sure. I can turn ___.", options=["off","it","to it","it off"], correct=3),
    dict(q="A: ___ I use the bathroom here? B: Sure.", options=["Be","Am","Can","Let"], correct=2),
  ]),
  dict(type="reading", title="二、依短文或圖表選出適當的答案", meta="18分，每題3分", passages=[
    dict(label="A.", text="ABC ZOO\nRules:\n1. Don't sit on the rocks.\n2. Don't climb the trees.\n3. Don't use a flashlight in the bat house.\n4. Don't eat or drink near the monkeys.\nFollow the rules and be safe.\n\n【字詞】flashlight 手電筒　bat 蝙蝠　monkey 猴子",
      items=[
        dict(q="What CAN'T you do at the zoo?", options=["Sit on the rocks.","Stand next to a tree.","Watch the monkeys.","Turn off your flashlight in the bat house."], correct=0),
        dict(q="Who are these rules for?", options=["Patrick, a monkey in the zoo.","Benson, a student in the school now.","Anita, a 13-year-old girl at the zoo now.","Mrs. Smith, a housewife in her kitchen now."], correct=2),
        dict(q="<div style=\"background:#fff;border:1px solid var(--paper-line);border-radius:8px;padding:10px 14px;margin-bottom:8px;\">Alan: Can we have our lunch（午餐）here?<br>Blair: We can't. Look at the sign. \"Don't eat or drink here.\"<br>Alan: Okay. Let's not eat here.</div>Where can the sign be?", options=["Under a tree.","On the rocks.","In the zoo kitchen.","Near the monkeys."], correct=3),
      ]),
    dict(label="B.", text="【字詞】area 區域　car model 模型車　race 比賽　food 食物", image="images/test6/b2_poster.png", imageWidth=560,
      items=[
        dict(q="Look at this sign: 「Don't run!」<br>Where can this be at Miki's Car Park?", options=["On 1F, in the blue area.","On 1F, in the pink area.","On 1F, in the green area.","On B1, near the food area."], correct=2),
        dict(q="<div style=\"background:#fff;border:1px solid var(--paper-line);border-radius:8px;padding:10px 14px;margin-bottom:8px;\">Jacky: Mr. Anderson, what is this?<br>Mr. Anderson: Shh. Look at the sign. Be quiet.</div>Where are Mr. Anderson and Jacky now?", options=["In the pink area.","In the food area.","In the white area.","In the green area."], correct=2),
        dict(q="Which（哪一個）is true（真實的）about（關於）Miki's Car Park?", options=["We can see car models at B1.","We can't eat at Miki's Car Park.","We can have a car race in the blue area.","We can't see old cars at Miki's Car Park."], correct=2),
      ]),
  ]),
]

