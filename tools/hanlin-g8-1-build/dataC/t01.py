META = dict(n=1, h1="第1回・Unit 1", subtitle="How Was the Weather in Australia?")
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="20分，每題2分", items=[
    dict(q="It is a sunny day. There are beautiful white c___ds in the blue sky.", answer="clouds"),
    dict(q="It is cold today. H___y snow is falling in the mountains now.", answer="Heavy"),
    dict(q="A: Do you s___k English? B: Yes, but my English is not very good.", answer="speak"),
    dict(q="There is a s___ge man at the playground. He's just standing there and watching the kids. Be careful of him.", answer="strange"),
    dict(q="The rainy s___n is from April to June. It rains a lot during that time.", answer="season"),
    dict(q="A: May I take your o___r? B: Yes. Can I have a glass of apple juice?", answer="order"),
    dict(q="There are always many cars on these busy r___ds in the morning from Monday to Friday. Many people are going to work.", answer="roads"),
    dict(q="In a___n, the leaves（樹葉）change into different colors—red, orange, and yellow.", answer="autumn"),
    dict(q="Look at my new bag. My mom g___ve it to me yesterday. I like it very much.", answer="gave"),
    dict(q="Debbie's parents live in the USA, so she often goes there on v___n during Lunar New Year（農曆新年）.", answer="vacation"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="20分，每題2分", items=[
    dict(q="A: ___ the weather like here? B: It's warm and sunny.", options=["How's","Who's","What's","Where's"], correct=2),
    dict(q="___ don't have much snow in winter.", options=["It","We","There","Here"], correct=1),
    dict(q="___ is a lot of rain here in spring.", options=["It","There","This","The weather"], correct=1),
    dict(q="A: How's the weather there ___ fall? B: ___ is cool.", options=["in; It","at; It","in; There","at; There"], correct=0),
    dict(q="Judy sends a letter（信）___ Joseph every week. She misses him a lot.", options=["to","with","of","from"], correct=0),
    dict(q="Mom's birthday is next week. Let's buy a gift ___ her.", options=["to","from","at","for"], correct=3),
    dict(q="Aunt Dora ___ cookies for us last week. They were yummy.", options=["sent","showed","made","took"], correct=2),
    dict(q="I usually borrow books ___ the library twice a month.", options=["of","to","with","from"], correct=3),
    dict(q="The woman didn't have an umbrella, so the man lent ___ one.", options=["she","her","to her","for her"], correct=1),
    dict(q="It's sunny and warm today. ___ lovely!", options=["Who","How","What","Which"], correct=1),
  ]),
  dict(type="mc", title="三、對話選擇", meta="10分，每題2分", items=[
    dict(q="A: How are you doing? B: ___", options=["Okay, see you soon.","I am watching TV at home.","I am ordering lunch with my phone.","Very busy. I work twelve hours every day."], correct=3),
    dict(q="A: Where did you get this snowboard? B: ___", options=["I lent it to my cousin.","I sent you the snowboard.","I made a snowboard for you.","I borrowed it from my cousin."], correct=3),
    dict(q="A: ___ B: It is rainy.", options=["Is it cold in winter?","Does it rain a lot in spring?","What's the weather like?","How was the weather yesterday?"], correct=2),
    dict(q="A: Do you have snow in winter? B: ___", options=["No. It is snowing now.","Yes, it was snowy all day.","No, I don't see any snow there.","No, it's not that cold here in winter."], correct=3),
    dict(q="A: Oh, I'm so hungry. B: Here. You can have my hamburger. A: Really? ___", options=["You are so mad.","That's kind of you.","It's coming right up.","In fact, it is yummy."], correct=1),
  ]),
  dict(type="guided", title="四、依提示作答", meta="12分，每題3分", items=[
    dict(prompt="Can you lend me your gloves?", hint="（加入to改寫句子，句意不變）", answer="Can you lend your gloves to me?"),
    dict(prompt="It is <u>sunny but windy</u> today.", hint="（依畫線部分造原問句）", answer="What's the weather like today? / How's the weather today?"),
    dict(prompt="We usually have a lot of rain in spring.", hint="（用There改寫句子）", answer="There is usually a lot of rain in spring."),
    dict(prompt="The teacher showed us <u>some paintings</u>.", hint="（將畫線部分改為代名詞改寫）", answer="The teacher showed them to us."),
  ]),
  dict(type="translation", title="五、翻譯", meta="9分，每題3分", items=[
    dict(zh="上個星期下了幾天的雪。（用It...造句）", answer="It snowed for a few / some days last week."),
    dict(zh="這個暑假你去臺灣旅行玩得怎麼樣？", answer="How was your trip to Taiwan this summer vacation?"),
    dict(zh="我可以向你借這件夾克嗎？", answer="Can I borrow this / the jacket from you?"),
  ]),
  dict(type="cloze", title="六、克漏字選擇", meta="10分，每題2分",
    passage="___1___,\nI ___2___ the comic books and the chocolate last Friday. Thanks a lot for the gifts. That was very sweet ___3___ you. I love them very much. I had a great time last Saturday. Here are some pictures ___4___ me with my friends. I was so happy because all my good friends came to my birthday party. When can you visit us in Australia? We can take you to many great places here. I miss you ___5___.\nLove,\nCeline",
    items=[
      dict(options=["Aunt","For Aunt Flo","Dear Aunt Flo","Good morning"], correct=2),
      dict(options=["got","sent","gave","bought"], correct=0),
      dict(options=["by","for","of","with"], correct=2),
      dict(options=["in","of","for","with"], correct=1),
      dict(options=["lot","a lot","lots of","a lot of"], correct=1),
  ]),
  dict(type="reading", title="七、根據圖表選出正確的答案", meta="4分，每題2分", passages=[
    dict(label="Here is the weather in some cities in Taiwan for today.", text="", image="images/test1c/q7_weather.png",
      items=[
        dict(q="How is the weather in Hualien today?", options=["It's cool and rainy.","It's hot and sunny.","It's cold and snowy.","It's warm and cloudy."], correct=3),
        dict(q="What is the weather like in Taipei?", options=["It's hot and rainy.","It's cold and rainy.","It's hot and windy.","It's warm and sunny."], correct=0),
      ]),
  ]),
  dict(type="reading", title="八、閱讀測驗", meta="15分，每題5分", passages=[
    dict(label="", text="    Hi, there. I am Eric Miller. Let's take a look at today's weather in Waycross. The weather is warm in the morning and hot in the afternoon, with temperatures of 26°C to 31°C. You can expect cloudy to sunny skies during the day but rain at night. At night, the temperature may fall to 12°C. So, take an umbrella and a heavy jacket with you at night. That's it for today. Up next is the TWB basketball game.\n\n【字詞】temperature 溫度　expect 預期　high 高的",
      items=[
        dict(q="What is the high temperature in Waycross today?", options=["10°C.","15°C.","26°C.","31°C."], correct=3),
        dict(q="Today at 7:30 p.m., Amy is in the park in Waycross. What does she need?", options=["Pictures.","Snow gloves.","A postcard.","An umbrella."], correct=3),
        dict(q="David lives in Waycross. He is watching the weather report. What might he wear today?", image="images/test1c/q8_clothes.png", options=["A","B","C","D"], correct=2),
      ]),
  ]),
]
