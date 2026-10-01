META = dict(n=1, h1="第1回・Unit 1", subtitle="How Was the Weather in Australia?")
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="【A部分 基礎題】13分，每題1分", items=[
    dict(q="I was m___d at Chris because he broke（打破）my cup and didn't say sorry to me.", answer="mad"),
    dict(q="A: I put my pen on the table two minutes ago, but now it's not there. How s___e! B: Maybe your baby sister took it.", answer="strange"),
    dict(q="A: Why don't you talk to Noah? B: We had a fight, so we're not s___king to each other.", answer="speaking"),
    dict(q="A: Do we need an umbrella? B: Yes. It might be r___y later today.", answer="rainy"),
    dict(q="A: What does this sign m___n? B: I don't know. Let's ask（問）the teacher.", answer="mean"),
    dict(q="A: Isn't Dr. Baker in the office? B: No. She went on v___n.", answer="vacation"),
    dict(q="My favorite season is a___n.", answer="autumn"),
    dict(q="A: I'm hungry. B: Me too. Let's o___r something from Richard's Pizza.", answer="order"),
    dict(q="A: Kate's baby girl is so cute. B: Yes, she's very lo___ly.", answer="lovely"),
    dict(q="The pot（鍋子）is hot. Please hold it with g___ves.", answer="gloves"),
    dict(q="A: Can I b___w your eraser? B: Sure. Here you go.", answer="borrow"),
    dict(q="A: I'm still hungry. Can I have a___r slice of toast? B: Okay. Here you go.", answer="another"),
    dict(q="Vivian didn't have enough money for breakfast the other day, so I l___t her some. She gave the money back（返回）to me today.", answer="lent"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="22分，每題2分", items=[
    dict(q="A: What was the weather ___ yesterday in Toronto? B: It was cold and cloudy.", options=["×","for","like","about"], correct=2),
    dict(q="It's hot and sunny ___ Taiwan ___ summer.", options=["in; in","on; in","in; on","on; on"], correct=0),
    dict(q="A: ___ the weather today? B: It's warm, so you might not need that jacket.", options=["How's","What's","When's","Where's"], correct=0),
    dict(q="A: Where did you get the postcard? It's beautiful. B: My friend sent it ___ me ___ Australia.", options=["to; to","for; from","from; for","to; from"], correct=3),
    dict(q="A: Does it snow a lot in winter? B: No, but there's ___ rain during that time.", options=["any","many","a lot","a lot of"], correct=3),
    dict(q="A: Who are you writing ___? B: My grandparents. I miss them.", options=["on","at","to","for"], correct=2),
    dict(q="___ can be very hot but ___ here in June.", options=["We; wind","It; wind","It; windy","We; windy"], correct=2),
    dict(q="___ some rain in early spring.", options=["It","It is","We have","There are"], correct=2),
    dict(q="A: That's a nice snowboard. B: Thanks. My dad ___ me this snowboard ___ my birthday.", options=["gave; to","sent; from","showed; to","bought; for"], correct=3),
    dict(q="The weather is always cold and ___ on the mountain top（頂部）.", options=["rain","cloud","warm","snowy"], correct=3),
    dict(q="Mandy didn't have an umbrella with her, so she borrowed one ___ her cousin.", options=["to","at","from","about"], correct=2),
  ]),
  dict(type="mc", title="三、對話選擇", meta="6分，每題2分", items=[
    dict(q="A: Josh, Uncle Buddy made this cake for us. B: ___", options=["It was fun.","I want one, too.","That was kind of him.","He doesn't hate snacks."], correct=2),
    dict(q="A: ___ B: No. It's hot and sunny today.", options=["Is today a hot day?","Is it a cloudy day today?","How's the weather today?","What's the weather like here?"], correct=1),
    dict(q="A: ___ B: It was nice. We had a great time there.", options=["Did you go to Maggie's farm?","What did you do last weekend?","How was your trip to Maggie's farm?","Was the weather nice on Maggie's farm?"], correct=2),
  ]),
  dict(type="guided-multi", title="四、依提示填入正確的字詞", meta="6分，每格1分", items=[
    dict(zh="(show)", lines=["Helen took out her new phone and {{showed}} it {{to}} her brother."]),
    dict(zh="(lend)", lines=["A: Can you {{lend}} a pencil {{to}} me? B: Sure. Here you are."]),
    dict(zh="(make)", lines=["Josh and his classmates {{made}} a big birthday card {{for}} their English teacher, Miss Clark. Miss Clark was very happy."]),
  ]),
  dict(type="guided", title="五、看圖詳答問題", meta="6分，每題3分", items=[
    dict(prompt="How was the weather last night?", hint="（看圖回答）", image="images/test1/sec5_1.png", answer="It was snowy. / There was (heavy) snow. / It snowed (a lot). / It was cold."),
    dict(prompt="What did the boy buy for his father?", hint="（看圖回答）", image="images/test1/sec5_2.png", answer="He bought a jacket for him. / He bought him a jacket."),
  ]),
  dict(type="guided", title="六、依提示作答", meta="4分，每題2分", items=[
    dict(prompt="They have a lot of rain in summer.", hint="（用It改寫）", answer="It rains a lot in summer."),
    dict(prompt="Mom always reads us stories before bed.", hint="（加入介系詞改寫）", answer="Mom always reads stories to us before bed."),
  ]),
  dict(type="translation", title="七、整句式翻譯", meta="6分，每題3分", items=[
    dict(zh="去年春天他們去了美國旅行。（took...）", answer="They took a trip to the USA last spring."),
    dict(zh="事實上，Mary 並不住在這條路上。", answer="In fact, Mary doesn't live on this road."),
  ]),
  dict(type="mc", title="一、單題", meta="【B部分 活用題】8分，每題2分", items=[
    dict(q="Maddie is going out now. She has an umbrella with her because it is rainy today. Where might Maddie live?", image="images/test1/b1_map.png", options=["In Taipei.","In Chiayi.","In Hualien.","In Taichung."], correct=0),
    dict(q="A: How was the party at Dylan's house? B: It was cool. I had ___ fun.", options=["a","many","any","a lot of"], correct=3),
    dict(q="A: Did you give the cookies to your sister? B: Yes, I just gave ___ to ___. She's eating them now.", options=["them; her","her; them","another; them","them; another"], correct=0),
    dict(q="A: ___ Leah's brother like? B: He is a nice guy, but sometimes he can be strange.", options=["How's","Who's","What's","Why's"], correct=2),
  ]),
  dict(type="cloze", title="二、克漏字選擇", meta="9分，每題3分",
    passage="In many places, there are four seasons in a year, but in the Philippines, ___1___. They are the rainy season and the dry season. Usually, the rainy season is from June to early October, and the dry season is from late October to May. During the rainy season, the weather is rainy and hot. The rain comes almost every day during the rainy season. Sometimes, ___2___. On the other hand, the weather in the dry season is usually nice and ___3___. It's perfect weather for the beaches and water sports. Many people take a trip to the Philippines during that time.\n\n【字詞】the Philippines 菲律賓　dry 乾的　almost 幾乎",
    items=[
      dict(options=["there is only one season","it is always hot and rainy","there are only two seasons","the seasons are always changing"], correct=2),
      dict(options=["it snows, too","it can be very cold","the rain lasts all day","there's no rain for years"], correct=2),
      dict(options=["rainy","cold","sunny","snowy"], correct=2),
  ]),
  dict(type="reading", title="三、依短文或圖表選出適當的答案", meta="20分，每題4分", passages=[
    dict(label="【A】", text="    Twenty years ago, there was a boy. His family didn't have much money. He wanted to help his family, so he sold postcards on the street every day after school. One day, he was very hungry and thirsty. He sat down in front of a house and took out his water bottle. There was no water in it. A few minutes later, a young girl came out of the house, and in her hand was a big glass of milk. \"We don't have much in the house. But take the milk. You need it,\" said the girl. The boy thanked the girl, gave her a postcard, and drank all the milk.\n    Twenty years later, the girl became a woman. She was sick, but she didn't have enough money for a good doctor. One day, a doctor came to her house. With the doctor's help, the woman got well, but she didn't have enough money for the doctor. So she said sorry to him again and again. The doctor took a look at the postcard on the wall and said to the woman, \"Please stop; I did this for free. Thank you for the milk twenty years ago.\"\n\n【字詞】want to 想要　became 成為（become的過去式）　get well 康復　free 免費的",
      items=[
        dict(q="What did the boy get from the girl?", options=["A postcard.","Some money.","A glass of milk.","A bottle of water."], correct=2),
        dict(q="Which is NOT true（真實的）about the doctor?", options=["He got help from the woman before.","He sent a postcard to the woman before.","He first met the woman twenty years ago.","He didn't take any money from the woman."], correct=1),
        dict(q="What do we know from the reading?", options=["The kind girl became a great doctor.","The girl was very sick twenty years ago.","The woman sells postcards on the street.","The boy met the girl again many years later."], correct=3),
      ]),
    dict(label="【B】", text="", image="images/test1/b3_weather.png",
      items=[
        dict(q="<div style=\"background:#fff;border:1px solid var(--paper-line);border-radius:8px;padding:10px 14px;font-style:italic;margin-bottom:8px;\">Kyle: Today is hot and sunny. Summer is here.<br>Candice: Right. There is no wind.</div>Where may Kyle and Candice be now?", options=["City A.","City B.","City C.","City D."], correct=1),
        dict(q="What do we know about the weather in these cities?", options=["It seldom rains in City D.","There is a lot of rain in City B.","It is very cold in City A in winter.","It is always cloudy in City C in fall."], correct=2),
      ]),
  ]),
]
