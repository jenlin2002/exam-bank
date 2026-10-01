META = dict(n=7, h1="第7回・Review Test 2", subtitle="Unit 3～Unit 4、節慶單元 總複習")
W = ["floor","broke","decided","believe","moved","remember","window","acted"]
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="【A部分 基礎題】15分，每格1分", items=[
    dict(q="Diane likes traveling. She visited five c___ries last year.", answer="countries"),
    dict(q="You can always see many ch___n with their parents at that park on weekends.", answer="children"),
    dict(q="A: Candy, can I borrow your pen? B: No p___m. Here you go.", answer="problem"),
    dict(q="Ken bought Ann a gift. He wanted to thank her for s___ving his cat's life.", answer="saving"),
    dict(q="After he washed his clothes, he dried them and h___g them up behind the house.", answer="hung"),
    dict(q="The elevator（電梯）isn't working; we can only take the s___rs.", answer="stairs"),
    dict(q="A: Are you ready to go? B: Just one m___t, please.", answer="moment"),
    dict(q="A: Good morning. How was your sleep? B: Not very good. I had a bad d___m.", answer="dream"),
    dict(q="A: Did you have any p___ts? B: Yes. I k___t a dog and a cat before.", answers=["pets","kept"]),
    dict(q="A: You are f___ly here. What happened? B: I'm sorry. There were many cars on the road.", answer="finally"),
    dict(q="A mouse got into Paul's house th___h a hole in the door last night. After Paul caught the mouse, he decided to f___x the door.", answers=["through","fix"]),
    dict(q="I'm looking for a desk with many d___rs. I have lots of things, and I need to find them a home.", answer="drawers"),
    dict(q="A: You helped me a lot with my report. Thank you, Lucy! B: It's n___g. I enjoy helping people.", answer="nothing"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="22分，每題2分", items=[
    dict(q="Watching baseball games ___ fun.", options=["has","is","are","have"], correct=1),
    dict(q="Daniel is thinking about ___ a boat.", options=["buy","buys","to buy","buying"], correct=3),
    dict(q="The soup is yummy, and it is easy ___.", options=["make","makes","to make","making"], correct=2),
    dict(q="Rachel gave up ___ after she lost her right leg.", options=["dance","danced","to dance","dancing"], correct=3),
    dict(q="Jenny often practices ___ early in the morning.", options=["run","running","to run","to running"], correct=1),
    dict(q="Iris plans to catch some fish and ___ them to her parents.", options=["send","sent","sends","sending"], correct=0),
    dict(q="The man was dying ___ the police found him.", options=["or","then","when","because"], correct=2),
    dict(q="Ben ___ the truck when his wife ___ the house.", options=["is cleaning; left","cleaned; leaving","was cleaning; left","cleaned; is leaving"], correct=2),
    dict(q="A: Is it a quarter ___ nine? B: Yes. It's eight forty-five.", options=["past","to","after","over"], correct=1),
    dict(q="A: What were you doing at half past two? B: I ___ the dishes.", options=["do","did do","am doing","was doing"], correct=3),
    dict(q="A: ___ was talking on the phone in the living room at five this morning? B: Mom ___.", options=["Who; did","What; did","Who; was","What; was"], correct=2),
  ]),
  dict(type="mc", title="三、對話選擇", meta="4分，每題2分", items=[
    dict(q="A: I have butterflies in my stomach now. B: ___ You can do it.", options=["Good idea!","Are they dead?","Don't catch them.","Just take it easy."], correct=3),
    dict(q="A: ___ B: I might go to the movies with my friends.", options=["What do you plan to do later?","Do you like going to the movies?","Where do your friends want to go?","What do you enjoy doing in your free time?"], correct=0),
  ]),
  dict(type="cloze", title="四、文意選填", meta="8分，每題2分",
    passage="（選項）(A) floor　(B) broke　(C) decided　(D) believe　(E) moved　(F) remember　(G) window　(H) acted\n\nIt was dark and quiet that night. I was in bed and ready to sleep. Before I closed my eyes, I saw something by my bedroom ___1___. It was white, and it looked like a person. Suddenly, it ___2___. I couldn't ___3___ my eyes. \"Someone or something is out there on the balcony,\" I thought. That couldn't be my mom or dad; they went to bed before I did. I was scared, but I ___4___ to check it out. I opened the door to the balcony. It was just a jacket.\n\n【字詞】look 看起來　suddenly 突然間　balcony 陽台",
    items=[dict(options=W, correct=c) for c in [6,4,3,2]]),
  dict(type="guided", title="五、依提示作答", meta="4分，每題2分", items=[
    dict(prompt="Seeing relatives is nice.", hint="（用虛主詞It改寫）", answer="It is nice to see relatives."),
    dict(prompt="What did Mrs. Lin tell her son to do?", hint="（以「拖地板」詳答）", answer="She told him to mop the floor."),
  ]),
  dict(type="guided", title="六、看圖詳答問題", meta="6分，每題3分", items=[
    dict(prompt="What was the man doing at 1 p.m. yesterday?", hint="（看圖回答）", image="images/test7/sec6_1.png", answer="He was driving a car (at 1 p.m. yesterday)."),
    dict(prompt="What are the farmers good at?", hint="（看圖回答）", image="images/test7/sec6_2.png", answer="They are good at growing pumpkins."),
  ]),
  dict(type="translation", title="七、整句式翻譯", meta="8分，每題4分", items=[
    dict(zh="當他睡著時，他父母正在擦桌子。（His parents...）", answer="His parents were wiping the table(s) / desk(s) when he fell asleep."),
    dict(zh="在這間舊工廠裡開萬聖夜派對是個很棒的點子。（It is...）", answer="It is a great idea to have a Halloween party in this old factory."),
  ]),
  dict(type="mc", title="一、單題", meta="【B部分 活用題】8分，每題2分", items=[
    dict(q="It might rain later, so Carrie decided ___ to the park.", options=["not go","not to go","didn't go","not going"], correct=1),
    dict(q="A: There's something wrong with my teeth. B: Do you need to go to the ___?", options=["lawyer","dentist","soldier","fisherman"], correct=1),
    dict(q="A: I called Kate, but she didn't answer the phone. B: Try ___ her again later.", options=["call","calls","called","calling"], correct=3),
    dict(q="A: Do you have a lot of homework ___ today? B: Yes, but I already（已經）finished some.", options=["do","to do","doing","of doing"], correct=1),
  ]),
  dict(type="cloze", title="二、克漏字選擇", meta="9分，每題3分",
    passage="Maggie and Patra were walking in the forest on a hot summer day. After hours of walking, they decided to take a rest. Just when they sat down, they saw a small but beautiful lake. \"Let's take off our clothes and go for a swim in the lake,\" Patra said to Maggie. \"___1___ Besides, is it safe to swim in that lake?\" said Maggie. \"___2___ There is no one else but me here. And it's just a small lake,\" Patra said and jumped into the lake after she took her clothes off. Maggie soon joined Patra. After a few minutes, they saw an old man. He was coming to the lake. \"Can you believe that? That old man is watching us,\" Maggie said to Patra. The old man heard Maggie and took off his sunglasses. \"Girls, ___3___,\" said the old man. \"I am blind, and my house is by the lake.\"\n\n【字詞】take off 脫下　sunglasses 太陽眼鏡　blind 盲的",
    items=[
      dict(options=["The water is too cold.","How do we dry our clothes?","There are too many people here.","I don't want people to see my body."], correct=3),
      dict(options=["Don't worry.","Never give up.","Keep practicing.","Don't break the rule."], correct=0),
      dict(options=["this place is too dark","I enjoy swimming, too","I didn't come here to watch you","swimming in that lake is not safe"], correct=2),
  ]),
  dict(type="reading", title="三、依短文選出適當的答案", meta="16分，每題4分", passages=[
    dict(label="【A】", text="Kyle: Sorry, Mrs. Davis. I'm late.\nMrs. Davis: Don't be late again. By the way, is everything ready for the meeting later?\nKyle: What meeting?\nMrs. Davis: I have a meeting with Mr. Wilson today. I told you yesterday. You don't remember?\nKyle: Oh yes! I remember now. Where did I put the document? Give me a minute.\nMrs. Davis: Don't worry. We have some time before Mr. Wilson comes. Find the document, bring it to me, and go make some coffee.\n(An hour later)\nKyle: Here's the document, Mrs. Davis.\nMrs. Davis: Thank you. Where is the coffee then?\nKyle: I finished it. You told me to make some coffee, but you didn't tell me to bring you some.\nMrs. Davis: Kyle, I hate to say this to you, but you might need to start looking for another job.\nKyle: Why? What did I do wrong?\n\n【字詞】meeting 會議　document 文件　bring 帶來",
      items=[
        dict(q="Which is true（真實的）about Kyle?", options=["He is good at his job.","Mrs. Davis is his boss.","He is never late for work.","He plans to find another job."], correct=1),
        dict(q="Why did Mrs. Davis say \"you might need to start looking for another job\" to Kyle?", options=["She didn't want Kyle to do her job.","She wanted Kyle to learn new things.","She wanted to help Kyle with his job interview.","She planned to find someone else to be her secretary."], correct=3),
      ]),
    dict(label="【B】Book Review by Jill Lee　★★★★☆", text="《The Road to Success》by Robert Price\n\nAre you looking for a change in your life?\nDo you want to make money in a short time?\nDo you want to be successful like Robert Price?\n\n    Before he became a salesman, Robert Price worked different jobs at the same time. During the day, he was an office worker. At night, he washed the dishes at a restaurant. On weekends, he drove a taxi. He was tired all the time, and he didn't have time for his family at all. However, he didn't make enough money. It was not easy for him to feed a family of five. One day, he decided to become a salesman. This decision changed his life and his family's. After years and years of trying, he became the best salesman in history. Do you want to know his secret? Read the book. It might change your life.\n\n【字詞】review 評論　taxi 計程車　decision 決定　best 最好的　secret 祕密",
      items=[
        dict(q="What do we know about Robert Price?", options=["He became successful just because he was lucky.","He lost his job and his family before he became successful.","He worked three different jobs before he became a salesman.","He sold things and made lots of money right after he became a salesman."], correct=2),
        dict(q="Which excerpt（節錄）might be from the book?", options=["I was washing dishes from morning to night, seven days a week. One day I just stopped and said, \"This is enough. No more dishes.\"","I made lots of money, but I thought, \"Is this it? Can I do anything else?\" Then I started something new, and it changed my life.","I was seldom home. My one-year-old daughter didn't even know me. She cried when I tried to hold her. I was so sad.","I had no job, and my family left me. I lost everything, but I didn't give up. I went to so many job interviews. Finally, I got a job at a shop."], correct=2),
      ]),
  ]),
]
