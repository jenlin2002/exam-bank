META = dict(n=10, h1="第10回・Unit 5", subtitle="What's the Date?")
I = "images/test10/"
CROPS = [("p1",20,(98,82,195,190)), ("p2",20,(98,192,200,300)), ("p3",20,(98,302,200,400)), ("phone",20,(632,745,968,1310))]
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="【A部分 基礎題】每格1分，共9分", items=[
    dict(q="A: What is the third month of the year? B: It's M___h.", answer="March"),
    dict(q="Today is January 2, the s___d day of the year.", answer="second"),
    dict(q="A: What's the month before October? B: It's S___r.", answer="September"),
    dict(q="A: Is Andrew's birthday in Ju___y? B: No. It's in A___t.", answers=["July","August"]),
    dict(q="It's 7:30 p.m., and everybody is eating d___r.", answer="dinner"),
    dict(q="A: Please be nice to Mr. Eastwood. He is very im___t to us. B: Yes, Mrs. Pierce.", answer="important"),
    dict(q="A: What a___ls can we see on your grandma's farm? B: C___ws, pigs, and maybe turkeys.", answers=["animals","Cows"]),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共20分", items=[
    dict(q="A: ___ the date today? B: It's ___ November 26.", options=["What's; ×","When's; ×","When's; on","What's; on"], correct=0),
    dict(q="A: Isn't Quinn's birthday ___ April? B: Yes. Her birthday is ___ April 1.", options=["in; on","in; at","on; in","at; in"], correct=0),
    dict(q="Glenn is Mr. and Mrs. McCarthy's ___ son.", options=["third","the third","three","the three"], correct=0),
    dict(q="A: What's today's date? B: It's June ___.", options=["twenty-five","twenty-fifth","twenty and five","twentieth and fifth"], correct=1),
    dict(q="A: When is the new year party? B: It's ___ December 29.", options=["for","at","in","on"], correct=3),
    dict(q="October is ___ tenth month of the year.", options=["×","a","one","the"], correct=3),
    dict(q="A: ___ is Mother's Day this year? B: It's May 12.", options=["What date","What day","What time","What month"], correct=0),
    dict(q="Today is the eighth ___ February.", options=["in","of","at","on"], correct=1),
    dict(q="A: ___ Mason's first day of school? B: It's September 3.", options=["When is","What is","What day is","What time is"], correct=0),
    dict(q="A: Jessie, do not run ___ in the classroom, please. B: Sorry, Mr. Burton.", options=["off","with","above","around"], correct=3),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共8分", items=[
    dict(q="A: When is the welcome party for Peggie? B: ___", options=["It's October.","It's ten thirty.","It's Friday today.","It's on November 6."], correct=3),
    dict(q="A: I am having fish for dinner. ___ B: I am having turkey.", options=["Isn't it great?","How about you?","Can we go around the table?","Is the turkey for your dinner?"], correct=1),
    dict(q="A: What's the date today? B: ___", options=["It's on October 21.","It's Wednesday today.","Today is Mother's Day.","Today is December 25."], correct=3),
    dict(q="A: ___ B: It's on Saturday night.", options=["What day is today?","When is the concert?","What's the date today?","What date is the concert?"], correct=1),
  ]),
  dict(type="guided-multi", title="四、填入正確的介系詞", meta="每格1分，共6分", items=[
    dict(zh="", lines=["A: Isn't the writer's meet-and-greet this month? B: No. It's {{in}} April."]),
    dict(zh="", lines=["A: When is Thanksgiving? B: Thanksgiving is {{on}} the fourth Thursday {{of/in}} November."]),
    dict(zh="", lines=["A: When is the welcome party? B: It's {{on}} the evening {{of}} May 15."]),
    dict(zh="", lines=["A: Is June {{before}} July? B: Yes, it is."]),
  ]),
  dict(type="cloze", title="五、克漏字選擇", meta="每題2分，共10分",
    passage="Hello, I am Oliver. I am from Australia. Today is ___1___, the day after Christmas. It is Boxing Day, a popular ___2___ in Australia. Now, my family and I are at my grandpa's house. Dad and Cousin Greg are watching cricket on TV. Cricket games on Boxing Day are very ___3___ to cricket fans. Boxing Day is ___4___ a big day for shoppers. Mom and Aunt Josephine are shopping online. What am I doing now? I'm drinking and eating with Grandpa. Everyone is having a great time on Boxing Day. This is my favorite time ___5___.\n\n【字詞】cricket 板球　shopper 購物者　shop 購物　online 線上",
    items=[
      dict(options=["December 24","December 25","December 26","December 27"], correct=2),
      dict(options=["eve","holiday","month","birthday"], correct=1),
      dict(options=["lucky","nervous","thankful","important"], correct=3),
      dict(options=["also","only","before","about"], correct=0),
      dict(options=["in year","next year","of the year","around the year"], correct=2),
  ]),
  dict(type="guided", title="六、看圖詳答問題（日期須寫出英文讀法）", meta="每題2分，共6分", items=[
    dict(prompt="What's the date today?", hint="（看圖回答）", image=I+"p1.png", answer="It's February twelfth."),
    dict(prompt="What date is the baseball game?", hint="（看圖回答）", image=I+"p2.png", answer="It's on January thirtieth."),
    dict(prompt="Is it October twenty-first today?", hint="（看圖回答）", image=I+"p3.png", answer="No, it's not. It's October twenty-second."),
  ]),
  dict(type="guided", title="七、依提示作答", meta="每題3分，共6分", items=[
    dict(prompt="Today is <u>April 27</u>.", hint="（依畫線部分造原問句）", answer="What's the date today? / What is today's date?"),
    dict(prompt="The movie party is <u>on February 13</u>.", hint="（依畫線部分造原問句）", answer="What date / When is the movie party?"),
  ]),
  dict(type="translation", title="八、整句式翻譯", meta="每題3分，共9分", items=[
    dict(zh="聖誕夜是幾月幾日？", answer="When / What date is Christmas Eve?"),
    dict(zh="我的生日派對在十一月二十四號。", answer="My birthday party is on November twenty-fourth."),
    dict(zh="父親節是在六月的第三個星期日嗎？", answer="Is Father's Day on the third Sunday of / in June?"),
  ]),
  dict(type="mc", title="一、單題", meta="【B部分 活用題】每題2分，共8分", items=[
    dict(q="A: ___ Christmas is coming. B: Yes! I can't wait.", options=["Is it December 25?","When is Christmas?","Today is December 22.","Can you wait for me, please?"], correct=2),
    dict(q="A: What date is the day before New Year's Eve? B: ___", options=["January 1.","January 2.","December 30.","December 31."], correct=2),
    dict(q="March 16 is my brother's ___ birthday.", options=["eight","eighth","the eight","the eighth"], correct=1),
    dict(q="There are（有）only twenty-eight days in ___.", options=["January","February","March","December"], correct=1),
  ]),
  dict(type="reading", title="二、依短文或圖表選出適當的答案", meta="每題3分，共18分", passages=[
    dict(label="【A】", text="Melanie: What are you doing for Thanksgiving this year?\nRandy: My family and I are giving food to the homeless people the day before Thanksgiving. Those people are not <u>fortunate</u> like us. We can have a big dinner in a nice house with our family on Thanksgiving, but they can't.\nMelanie: That's really nice of you. Is it next Wednesday?\nRandy: Yes. It's on the 27th.\nMelanie: I am free that day. Can I come, too?\nRandy: Sorry. It's a family event. Only my family can go that day. How about the Saturday before Thanksgiving? Food & Friends is giving food to the homeless people every day, and my family and I are there every weekend.\nMelanie: Sure. You really are a good person.\n\n【字詞】food 食物　homeless 無家可歸的　like 像　event 活動；事件　every 每一", items=[
      dict(q="\"Fortunate\" means（意指）___.", options=["nice","lucky","nervous","important"], correct=1),
      dict(q="When is Melanie meeting Randy at Food & Friends?", options=["On November 23.","On November 24.","On November 27.","On November 28."], correct=0),
      dict(q="Which（哪一個）is true（真實的）?", options=["Melanie is only free this weekend, not next Wednesday.","Randy is at Food & Friends every weekend with his family.","The homeless people can only have food around Thanksgiving.","Randy's family is giving food to the homeless on November 26."], correct=1),
    ]),
    dict(label="【B】This is Mr. White's phone, and these are important events for Mr. White this month.", text="", image=I+"phone.png", items=[
      dict(q="What is the date today?", options=["September 22.","September 25.","September 29.","September 30."], correct=0),
      dict(q="Walter's basketball game is NOT ___.", options=["next Tuesday","at Pollo Park","in the afternoon","on September 28"], correct=2),
      dict(q="Which is true?", options=["Holly is only one month old.","Jessy's birthday is two days from now.","Mr. White is having dinner with Skyler next week.","Holly's birthday is four days after Walter's basketball game."], correct=2),
    ]),
  ]),
]
