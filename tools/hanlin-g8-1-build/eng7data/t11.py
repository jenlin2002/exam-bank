META = dict(n=11, h1="第11回・Unit 6", subtitle="There Are Some Elephants Over There")
I = "images/test11/"
CROPS = [("zoo",22,(210,312,452,500)), ("b1",22,(440,595,570,712)), ("sg",22,(670,1288,1070,1588))]
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="【A部分 基礎題】每題1分，共10分", items=[
    dict(q="Z___as are black and white animals.", answer="Zebras"),
    dict(q="T___ers are not from Africa. They are animals from Asia.", answer="Tigers"),
    dict(q="Fish is my favorite f___d.", answer="food"),
    dict(q="I am not f___l. I'm still（仍然）hungry.", answer="full"),
    dict(q="A: The box is heavy. Can you h___p me, please? B: Sure.", answer="help"),
    dict(q="The l___n is the king of the animals.", answer="lion"),
    dict(q="Mrs. Elena's car is nice and cl___n.", answer="clean"),
    dict(q="A: There is a dog at the back of your house, r___t? B: Yes. That's my grandma's dog.", answer="right"),
    dict(q="In today's w___ld, we can get to（到達）many places in a short time.", answer="world"),
    dict(q="You can help Ken on his farm. For e___e, you can feed（餵食）cows for him.", answer="example"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共24分", items=[
    dict(q="A: Are ___ three birthday cards on the desk? B: No, there aren't.", options=["they","these","there","those"], correct=2),
    dict(q="A: Isn't there a party at Mathew's place? B: Yes, ___.", options=["it's","it is","there's","there is"], correct=3),
    dict(q="A: ___ brushes on the table? B: Yes. There are two.", options=["Isn't there","Is there","Aren't these","Are there any"], correct=3),
    dict(q="There is ___ TV in Tracy's living room.", options=["no a","no the","not a","not the"], correct=2),
    dict(q="___ there any ___ in this park?", options=["Is; a fox","Is; foxes","Are; fox","Are; foxes"], correct=3),
    dict(q="A: What's that ___ there? B: That's a small bug.", options=["over","at","about","for"], correct=0),
    dict(q="There are ___ horses on the farm, but there are not ___ rabbits.", options=["some; any","any; any","some; some","any; some"], correct=0),
    dict(q="There are ___ dolls in Amanda's bedroom.", options=["no","no a","not a","not the"], correct=0),
    dict(q="There are ___ pencils and ___ eraser in my pencil case.", options=["some; any","any; an","many; any","some; an"], correct=3),
    dict(q="A: ___ there two pictures on the wall? B: No. There ___ only one.", options=["Is; is","Is; are","Are; is","Are; are"], correct=2),
    dict(q="A: Isn't there a car in front of you? B: No, ___.", options=["there is","there isn't","there are","there aren't"], correct=1),
    dict(q="A: Are there any people in front of the school? B: Yes. There are ___.", options=["no","any","one","many"], correct=3),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共8分", items=[
    dict(q="A: ___ B: Yes. There are twelve.", options=["Are these boys twelve years old?","Is there a woman in front of the house?","Are there any students on the school bus?","Aren't there twenty teachers in your school?"], correct=2),
    dict(q="A: ___ B: No, there aren't any.", options=["Isn't the horse behind the bus?","Are they Mr. Pacino's animals?","Are these pigs from Mary's farm?","Are there many elephants near the trees?"], correct=3),
    dict(q="A: ___ B: There are some comic books.", options=["What's there under John's bed?","Are John's comic books under his bed?","How many books are under John's bed?","Are there some comic books under John's bed?"], correct=0),
    dict(q="A: ___ B: One, two, three... ten. Yeah, you're right.", options=["What's that over there?","Are there any rats in the kitchen?","There aren't any tigers in the zoo.","Aren't there ten bears in the picture?"], correct=3),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="每題2分，共8分",
    passage="Hello, I'm Elena Elephant. Leon Zoo is my home. There are thirteen animals in the zoo. There are two elephants, two bears, ___1___ monkeys, and three zebras. Elijah Elephant is my brother. Betty Bear and Ben Bear are very nice to everyone. The monkey family is a cute family, and the ___2___ sisters are beautiful. Zoe Zebra and I are very good friends. Our favorite ___3___ is the green grass. Oh, wait! How can I miss Leo Lion? He is the animal king in Leon Zoo, and he is very popular. We are a big family in Leon Zoo. ___4___ every animal here, I am happy every day.\n\n【字詞】grass 青草　miss 錯過　every 每一",
    items=[
      dict(options=["two","three","four","five"], correct=3),
      dict(options=["lion","tiger","zebra","horse"], correct=2),
      dict(options=["bug","help","back","food"], correct=3),
      dict(options=["For","Luckily","Thanks to","A big help from"], correct=2),
  ]),
  dict(type="guided", title="五、依提示作答", meta="每題3分，共9分", items=[
    dict(prompt="Are there any monkeys in the tree?", hint="（否定簡答）", answer="No, there aren't (any)."),
    dict(prompt="Is there a brown bear behind me?", hint="（肯定詳答）", answer="Yes, there is a brown bear behind you."),
    dict(prompt="There aren't any people in the park.", hint="（改寫句子：將 any 改成 some）", answer="There are some people in the park."),
  ]),
  dict(type="guided", title="六、看圖詳答問題", meta="每題3分，共9分", items=[
    dict(prompt="Are there four elephants in the zoo?", hint="（看圖回答）", image=I+"zoo.png", answer="No, there aren't. There are two elephants in the zoo. / There aren't four elephants in the zoo."),
    dict(prompt="What animal is there next to the lion?", hint="（看圖回答）", image=I+"zoo.png", answer="There is a tiger next to the lion."),
    dict(prompt="Are there any monkeys in the zoo?", hint="（看圖回答）", image=I+"zoo.png", answer="Yes, there are two monkeys in the zoo."),
  ]),
  dict(type="translation", title="七、整句式翻譯", meta="每題3分，共9分", items=[
    dict(zh="沒有任何蟲在我的狗的背上。", answer="There aren't any bugs on my dog's back."),
    dict(zh="幸虧有那些醫生，我媽媽現在非常健康。", answer="Thanks to the doctors, my mom is now very healthy. / Thanks to the doctors, my mom is very healthy now."),
    dict(zh="Jeff 正在清理桌子。你可以幫忙他嗎？", answer="Jeff is cleaning (up) the table. Can you help him?"),
  ]),
  dict(type="mc", title="一、單題", meta="【B部分 活用題】每題2分，共8分", items=[
    dict(q="Look at the picture. They are ___.", image=I+"b1.png", options=["looking at a rat","cooking some food","playing with a monkey","cleaning up the kitchen"], correct=3),
    dict(q="A: Are there any houses near the farm? B: Yes, there are ___.", options=["any","some","these","those"], correct=1),
    dict(q="A: We can't talk ___. It's not right. B: You're right. I'm sorry.", options=["for people's help","in people's back","with people's help","behind people's back"], correct=3),
    dict(q="A: Alan Fred's music is so good. B: Yes! ___", options=["He is full and healthy.","His music can't really help.","His music is not so popular.","He's the king of popular music."], correct=3),
  ]),
  dict(type="reading", title="二、依短文或圖表選出適當的答案", meta="每題3分，共15分", passages=[
    dict(label="【A】", text="(John is talking to the girl next door, Betty.)\nJohn: There is a rat in my kitchen. Can you help me, please?\nBetty: Sure. <u>I've got your back</u>. Is there a rat trap in your house?\nJohn: No, there isn't.\nBetty: You can use my rat trap. Put some cheese on <u>it</u>, and you can catch the rat.\nJohn: But there isn't any cheese in my house.\nBetty: Hmm, you can use bananas, too.\nJohn: There aren't any bananas in my house.\nBetty: Is there any food in your house?\nJohn: No. There isn't any.\nBetty: What? Then what is the rat doing in your house?\n\n【字詞】trap 陷阱　put 放置　cheese 起司　catch 捕捉　then 那麼", items=[
      dict(q="<u>It</u> refers to（指涉）___.", options=["the rat","the trap","the food","the house"], correct=1),
      dict(q="\"<u>I've got your back</u>\" means（意指）___.", options=["I can help you","I am behind you","I can clean it up","I can see your back"], correct=0),
      dict(q="Which（哪一個）is NOT true（真實的）?", options=["There is an animal at John's place.","With a trap, people can catch a rat.","There isn't any food in John's house.","Thanks to Betty, the kitchen is clean."], correct=3),
    ]),
    dict(label="【B】Sour Grapes", text="One afternoon, a fox is walking around on a farm and thinking, \"Is there any food around here?\" Luckily, there are many grapes on the farm. The fox is looking at the grapes, and he is really hungry. He is jumping again and again, but he is not tall enough. Now, the fox is sitting under the grapes and looking up at the grapes. He is thinking, \"What am I doing? Maybe those grapes are really sour, or maybe there are bugs in the grapes.\"\n    Are the grapes really sour, or are there bugs in them? There is only one thing for sure: The fox is talking bad about the grapes because he cannot have them.\n\n【字詞】sour 酸的　grape 葡萄　again 再次　thing 事情　because 因為", items=[
      dict(q="What can we learn（得知）from the reading（文章）?", options=["The grapes are very sour.","There is some food near the fox.","Grapes are the fox's favorite food.","Thanks to the grapes, the fox is full."], correct=1),
      dict(q="Which is an example of \"sour grapes\"?", image=I+"sg.png", options=["A","B","C","D"], correct=2),
    ]),
  ]),
]
