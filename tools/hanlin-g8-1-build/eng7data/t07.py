META = dict(n=7, h1="第7回・Unit 4", subtitle="What Time Is the Concert?")
I = "images/test7/"
CROPS = [("p1",14,(90,82,210,190)), ("p2",14,(90,192,210,290)), ("p3",14,(90,300,210,405)), ("p4",14,(608,50,750,160)),
         ("b1",14,(430,540,570,640)), ("sched",14,(605,730,1105,1168))]
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="【A部分 基礎題】每題1分，共11分", items=[
    dict(q="The day before（在…之前）Thursday is W___y.", answer="Wednesday"),
    dict(q="A: Are you r___y? The bus is coming. B: OK. Let's go.", answer="ready"),
    dict(q="The concert is great. E___y is having a good time.", answer="Everybody"),
    dict(q="A: What m___e are you watching? B: <i>Eight Bad Guys</i>. It's good.", answer="movie"),
    dict(q="A: Wow! Who's that beautiful girl? B: That's Willie's sister. She's very c___e.", answer="cute"),
    dict(q="A: I can play the guitar（吉他）. B: Great! You can play in our b___d.", answer="band"),
    dict(q="A: Let's take a w___k at the park. B: Sure. Lucky can come with us, too.", answer="walk"),
    dict(q="The writer is very p___ar. His books are many people's favorite.", answer="popular"),
    dict(q="A: Are you f___e on Friday night? Let's play baseball t___r. B: Sorry. I can't play with you. My dance class is at 7 p.m.", answers=["free","together"]),
    dict(q="A: I'm hungry. Can I eat a___l the cookies? B: Sure.", answer="all"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共22分", items=[
    dict(q="A: ___ is it? B: Five oh seven.", options=["How","What day","How old","What time"], correct=3),
    dict(q="A: Where are you two? B: We are ___ Joel's concert.", options=["at","on","in","with"], correct=0),
    dict(q="Sherry Peterson's meet-and-greet is ___ ten ___ Saturday morning.", options=["on; at","at; at","on; on","at; on"], correct=3),
    dict(q="Look! A dog ___ under your car.", options=["sleep","to sleep","is sleeping","sleeping"], correct=2),
    dict(q="A: What day is the basketball game? B: It's ___ this Tuesday.", options=["on","at","in","×"], correct=3),
    dict(q="A: ___ you studying? B: No, I ___.", options=["Can't; am not","Don't; can't","Aren't; am not","Aren't; don't"], correct=2),
    dict(q="A: ___ is the concert? B: Isn't it on Tuesday?", options=["What","How old","What time","What day"], correct=3),
    dict(q="A: Is the baseball game ___ today? B: No. It's ___ Sunday.", options=["×; at","×; on","on; ×","on; on"], correct=1),
    dict(q="A: ___ Cathy studying? B: In her sister's bedroom.", options=["Who's","What's","How's","Where's"], correct=3),
    dict(q="Jerry and Tammy ___ singing and dancing.", options=["is","am","are","can"], correct=2),
    dict(q="A: Let's ___ to the park. B: Sorry, I can't. I am ___ for Elena.", options=["go; wait","going; wait","go; waiting","going; waiting"], correct=2),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共10分", items=[
    dict(q="A: ___ B: It's at 6 p.m.", options=["What time is your welcome party?","What day is Mike's welcome party?","What day is the party for Mrs. White?","What time is Linda's party this morning?"], correct=0),
    dict(q="A: Is Ann's basketball game today? B: ___", options=["Yes. It's this weekend.","No. It's at 9 p.m. today.","Yes. It's at 8 p.m. today.","No. It's not at six o'clock."], correct=2),
    dict(q="A: What are you doing? B: ___", options=["We are free.","You can sign here.","The report is ready.","We are writing a report."], correct=3),
    dict(q="A: What day is it today? B: ___", options=["It's on Sunday.","It's a good day.","It's not my day.","Isn't it Monday?"], correct=3),
    dict(q="A: ___ B: No. I am watching a music video.", options=["What are you watching?","Aren't you watching a movie?","Isn't that Fred's new music video?","Where are you watching the music video?"], correct=1),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="每題2分，共8分",
    passage="It is nine o'clock on a Saturday night. Kelly is having a ___1___ at her new house. All her friends are there. Jake and Finn are listening to pop music. They are big ___2___ of Michelle Johnson. Clarence and Mary are dancing together. They are dancing to the music. In front of the TV are Anais and Darwin; they are sitting on the sofa and ___3___ a movie. They are eating and drinking, too. Kelly is looking at her friends. She is ___4___ of them with her phone. It's a nice party. Everyone is having a great time.",
    items=[
      dict(options=["party","band","report","class"], correct=0),
      dict(options=["days","fans","movies","hands"], correct=1),
      dict(options=["watch","can watch","watching","is watching"], correct=2),
      dict(options=["taking a look","taking walks","shaking hands","taking pictures"], correct=3),
  ]),
  dict(type="guided", title="五、看圖詳答問題", meta="每題3分，共12分", items=[
    dict(prompt="What is the girl doing?", hint="（看圖回答）", image=I+"p1.png", answer="She is taking a picture."),
    dict(prompt="What time is it now?", hint="（看圖回答）", image=I+"p2.png", answer="It's seven o'clock."),
    dict(prompt="Are the boy and the girl washing their hands?", hint="（看圖回答）", image=I+"p3.png", answer="No, they aren't. They are shaking hands."),
    dict(prompt="What day is it today?", hint="（看圖回答）", image=I+"p4.png", answer="It's Friday."),
  ]),
  dict(type="guided", title="六、依提示作答", meta="每題3分，共9分", items=[
    dict(prompt="The fans are <u>waiting for the singer</u>.", hint="（依畫線部分造原問句）", answer="What are the fans doing?"),
    dict(prompt="Ruby's music class is <u>at 5 p.m.</u>", hint="（依畫線部分造原問句）", answer="What time is Ruby's music class?"),
    dict(prompt="The zoo is not open <u>on Monday</u>.", hint="（依畫線部分造原問句）", answer="What day is the zoo not open? / What day isn't the zoo open?"),
  ]),
  dict(type="mc", title="一、單題", meta="【B部分 活用題】每題2分，共10分", items=[
    dict(q="Look at the picture. The girl is ___.", image=I+"b1.png", options=["writing a report","watching a video","cleaning her desk","studying in the room"], correct=3),
    dict(q="___ is between Wednesday and Friday.", options=["Monday","Tuesday","Thursday","Saturday"], correct=2),
    dict(q="Let's go to the movies on ___.", options=["today","Tuesday night","the evening","this Wednesday"], correct=1),
    dict(q="A: The students are singing in the music room. B: ___ A: An English song.", options=["How are they doing?","What are they doing?","What are they singing?","Where are they singing?"], correct=2),
    dict(q="A: ___ B: It's four fifteen.", options=["What is the time?","What day is it today?","How old is your dad?","How long is the movie?"], correct=0),
  ]),
  dict(type="reading", title="二、依短文或圖表選出適當的答案", meta="每題3分，共18分", passages=[
    dict(label="【A】", text="Mom: Tommy, are you singing?\nTommy: Yes. I am singing to Hello Boys' new music video. Their music is great. Mom, come sing with me.\nMom: Not now, Tommy. Your baby sister is sleeping in the next room. Can you be quiet, please?\nTommy: But Mel is dancing in her bedroom, and John is jumping rope in his bedroom. Why can't I sing in my room?\nMom: Their rooms aren't next to Linda's room.\nTommy: Oh, Mom!\nMom: Your dad is cooking now. Go help your dad, OK?\nTommy: OK.\nMom: Good boy. Hey, maybe you can sing in the kitchen with Dad.\n\n【字詞】why 為什麼　help 幫助", items=[
      dict(q="What's Linda doing?", options=["She's singing.","She's dancing.","She's sleeping.","She's cooking."], correct=2),
      dict(q="How many（有多少）people are in the kitchen now?", options=["One.","Two.","Three.","Four."], correct=0),
      dict(q="Which（哪一個）is true（真實的）?", options=["Mel is dancing in John's room.","Tommy's mom is jumping rope.","Tommy's dad is singing in the kitchen.","Tommy's room is next to his baby sister's room."], correct=3),
    ]),
    dict(label="【B】Here are Sandy's, Leo's, and their mother's schedules for this week.", text="【字詞】schedule 行程表　drive... to 開車載…去", image=I+"sched.png", items=[
      dict(q="It's four thirty-two in the afternoon. Sandy is waiting for her mom. What day is it today?", options=["Monday.","Tuesday.","Thursday.","Saturday."], correct=1),
      dict(q="It's ten in the morning on Saturday. Leo is in the car with his mom. Where are they going?", options=["To school.","To a meet-and-greet.","To a concert.","To the Browns' place."], correct=1),
      dict(q="Which is NOT true?", options=["It's seven o'clock on Monday evening. Leo is at his music class.","It's 4:30 p.m. on Tuesday. Sandy's mom is at Sandy's school.","It's eight on Monday. Sandy and Leo are studying English together.","It's 8:40 p.m. on Sunday. Sandy's mom is talking to Mr. Brown at his place."], correct=2),
    ]),
  ]),
]
