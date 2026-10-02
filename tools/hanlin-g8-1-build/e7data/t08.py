META = dict(n=8, h1="第8回・Review Test 2", subtitle="Review Test 2（Unit 3～Unit 4）", lesson="Review 2", ctitle="Unit 3～Unit 4 總複習")
CROPS = [
  ("b2_a_hours", 16, (862, 626, 1372, 1006)),
]
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="【A部分 基礎題】8分，每題1分", items=[
    dict(q="A: Can I u___e your phone, please? B: Sure. Who are you calling（打電話）?", answer="use"),
    dict(q="Please be q___t. Grandma is sleeping.", answer="quiet"),
    dict(q="A: What m___e are you watching? B: Chef Rat. It's good.", answer="movie"),
    dict(q="Hayden is singing an E___sh song, \"Ten Little Indians.\"", answer="English"),
    dict(q="Look at the s___n there. Please turn off your phone.", answer="sign"),
    dict(q="Please f___w the teacher to the music room.", answer="follow"),
    dict(q="A: Are you free this w___d? B: No. My cousins are coming to my place on Saturday.", answer="weekend"),
    dict(q="Teresa is st___ying for a test（考試）at her desk.", answer="studying"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="28分，每題2分", items=[
    dict(q="Tilda ___ Davey Bowen's song in the bathroom.", options=["sing","singing","is singing","be singing"], correct=2),
    dict(q="Please do not fight. ___ nice to each other.", options=["Be","Is","Are","Let's"], correct=0),
    dict(q="Jimmy, please ___ the door for me. Thank you.", options=["open","opening","is opening","can open"], correct=0),
    dict(q="A: ___ is Jerry's party? B: This Wednesday.", options=["What","Where","What time","What day"], correct=3),
    dict(q="It's 6:25 a.m. = It's 6:25 ___.", options=["at night","in the evening","in the morning","in the afternoon"], correct=2),
    dict(q="Harley's basketball game is ___ Thursday night.", options=["in","at","on","for"], correct=2),
    dict(q="A: ___ your parents cooking? B: Yes. They are in the kitchen now.", options=["Do","Is","Can","Are"], correct=3),
    dict(q="The meet-and-greet is ___ 4 p.m. ___ 6 p.m.", options=["at; at","on; and","to; at","from; to"], correct=3),
    dict(q="A: What ___ is the welcome party? B: It's ___ 3:30.", options=["day; at","day; on","time; at","time; on"], correct=2),
    dict(q="Damien, ___ you hurry, please?", options=["be","can","are","do not"], correct=1),
    dict(q="Elliot's baseball game is ___ 3 p.m. ___ Sunday.", options=["at; ×","at; on","on; at","this; ×"], correct=1),
    dict(q="Look at the sign. You ___ eat here.", options=["not","are not","cannot","let's not"], correct=2),
    dict(q="Sally and her dog are ___ at the park.", options=["run and play","run and playing","running and play","running and playing"], correct=3),
    dict(q="___ stand behind the door, please.", options=["No","Isn't","Can't","Don't"], correct=3),
  ]),
  dict(type="mc", title="三、對話選擇", meta="8分，每題2分", items=[
    dict(q="A: ___ B: OK. I'm coming.", options=["Please hurry!","Are you sure?","Can you do it?","Let's wait for the bus."], correct=0),
    dict(q="A: ___ B: I am not sure. Maybe it's on Tuesday.", options=["Is today Tuesday?","What day is today?","What day is Lee's dance class?","Is Jim's party at 7 p.m. on Tuesday?"], correct=2),
    dict(q="A: ___ B: Oops, sorry.", options=["Can you sing a song for me?","Are you having a good time?","Please don't eat or drink here.","Let's go to the concert together."], correct=2),
    dict(q="A: The sofa is old and broken（破的）. B: It is. ___", options=["Let's not sit on it.","Do not stand up, please.","Please wait for your turn.","You can't take a look at it."], correct=0),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="8分，每題2分",
    passage="Mrs. Allen: ___1___ is Barry?\nMr. Allen: He's in his bedroom.\nMrs. Allen: ___2___\nMr. Allen: He's sleeping. It's only ___3___ seven o'clock.\nMrs. Allen: He's still sleeping? It's time for school.\nMr. Allen: School?\nMrs. Allen: Yes. ___4___\nMr. Allen: Ha ha! No. It's Sunday today.\nMrs. Allen: Oh, I'm sorry.\n\n【字詞】only 才　still 仍然",
    items=[
      dict(options=["How","Who","What","Where"], correct=3),
      dict(options=["How's his sleep?","How's he doing?","What is he doing?","What is he waiting for?"], correct=2),
      dict(options=["×","in","at","on"], correct=0),
      dict(options=["What day is today?","Isn't today Monday?","What time is it now?","Isn't it seven-thirty now?"], correct=1),
  ]),
  dict(type="guided-multi", title="五、依提示填空（動詞形式需做適當的變化）", meta="6分，每題1分", items=[
    dict(lines=["Please {{be}}（be）nice to your sister."]),
    dict(lines=["Let's {{walk}}（walk）to the park together."]),
    dict(lines=["The singers are {{signing}}（sign）pictures for their fans."]),
    dict(lines=["Can you {{take}}（take）a look at my car, please?"]),
    dict(lines=["Don't {{talk}}（talk）to Greta now, please."]),
    dict(lines=["Jason is {{sitting}}（sit）next to Anya."]),
  ]),
  dict(type="guided", title="六、依畫線部分造原問句", meta="9分，每題3分", items=[
    dict(prompt="The party is <u>at 6 p.m.</u>", hint="", answer="What time is the party?"),
    dict(prompt="Michelle is shaking hands with <u>her fans</u>.", hint="", answer="Who is Michelle shaking hands with? / Who's Michelle shaking hands with?"),
    dict(prompt="The baby can eat <u>bananas</u>.", hint="", answer="What can the baby eat?"),
  ]),
  dict(type="translation", title="七、整句式翻譯", meta="9分，每題3分", items=[
    dict(zh="請清洗你的手。", answer="Please wash your hands. / Wash your hands, please."),
    dict(zh="那傢伙受許多年輕人的歡迎。", answer="That guy is popular with many young people."),
    dict(zh="Alina，醒醒！媽媽正在車裡等我們。", answer="Alina, wake up! Mom is waiting for us in the car. / Alina, wake up! Mom's waiting for us in the car."),
  ]),
  dict(type="mc", title="一、單題", meta="【B部分 活用題】6分，每題2分", items=[
    dict(q="A: ___ ride the bus to the park. B: OK. Let's walk together.", options=["Let's","Do","Let's not","They can't"], correct=2),
    dict(q="A: The music is loud（大聲的）. Can you ___, please? Dad is sleeping. B: OK. I'm sorry.", options=["turn it","off it","turn off","turn it off"], correct=3),
    dict(q="A: How's your mother doing? B: ______", options=["She can cook for us.","She's great. Thanks.","She's watching a video.","She's not ready. Please wait."], correct=1),
  ]),
  dict(type="reading", title="二、依短文或圖表選出適當的答案", meta="18分，每題3分", passages=[
    dict(label="A.", text="Bruna: Look. A new museum is open. Let's go together.\nWayne: Is the new museum next to the zoo?\nBruna: Yes. It's the Hopper Museum.\nWayne: What are the opening hours?\nBruna: Let's see. It's open from 10 a.m. to 5 p.m.\nWayne: What time is it?\nBruna: It's 1:30. We can go now.\nWayne: Wait. The museum is open every day, but not on Mondays.\nBruna: OK. Maybe this Friday?\nWayne: I am not free on Friday. How about Sunday?\nBruna: Sure. I can't wait.\n\n【字詞】opening hours 營業時間　every 每一　How about...? 那…呢？",
      items=[
        dict(q="What day is today?", options=["Monday.","Friday.","Saturday.","Sunday."], correct=0),
        dict(q="Which（哪一個）is NOT true（真實的）?", options=["It is 1:30 in the afternoon now.","Bruna and Wayne are at the museum.","Bruna and Wayne are free this Sunday.","People can go to the museum on weekends."], correct=1),
        dict(q="Which picture can people see at the museum?", image="images/test8/b2_a_hours.png", options=["A","B","C","D"], correct=2),
      ]),
    dict(label="B.", text="Hi, guys. This is Nancy Drewes. You are now watching <i>Follow the Bad Guy</i>. It is 4:27 in the afternoon. My friend Kip can't find his <u>cell</u> after school. Let's go check the school bus. Hmm... it's not here. Wait. Who's that guy with a pink cell in his hand? Kip's cell is pink, too. Let's follow him.\n\nOK. Look at my cell. It's 5 p.m. now. Kip and I are following a guy at the park. Maybe Kip's cell is in his hand. Look. The guy is taking pictures with the cell. It is ringing now. Hmm... who is the guy talking to on the cell?\n\nNow it's 5:31. The guy is washing his hands, and the cell is next to him. Wait. Listen! A cell is ringing, but it's not the cell next to him. Kip, what's that in your bag? What? That's your cell? Oh, Kip! Are you kidding me? OK. That's it for today's <i>Follow the Bad Guy</i>. See you!\n\n【字詞】find 找到　check 查看　ring 響起鈴聲　kid 開玩笑",
      items=[
        dict(q="What CAN'T you do with a <u>cell</u>?", options=["Wash hands.","Take pictures.","Talk to people.","Check the time."], correct=0),
        dict(q="Kip's cell is in his bag. Nancy is looking at it and talking about it. What time is it?", options=["4 a.m.","4:27 p.m.","5 p.m.","5:31 p.m."], correct=3),
        dict(q="Which is NOT true?", options=["The guy's cell is pink.","Nancy is taking videos.","Kip's cell is in the guy's hand.","Nancy is not happy about（對於）Kip."], correct=2),
      ]),
  ]),
]
