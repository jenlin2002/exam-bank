META = dict(n=10, h1="第10回・Unit 6", subtitle="I'll Take Two Pairs of Gloves")
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="22分，每題2分", items=[
    dict(q="Dad is not home now, but he'll be back in a s___d.", answer="second"),
    dict(q="I need to buy a pair of p___ts; I only have old jeans.", answer="pants"),
    dict(q="A: Is this ring e___ve? B: Not really. It only costs NT$100.", answer="expensive"),
    dict(q="A: The apples are 195 NT dollars. B: Here is 200 NT dollars, and you can keep the ch___ge.", answer="change"),
    dict(q="The p___ce of this coat is too high. I don't want to pay that much for a coat.", answer="price"),
    dict(q="The worker h___t his back when he moved these heavy boxes. Now he needs to rest for a few days.", answer="hurt"),
    dict(q="To see the road signs, I always wear my g___ses when I drive.", answer="glasses"),
    dict(q="Mrs. Bean paid three th___d and eight hundred dollars for her son's clothes.", answer="thousand"),
    dict(q="Today is August 5; the day after t___w is August 7.", answer="tomorrow"),
    dict(q="Today is very cold. Put on a heavy s___r or a jacket before you go out.", answer="sweater"),
    dict(q="A: Is Lisa's Christmas party today? B: Yes, it's t___t. It starts at 7 p.m.", answer="tonight"),
  ]),
  dict(type="mc", title="二、語法選擇", meta="20分，每題2分", items=[
    dict(q="We need to ___ our shoes before we go into the house.", options=["get off","take off","come off","turn off"], correct=1),
    dict(q="A: How much do the socks ___? B: NT$100.", options=["pay","spend","take","cost"], correct=3),
    dict(q="Betty and her sister ___ to wear pink dresses to their grandma's birthday party.", options=["going","will go","is going","are going"], correct=3),
    dict(q="My family ___ go camping this weekend because it ___ rainy.", options=["aren't; will","won't; be","aren't; is","won't; will be"], correct=3),
    dict(q="A: Where ___ the Jenkins going to have dinner? B: At the department store.", options=["will","is","are","do"], correct=2),
    dict(q="The Smiths spent one hour ___ in the sea last Sunday.", options=["surf","to surf","surfed","surfing"], correct=3),
    dict(q="A: ___ did it take you to walk to the post office from the bus stop? B: About 30 minutes.", options=["How long","How soon","How many","How much"], correct=0),
    dict(q="It usually ___ Emily three and a half hours to climb up the mountain.", options=["spends","takes","costs","pays"], correct=1),
    dict(q="I didn't ___ for the jacket ___ cash because I didn't have enough money with me.", options=["pay; in","pay; by","spend; in","spend; by"], correct=0),
    dict(q="A: How may I help you? B: I would ___ to have a cup of coffee.", options=["need","want","like","plan"], correct=2),
  ]),
  dict(type="mc", title="三、對話選擇", meta="10分，每題2分", items=[
    dict(q="A: What do you think of this T-shirt? B: ___", options=["It's on sale.","It's a little ugly.","I'll take this one.","It's 300 dollars in total."], correct=1),
    dict(q="A: How would you like to pay? B: ___", options=["By card.","That's all.","I have no cash.","It's 980 dollars."], correct=0),
    dict(q="A: ___ B: It's NT$2,560.", options=["Here's your change.","How much is the total?","How much are the jeans?","How much will you spend on it?"], correct=1),
    dict(q="A: ___ B: I always spend it with my cousin.", options=["How long will you be there?","Who will go shopping with you?","Where will you spend the holiday?","Who will you spend the holiday with?"], correct=3),
    dict(q="A: How much did the sweater cost? B: ___", options=["It costs a lot.","It cost NT$900.","I paid NT$800 for them.","I spend two hours in the store."], correct=1),
  ]),
  dict(type="guided", title="四、依提示作答", meta="9分，每題3分", items=[
    dict(prompt="David paid NT$250 for the belt.", hint="（用spend改寫）", answer="David spent NT$250 on the belt."),
    dict(prompt="This pair of yellow shorts costs <u>$290</u>.", hint="（依畫線部分造原問句）", answer="How much does this pair of yellow shorts cost?"),
    dict(prompt="Sam usually spends ten minutes jogging from the hill to the beach.", hint="（用It... to... 改寫句子）", answer="It usually takes Sam ten minutes to jog from the hill to the beach. / It usually takes ten minutes for Sam to jog from the hill to the beach."),
  ]),
  dict(type="guided-multi", title="五、引導式翻譯", meta="14分，每格1分", items=[
    dict(zh="快時尚背後的真相可能非常醜陋。", lines=["The truth {{behind}} {{fast}} fashion can be very {{ugly}}."]),
    dict(zh="多虧有你，我們可以用低價買這些玩具。", lines=["Thanks to you, we can buy these toys {{at}} {{low}} {{prices}}."]),
    dict(zh="A：我要買三雙手套。B：好的。總共是一千元。", lines=["A: I'd like three {{pairs}} of gloves. B: OK. The {{total}} is one {{thousand}} dollars."]),
    dict(zh="在那個國家，許多工人一小時的工作只賺約新臺幣五元。", lines=["In that country, many workers {{make}} only about five NT dollars {{for}} an hour's work."]),
    dict(zh="那間公司將藉著使用廉價勞工來維持低價。", lines=["The company will {{keep}} prices low {{by}} using {{cheap}} workers."]),
  ]),
  dict(type="reading", title="六、克漏字選擇", meta="9分，每題3分", passages=[
    dict(label="", text="Dear Jane,                                                    Wed., Sep. 2\nI can't wait to see you this Saturday! The weather in New York is nice this week. Some people are wearing T-shirts and shorts. However, you need to bring a jacket or a coat because it can be cold at night. Also, bring a nice dress because I'm taking you to a fashion show. And of course, we'll also go to the theater to watch some great plays. By the way, can you buy some Taiwanese snacks for me? I want to give <u>them</u> to my students and friends here. See you soon!\nYour friend,\nEric\n\n【字詞】bring 帶來　Taiwanese 臺灣的　true 真實的",
      items=[
        dict(q="Why did Eric write this postcard to Jane?", options=["To tell her about his trip.","To talk about bad weather.","To ask for Taiwanese snacks.","To tell her about his plans for her visit."], correct=3),
        dict(q="What does <u>them</u> mean?", options=["T-shirts.","Nice dresses.","Warm coats.","Taiwanese snacks."], correct=3),
        dict(q="Which is NOT true?", options=["Eric teaches in New York.","Jane won't need heavy clothes in New York.","Eric and Jane will go to the theater to watch plays.","Eric wants Jane to wear a dress for the fashion show."], correct=1),
      ]),
  ]),
  dict(type="reading", title="七、閱讀測驗", meta="16分，每題4分", passages=[
    dict(label="", text="【字詞】furniture 家具　address 地址　in three installments 分三期（三個月）付款", image="images/test10c/r_ad.png",
      items=[
        dict(q="What is Joy House trying to do?", options=["Tell people to change their lives.","Tell people to buy a good house.","Tell people to go shopping at Joy House.","Tell people the open hours of Joy House."], correct=2),
        dict(q="Gary needs some plates for his dinner party next Saturday. He has one thousand two hundred dollars. How many plates can he buy?", options=["Twelve.","Ten.","Eight.","Six."], correct=1),
        dict(q="Joyce just moved to a new house. She is buying the desk and the sofa at the sale. How much is she going to pay every month?<div style=\"background:#fff;border:1px solid var(--paper-line);border-radius:8px;padding:10px 14px;font-style:italic;margin:8px 0;\">Joyce: I'll take the desk and the sofa. And I'd like to pay by card. Can I pay in three installments?<br>Clerk: Sure.<br>Joyce: Great. Here is the card.</div>", options=["NT$3,500.","NT$7,000.","NT$21,000.","NT$30,000."], correct=1),
        dict(q="Which is true about the sale?", options=["It's a summer sale.","It lasts for three weeks.","It ends at the end of April.","You can shop there before 11 a.m."], correct=3),
      ]),
  ]),
]
