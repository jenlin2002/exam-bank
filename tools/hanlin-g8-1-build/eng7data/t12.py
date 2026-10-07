META = dict(n=12, h1="第12回・Review Test 3", subtitle="Unit 5～Unit 6 總複習")
I = "images/test12/"
CROPS = [("pic",24,(170,80,465,245)), ("farms",24,(65,835,565,1368)), ("cal",24,(668,1275,1095,1575))]
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="【A部分 基礎題】每格1分，共11分", items=[
    dict(q="Christmas is an important h___y in the USA.", answer="holiday"),
    dict(q="A___t is the eighth month of the year.", answer="August"),
    dict(q="A: Is there a park a___d here? B: Yes. There's one next to the zoo.", answer="around"),
    dict(q="Don't eat fried food（炸物）. It's not h___y.", answer="healthy"),
    dict(q="A: Is your baby one year old? B: No. She's o___y five months old.", answer="only"),
    dict(q="A: Can you c___n the dog house, please? It's messy（髒亂的）. B: OK.", answer="clean"),
    dict(q="A: What's your favorite a___l? My favorite is the zebra. B: My favorite is the b___r. It is big but cute.", answers=["animal","bear"]),
    dict(q="There is f___d in the kitchen. You can eat some.", answer="food"),
    dict(q="A: When is your birthday? B: It's on F___y 28.", answer="February"),
    dict(q="A: I can go to Annie Brown's concert for free（免費）. B: Wow, you are so l___ky.", answer="lucky"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共24分", items=[
    dict(q="A: ___ is Makayla's concert? B: It's ___ March 11.", options=["When; on","What day; in","What time; on","What month; in"], correct=0),
    dict(q="A: Are ___ any cows over there? B: Yes, there are.", options=["they","there","these","those"], correct=1),
    dict(q="A: ___ is Thanksgiving this year? B: November 28.", options=["What day","What date","How long","What time"], correct=1),
    dict(q="There aren't ___ pigs on Maggie's farm, but there are ___ horses there.", options=["any; any","any; some","some; some","some; any"], correct=1),
    dict(q="A: Isn't there food on the table? B: Yes, ___.", options=["it's","it is","there's","there is"], correct=3),
    dict(q="A: ___ there two lions in the zoo? B: No. There ___ only one there.", options=["Isn't; is","Is; are","Aren't; is","Are; isn't"], correct=2),
    dict(q="A: ___ is your first dance class? B: It's ___ the morning of May 14.", options=["What day; in","When; on","What time; at","What date; of"], correct=1),
    dict(q="There aren't ___ elephants near the trees. There are only two.", options=["two","any","many","some"], correct=2),
    dict(q="A: When is Ruby's baseball game? B: I am not sure. Maybe it's ___ June.", options=["at","on","in","of"], correct=2),
    dict(q="A: Are there any zebras in the zoo? B: Yes. There are ___ foxes.", options=["any","also","full","only"], correct=1),
    dict(q="A: ___ turkey for dinner today? B: No. There is only fish.", options=["Is it a","Are there","Are those","Is there any"], correct=3),
    dict(q="There are ___ rabbits and ___ horse on my grandma's farm.", options=["some; a","any; a","not any; one","not; any"], correct=0),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共8分", items=[
    dict(q="A: What's today's date? B: ___", options=["It's in January.","It's Wednesday.","It's twelve twenty-five.","It's the seventh of October."], correct=3),
    dict(q="A: The baby monkey is only two months old. ___ B: Yes! She's small and beautiful.", options=["You cannot.","So cute, right?","Let's go around.","That's new to me."], correct=1),
    dict(q="A: ___ B: No. It's March 22 today.", options=["What day is today?","Is today March 24?","Isn't today March 22?","What's the date today?"], correct=1),
    dict(q="A: Are there any rats in the kitchen? B: ___", options=["No, that is not a rat.","No, there aren't any.","Yes, there is a kitchen.","Yes, the rats are in the kitchen."], correct=1),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="每題3分，共12分",
    passage="Alena is a cute young girl. Her pets, James and Chloe, are two white mice. Today is a big day for James. It's James's ___1___ birthday. He is turning three today. Look at James. He is eating a cucumber, his favorite ___2___. Chloe is next to him. She is jumping up and down. She is very nervous ___3___ cucumbers. Maybe she is not a fan of the color green. But thanks to James, Chloe can have a big dinner today, too. With the food, James and Chloe are ___4___ and happy.\n\n【字詞】pet 寵物　turn 變成　cucumber 黃瓜",
    items=[
      dict(options=["first","second","third","fourth"], correct=2),
      dict(options=["food","help","month","back"], correct=0),
      dict(options=["at","above","from","around"], correct=3),
      dict(options=["full","clean","right","important"], correct=0),
  ]),
  dict(type="guided", title="五、依提示作答", meta="每題3分，共9分", items=[
    dict(prompt="Are there any foxes under the tree?", hint="（用「三隻」詳答）", answer="Yes, there are. There are three foxes under the tree."),
    dict(prompt="When is Mandy's birthday?", hint="（用「在十二月二號」詳答）", answer="It's on December 2. / It's on December second."),
    dict(prompt="There are some horses in the zoo.", hint="（改寫句子：將 some 改成 any）", answer="There aren't any horses in the zoo."),
  ]),
  dict(type="guided", title="六、看圖詳答問題", meta="每題3分，共9分", items=[
    dict(prompt="Are there any tigers in the picture?", hint="（看圖回答）", image=I+"pic.png", answer="Yes, there is a / one tiger in the picture."),
    dict(prompt="Are there five monkeys in the tree?", hint="（看圖回答）", image=I+"pic.png", answer="No. There are (only) three monkeys in the tree. / No, there aren't five monkeys in the tree."),
    dict(prompt="What is there under the tree?", hint="（看圖回答）", image=I+"pic.png", answer="There are two elephants under the tree."),
  ]),
  dict(type="translation", title="七、整句式翻譯", meta="每題3分，共6分", items=[
    dict(zh="我們何時能去公園？", answer="When can we go to the park?"),
    dict(zh="母親節是在五月的第二個星期日。", answer="Mother's Day is on the second Sunday of / in May."),
  ]),
  dict(type="mc", title="一、單題", meta="【B部分 活用題】每題2分，共6分", items=[
    dict(q="A: Are there any people at the party? B: Yes, there are ___.", options=["any","some","those","these"], correct=1),
    dict(q="Carl's birthday is ___ Christmas Eve. It's on December 23.", options=["also","on","the day after","the day before"], correct=3),
    dict(q="A: ___ B: It's on January first.", options=["What day is today?","What's the date today?","When is New Year's Day?","What day is New Year's Day?"], correct=2),
  ]),
  dict(type="reading", title="二、依短文或圖表選出適當的答案", meta="每題3分，共15分", passages=[
    dict(label="【A】", text="【字詞】kind 種類　bring 帶回", image=I+"farms.png", items=[
      dict(q="___ are a kind of <u>fruit</u>.", options=["Mice","Trees","Apples","Cookies"], correct=2),
      dict(q="Laura's favorite animal is the horse. On which（哪一個）farm can she see a horse?", options=["Fiona's Farm.","Kim's Farm.","House of Cuties.","Carrie's Happy Farm."], correct=2),
      dict(q='<div style="background:#fff;border:1px solid var(--paper-line);border-radius:8px;padding:10px 14px;font-style:italic;margin-bottom:8px;">Janet: There are so many special birds here. I can watch them all day.<br>Brad: Great. There are also pigs and cows on the farm. Can I go play with them?<br>Janet: Sure.</div>Which farm are Janet and Brad on?', options=["Fiona's Farm.","Kim's Farm.","House of Cuties.","Carrie's Happy Farm."], correct=0),
    ]),
    dict(label="【B】", text="(On the phone)\nTim: Hello, this is Mrs. Sarandon's office.\nPat: Hello, this is Pat Lee. Can I meet Mrs. Sarandon?\nTim: Let me have a look at Mrs. Sarandon's schedule. When is good for you, Mrs. Lee?\nPat: She's going to Poland on October 14. Right?\nTim: Yes. She will be on holiday for two weeks. She's coming back on the 28th. You can meet her on that day.\nPat: Hmm... Can I meet her this week? Is this Thursday okay?\nTim: Let's see. Thursday, October 10. She's out of the office all morning. She's free after twelve.\nPat: How about Friday?\nTim: Friday is fine, Mrs. Lee.\nPat: Nice. Is 3 p.m. okay?\nTim: Sure. See you on Friday at 3 p.m.\nPat: Thank you. Bye-bye.\n\n【字詞】let 讓　schedule 行程表　will 將會　back 返回　out 外出", items=[
      dict(q="Which is true（真實的）?", options=["Mrs. Lee is talking to Mrs. Sarandon.","Mrs. Sarandon is in Poland on October 20.","Mrs. Lee is meeting Mrs. Sarandon at night.","Mrs. Sarandon is in her office on Thursday morning."], correct=1),
      dict(q="Which is Mrs. Sarandon's schedule?", image=I+"cal.png", options=["A","B","C","D"], correct=2),
    ]),
  ]),
]
