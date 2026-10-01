META = dict(n=11, h1="第11回・Review Test 3", subtitle="Unit 5～Unit 6 總複習")
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="【A部分 基礎題】11分，每題1分", items=[
    dict(q="Kevin jogs a___g the river bank every evening.", answer="along"),
    dict(q="A: You know what? The new shop on the street c___er sells candy. B: Nice. I can buy some on my way home.", answer="corner"),
    dict(q="Vicky hurt her leg last week. She's still in the h___al.", answer="hospital"),
    dict(q="The skirt is on s___e. It was NT$1,680, but now it's NT$890.", answer="sale"),
    dict(q="Street food is yummy and ch___p. You don't need to spend a lot of money to get good food.", answer="cheap"),
    dict(q="A: This T-shirt cost me NT$1,500. B: That's e___ve. I wouldn't pay that much for a T-shirt.", answer="expensive"),
    dict(q="A: Are you married（已婚的）? B: Yes. See the r___g on my finger（手指）?", answer="ring"),
    dict(q="A: How was your trip to Australia? B: It was great. I had a w___ul time there.", answer="wonderful"),
    dict(q="I'm going to the su___t. I need some milk and eggs.", answer="supermarket"),
    dict(q="A: You need to wear a s___er. It's cold. B: Don't worry. I have my coat with me.", answer="sweater"),
    dict(q="Claire's dog started barking（吠叫）when it heard the s___d of her scooter.", answer="sound"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="26分，每題2分", items=[
    dict(q="A: ___ will it take to cook the chicken soup? B: Around twenty minutes.", options=["How long","How soon","How often","What time"], correct=0),
    dict(q="It ___ me ten thousand dollars to fix the truck.", options=["cost","paid","took","spent"], correct=0),
    dict(q="It ___ Irene two years ___ writing the book.", options=["took; to finish","took; finishing","spent; to finish","spent; finishing"], correct=0),
    dict(q="Ray paid a thousand dollars ___ his new hat.", options=["at","on","in","for"], correct=3),
    dict(q="Jessica spends too much time ___ video games.", options=["play","plays","to play","playing"], correct=3),
    dict(q="Daniel left the house at 5:50 a.m. ___ the first bus to Taipei.", options=["catch","caught","to catch","catching"], correct=2),
    dict(q="The concert starts at 7:30, but we need to get to the concert before six. There ___ a lot of people there tonight.", options=["will","were","will be","are going to have"], correct=2),
    dict(q="A: Did you fly to Jingoo Island? B: No. We ___ a ship.", options=["sat","got","made","took"], correct=3),
    dict(q="A: ___ you going surfing next week? B: No. I plan to go biking.", options=["Do","Are","Will","Were"], correct=1),
    dict(q="A: ___ do you spend ___ new clothes every year? B: About 3,000 dollars.", options=["How many; on","How much; on","How much; for","How many; for"], correct=1),
    dict(q="A: ___ do we get to the fire station? B: Just go straight for three blocks. It's on your left.", options=["Why","What","How","When"], correct=2),
    dict(q="A: Will you take Joseph to the beach after he ___ breakfast? B: No. I'll take him to the market nearby.", options=["had","has","will have","is having"], correct=1),
    dict(q="A: Can we take ___ metro there? B: No, but we can go ___ train.", options=["×; on","the; by","×; on a","the; by a"], correct=1),
  ]),
  dict(type="mc", title="三、對話選擇", meta="6分，每題2分", items=[
    dict(q="A: What do you think about this belt? B: It's nice, and the price isn't too bad. A: Okay. ___", options=["It's really ugly.","It's not on sale.","I'll take it then.","Have a nice day!"], correct=2),
    dict(q="A: What street are we on now? Oh no! ___ B: Don't worry. We can look at the map here.", options=["Are we lost?","Isn't that funny?","Is it on the corner?","Did it take too long?"], correct=0),
    dict(q="A: Excuse me. ___ B: Turn left here, walk down First Street, and you will see one.", options=["Where is your favorite restaurant?","Is this the right way to Sunny Bank?","Is there a swimming pool around here?","How do I get to the Big Screen Movie Theater?"], correct=2),
  ]),
  dict(type="guided", title="四、看圖詳答問題", meta="4分，每題2分", items=[
    dict(prompt="What will they do this Saturday?", hint="（看圖回答）", image="images/test11/sec4_1.png", answer="They will go mountain climbing / go hiking (this Saturday)."),
    dict(prompt="How did the man go to work today?", hint="（看圖回答）", image="images/test11/sec4_2.png", answer="He rode a motorcycle (to work). / He went (to work) by motorcycle."),
  ]),
  dict(type="guided", title="五、依提示作答", meta="4分，每題2分", items=[
    dict(prompt="She spent ten minutes walking to the post office.", hint="（用take改寫）", answer="It took her ten minutes to walk to the post office."),
    dict(prompt="We will go sailing <u>next month</u>.", hint="（依畫線部分造原問句）", answer="When will you go sailing?"),
  ]),
  dict(type="translation", title="六、整句式翻譯", meta="8分，每題4分", items=[
    dict(zh="Joan 將要在後天買一輛腳踏車。（be going to）", answer="Joan is going to buy a bike / bicycle the day after tomorrow."),
    dict(zh="步行環遊臺灣是一個很棒的經驗。（It was... travel... foot）", answer="It was a great / wonderful experience to travel around Taiwan on foot."),
  ]),
  dict(type="mc", title="一、單題", meta="【B部分 活用題】9分，每題3分", items=[
    dict(q="Look at the sign. It says ___.", image="images/test11/b1_sign.png", options=["Turn Left","Turn Right","Go Straight and Turn Right","Go Straight or Turn Left Only"], correct=3),
    dict(q="A button（鈕扣）___ off Chris's shirt when he was exercising.", options=["got","came","took","turned"], correct=1),
    dict(q="A: Are you going to the party with us later? B: ___, but I can't. Maybe next time.", options=["I'll go","I'm going","I did go","I'd love to go"], correct=3),
  ]),
  dict(type="cloze", title="二、克漏字選擇", meta="12分，每題3分",
    passage="Roy: Excuse me. ___1___ The name is Super Day Hotel.\nPam: There is a hotel on Calvary Road, but I'm not sure about the name.\nRoy: It's okay. I can go check it out. ___2___\nPam: We are on Wilson Road now. To get to Calvary Road, you need to go down the road for four blocks and make a left turn on Malibu Street. Walk along Malibu Street until you see Calvary Road. Then you make another left turn. The hotel is on your right.\nRoy: How long does it take to walk there?\nPam: It is a little far from here. ___3___\nRoy: Wow. ___4___\nPam: No. No buses go to Calvary Road from here.\nRoy: All right. Thank you so much.\n\n【字詞】until 直到　far 遠的",
    items=[
      dict(options=["I'm looking for a hotel.","I'm lost, and I don't have a map.","Is there a hotel on Wilson Road?","How much does it cost for a night at the hotel?"], correct=0),
      dict(options=["Which road is the hotel on?","How do I get to Calvary Road?","Is there another hotel around here?","How many hotels are there on Calvary Road?"], correct=1),
      dict(options=["It won't take me too long.","It takes about 20 minutes.","You won't have enough time.","I spent an hour looking for it."], correct=1),
      dict(options=["Can I take a bus there?","How soon will the bus come?","Do I need to pay for the bus ride?","When did you last take a bus there?"], correct=0),
  ]),
  dict(type="reading", title="三、依短文或圖表選出適當的答案", meta="20分，每題4分", passages=[
    dict(label="【A】", text="", image="images/test11/b3_map.png",
      items=[
        dict(q="Freddie just got some drinks from the tea shop. Now, he is going to get some fish at the fish market. Which way can he take to save time?", options=["Go down Oak Street for two blocks.","Take Oak Street and turn left on River Road.","Go along Fox Road and turn left on Stone Street.","Go down Fox Road and turn right on Mill Street."], correct=3),
        dict(q="<div style=\"background:#fff;border:1px solid var(--paper-line);border-radius:8px;padding:10px 14px;font-style:italic;margin-bottom:8px;\">Emma: Excuse me. How do I get to City Library?<br>Man: Go along this street and turn left on River Road. Go straight for three blocks. It's on your left.<br>Emma: Thank you so much.</div>Where is Emma?", options=["At First Bank.","At Nice Hotel.","At ABC Bookstore.","At Children's Hospital."], correct=1),
      ]),
    dict(label="【B】", text="Jack and Clara are now at Fords, and they heard an announcement.\n\n    Welcome to Fords. We are having a special sale for a special time like this. On the ground floor, we have great offers on women's shoes. There, you can buy shoes for half price. On the first floor, we have women's wear. There, you save 60% when you spend over NT$3,500. On the second floor, you can find men's wear. Go check it out and save 70%. On the third floor, you can buy three T-shirts and get one free in kids' wear. Don't forget to stop by the fourth floor to enjoy yummy food at different restaurants. Thank you for coming to Fords today. Enjoy your shopping here.\n\n【字詞】announcement 廣播　offer 折扣　over 超過　forget 忘記",
      items=[
        dict(q="What might Fords be?", options=["A hospital.","A restaurant.","A night market.","A department store."], correct=3),
        dict(q="Which is the floor guide（導覽）for Fords?", options=[
          "4F Kids' Wear／3F Men's Wear／2F Women's Wear／1F Women's Shoes／GF Food",
          "4F Food／3F Kids' Wear／2F Women's Wear／1F Men's Wear／GF Women's Shoes",
          "4F Food／3F Kids' Wear／2F Men's Wear／1F Women's Wear／GF Women's Shoes",
          "4F Coming Soon／3F Food／2F Kids' Wear／1F Men's Wear／GF Women's Shoes / Women's Wear"], correct=2),
        dict(q="Clara is looking at a pair of shoes at Fords. The price tag（標籤）on the shoes says NT$3,800. Clara can get the shoes at a better（較好的）price because of the sale at Fords. How much will Clara need to pay for those shoes?", options=["NT$800.","NT$1,800.","NT$1,900.","NT$3,500."], correct=2),
      ]),
  ]),
]
