META = dict(n=10, h1="第10回・Unit 6", subtitle="I'll Take Two Pairs of Gloves")
BOX = "<div style=\"background:#fff;border:1px solid var(--paper-line);border-radius:8px;padding:10px 14px;margin-bottom:8px;\">"
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="【A部分 基礎題】13分，每格1分", items=[
    dict(q="Don't lose hope. T___w is another day.", answer="Tomorrow"),
    dict(q="It was cold, so Chris decided to put on a s___r.", answer="sweater"),
    dict(q="The video was f___y, and everyone laughed（大笑）when they watched it.", answer="funny"),
    dict(q="Victor won't go to baseball practice today because he h___t his arm.", answer="hurt"),
    dict(q="I'm not going to buy that cap. Its p___e is too high.", answer="price"),
    dict(q="My feet are big. These s___es are too small for me.", answer="shoes"),
    dict(q="A: Today is Friday. Do you have any plans t___t? B: Yes. I'll go to the movies with my sister at 7 p.m.", answer="tonight"),
    dict(q="I can't see clearly（清楚地）with my g___ses; I need to buy a new pair.", answer="glasses"),
    dict(q="They knocked down（拆除）u___y old buildings and built beautiful new ones.", answer="ugly"),
    dict(q="A: How many students are there in the classroom? B: There are 31 students in t___l.", answer="total"),
    dict(q="The computer is not e___e. It costs only ten t___d NT dollars.", answers=["expensive","thousand"]),
    dict(q="They didn't want others to hear them, so they spoke in a l___w voice（聲音）.", answer="low"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="32分，每題2分", items=[
    dict(q="It took Louis four years ___ this painting.", options=["finish","finished","to finish","finishing"], correct=2),
    dict(q="It cost Hank a lot of money ___ the house.", options=["fix","to fix","fixed","fixing"], correct=1),
    dict(q="There ___ three soccer games in early July.", options=["will","will have","are going to be","are going to have"], correct=2),
    dict(q="Calvin ___ out with his aunt tomorrow evening.", options=["eats","ate","was eating","will eat"], correct=3),
    dict(q="Dan is going to get some sleep, but his wife ___.", options=["won't","doesn't","wasn't","isn't"], correct=3),
    dict(q="The children's concert tomorrow ___ a lot of fun.", options=["was","will be","will have","is going to have"], correct=1),
    dict(q="Joe will visit his grandpa after he ___ to the dentist.", options=["went","goes","is going","will go"], correct=1),
    dict(q="___ going to ___ a welcome party next week.", options=["We're; have","We'll; have","We're; having","We'll; having"], correct=0),
    dict(q="Stella is going to wash her car ___ weekend.", options=["on","at","last","next"], correct=3),
    dict(q="Mrs. Barr spends NT$5,000 ___ dog food every month.", options=["on","in","at","with"], correct=0),
    dict(q="The Waldorf family will go to Kenya ___ half a year.", options=["in","at","with","from"], correct=0),
    dict(q="___ the first train to Hualien, the sisters got up before 5 a.m. today.", options=["Catch","To catch","Caught","On catching"], correct=1),
    dict(q="___ exercising three times a week, Kevin is now healthy and strong.", options=["At","On","By","From"], correct=2),
    dict(q="Ben is tired. He spent five hours ___ the house.", options=["clean","cleans","to clean","cleaning"], correct=3),
    dict(q="Jane has really long hair. Washing her hair always ___ her a lot of time.", options=["has","gets","takes","spends"], correct=2),
    dict(q="A: ___ did it take you to design the game? B: Two months.", options=["How soon","How long","How often","What time"], correct=1),
  ]),
  dict(type="mc", title="三、對話選擇", meta="6分，每題2分", items=[
    dict(q="A: Remember to give me a call. B: ___ Talk to you later.", options=["I will.","That's funny.","How nice of you!","Do you need anything?"], correct=0),
    dict(q="A: How would you like to pay, sir? B: ___ I don't have enough cash.", options=["That's all.","Isn't it on sale?","I'll pay by card.","I bought it at a low price."], correct=2),
    dict(q="A: The socks are NT$30 a pair. B: That's cheap. ___ A: Here you go.", options=["I'll take two.","I'll take them off.","Have a nice day!","Here's your change."], correct=0),
  ]),
  dict(type="guided", title="四、看圖詳答問題", meta="6分，每題3分", items=[
    dict(prompt="Ken bought the hat. How much did he pay for it?", hint="（看圖回答）", image="images/test10/sec4_1.png", answer="He paid $699 / 699 dollars for it."),
    dict(prompt="Will the girl wear jeans to the party?", hint="（看圖回答）", image="images/test10/sec4_2.png", answer="No, she won't. She will wear a skirt (to the party)."),
  ]),
  dict(type="guided", title="五、依提示作答", meta="6分，每題2分", items=[
    dict(prompt="The tie cost him <u>2,000 dollars</u>.", hint="（依畫線部分造原問句）", answer="How much did the tie cost him?"),
    dict(prompt="It took me three days to make this ring.", hint="（用spend改寫）", answer="I spent three days making this ring."),
    dict(prompt="It takes <u>an hour</u> to fly from here to Taiwan.", hint="（依畫線部分造原問句）", answer="How long does it take to fly from here to Taiwan?"),
  ]),
  dict(type="translation", title="六、整句式翻譯", meta="8分，每題4分", items=[
    dict(zh="你將會借一條長褲給我嗎？（Are you...）", answer="Are you going to lend a pair of pants to me / me a pair of pants?"),
    dict(zh="脫掉這件長洋裝要三分鐘。（It will...）", answer="It will take three minutes to take off this long dress / take this long dress off."),
  ]),
  dict(type="mc", title="一、單題", meta="【B部分 活用題】6分，每題2分", items=[
    dict(q="Look at the picture. The ___ and the ___ are on sale.", image="images/test10/b1_sale.png", options=["socks; tie","shoes; belt","shorts; cap","glasses; ring"], correct=1),
    dict(q="A: Do you want to try this dress on? B: ___ Isn't that Mom's dress?", options=["That's cheap.","Wait a second.","I won't take it off.","Don't say anything."], correct=1),
    dict(q="The music festival is popular. There are ___ of people there now.", options=["thousand","thousands","the thousand","one thousand"], correct=1),
  ]),
  dict(type="cloze", title="二、克漏字選擇", meta="8分，每題2分",
    passage="Horton: ___1___ my first job interview tomorrow.\nJanelle: Great! I'm so happy for you. ___2___\nHorton: My favorite white T-shirt and blue jeans.\nJanelle: Are you sure? Well, ___3___ job interviews, you might need to wear something formal.\nHorton: Like what?\nJanelle: Like a shirt and ___4___. Maybe a tie, too.\nHorton: A tie? I'm not trying to be a salesman. I'm trying to be a model.\nJanelle: I see. Then your choice is fine. You'll be great!\n\n【字詞】formal 正式的　model 模特兒",
    items=[
      dict(options=["I had","I'll have","I was having","I'm going to be"], correct=1),
      dict(options=["Do you need help with anything?","How fast can you change clothes?","What are you going to wear to the interview?","Are you going to shop for some new clothes?"], correct=2),
      dict(options=["on","for","with","from"], correct=1),
      dict(options=["a beautiful dress","an expensive ring","a pair of black pants","a nice pair of glasses"], correct=2),
  ]),
  dict(type="reading", title="三、依短文或圖表選出適當的答案", meta="15分，每題3分", passages=[
    dict(label="【A】Nora's Clothes Shop　Summer Sale (July 21–July 31)", text="", image="images/test10/b3_sale.png",
      items=[
        dict(q="Chelsea was at Nora's Clothes Shop this morning. She saw a short skirt, but she didn't buy it. She is going back to Nora's to buy it tomorrow because she can get it for half price. What is the date today?", options=["July 20.","July 21.","July 30.","July 31."], correct=0),
        dict(q="Matt went to Nora's Clothes Shop on July 25. He got a T-shirt and four pairs of socks. How much did he spend there?", options=["NT$633.","NT$733.","NT$800.","NT$900."], correct=2),
        dict(q="Ritz wants to shop for her mom's birthday gift during the sale, but she only has three hundred dollars. What can she buy?", options=["A skirt.","A T-shirt.","A pair of jeans.","A pair of shorts."], correct=3),
      ]),
    dict(label="【B】", text="    Do you spend a lot of money on clothes, but you still don't look good in them? Well, you don't need to spend a lot of money to look good. It's never about the price. It's all about putting clothes together. First, you need to know about colors. Some colors <u>match</u> with each other; some don't. Matching colors is not putting the same color together. It's putting different colors together, but they still look great. You can start by wearing black and white or other dark colors and white. A white T-shirt goes well with a pair of blue jeans or a black skirt. That can look good on anyone. Also, knowing your skin color is important, too. People with dark skin look great in bright colors. On the other hand, dark colors look good on people with lighter skin colors. Matching your clothes is an easy way to look good. Next week, I am going to talk more about the use of hats. See you then!\n\n【字詞】look 看起來　anyone 任何人　skin 皮膚　lighter 較淺的",
      items=[
        dict(q="When two things <u>match</u>, they ___.", options=["look cheap","look good together","are both expensive","look funny on a person"], correct=1),
        dict(q="Four people read the article（文章）and wrote down their thoughts（想法）. Who has different thoughts from the writer?"
          + BOX + "<b>Doris</b>（August 25 7:45 p.m.）<br>I like being in the sun, so my skin is very dark. I don't wear black at all because my skin doesn't look good in that color. I like wearing bright colors to look full of life.</div>"
          + BOX + "<b>Cayden</b>（August 25 11:12 a.m.）<br>Come visit my room, and you will see a lot of white T-shirts. Really, I don't have T-shirts in any other color, and I only have two pairs of jeans. One blue and one black. That's it. I don't need anything else.</div>"
          + BOX + "<b>Kayla</b>（August 20 1:56 p.m.）<br>I like white, but pink is my favorite color. What's wrong with pink on pink? I have many pink clothes. I like wearing a pink dress with pink shoes. I look like a doll, and I love it.</div>"
          + BOX + "<b>Tim</b>（August 17 9:06 p.m.）<br>This helped me a lot. Before, I always wore all black. Black T-shirt, black jeans, and black shoes—everything black. \"I look cool,\" I thought, but I was wrong. This week I started to wear a white T-shirt or white shoes with black jeans. People saw my changes and said to me, \"You look good.\"</div>",
          options=["Doris.","Cayden.","Kayla.","Tim."], correct=2),
      ]),
  ]),
]
