META = dict(n=13, h1="第13回・Review Test 4", subtitle="Unit 1～Unit 6 全冊總複習")
SECTIONS = [
  dict(type="mc", title="一、單題：請依文意選出一個正確或最佳的答案", meta="36分，每題3分", items=[
    dict(q="Look at the picture. How is the weather?", image="images/test13/q1.png", options=["It's sunny and hot.","It's sunny but cool.","It's cloudy and cold.","It's cloudy and warm."], correct=0),
    dict(q="Watching soccer games ___ fun for Megan.", options=["is","has","are","have"], correct=0),
    dict(q="Tony was doing the dishes when I ___ into the kitchen.", options=["walk","walked","walking","was walking"], correct=1),
    dict(q="A: This camera costs NT$99,000. B: That's very ___ for a camera.", options=["ugly","funny","heavy","expensive"], correct=3),
    dict(q="It ___ a day to go to Red Island ___ ship.", options=["takes; on","takes; by","spends; on","spends; by"], correct=1),
    dict(q="Sandra's hair is long and thick. She needs to ___ half an hour ___ her hair after she washes it.", options=["take; drying","take; to hang","spend; drying","spend; to hang"], correct=2),
    dict(q="A: I'm really poor at ___. B: Don't worry. I can teach you.", options=["cook","cooks","to cook","cooking"], correct=3),
    dict(q="A: Are you ready to ___, sir? B: Yes. I'd like to have the turkey salad, please.", options=["catch","wipe","order","start"], correct=2),
    dict(q="A: When did you ___ the baby? B: Two hours ago. Is she hungry again?", options=["move","feed","interview","remember"], correct=1),
    dict(q="A: What are you ___? B: My toy robot. I can't find it.", options=["taking off","putting on","cutting out","looking for"], correct=3),
    dict(q="A: Did you hear that ___? Where is it coming from? B: It's from the TV.", options=["idea","hope","sound","subject"], correct=2),
    dict(q="A: I paid NT$5,000 for these shoes. B: How could you ___ that much on a pair of shoes?", options=["get","cost","take","spend"], correct=3),
  ]),
  dict(type="cloze", title="二、題組：請依所附的短文或圖表，選出一個最適當的答案（13－17）", meta="20分，每題4分", start=13,
    passage="Aura: The weather is nice today. Let's ___13___ in the mountains. We can see beautiful flowers along the way.\nJose: Maybe next time. ___14___ the sofa today.\nAura: Are you going to watch TV all day again?\nJose: Yes! ___15___\nAura: Come on, Jose! Sitting for long hours is really bad for your ___16___. It may cause an early death.\nJose: That's terrible. Then I'll do some exercise later this weekend.\nAura: Well, it's not enough.\nJose: What else can I do then?\nAura: Stop ___17___ and stand up every twenty minutes.\nJose: Okay. Then I'm going to stand in front of the TV the whole day.\nAura: Oh, Jose!\n\n【字詞】cause 造成　death 死亡　whole 整個的",
    items=[
      dict(options=["go hiking","go sailing","go surfing","go swimming"], correct=0),
      dict(options=["I won't leave","I'm leaving","I was sitting on","I'm not going to sit on"], correct=0),
      dict(options=["It's not fun at all.","That's my dream job.","I just turned off the TV.","That's my plan for today."], correct=3),
      dict(options=["health","choice","moment","experience"], correct=0),
      dict(options=["being so kind","sitting for too long","worrying too much","exercising every day"], correct=1),
  ]),
  dict(type="reading", title="二、題組（18－28）", meta="44分，每題4分", passages=[
    dict(start=18, label="（18－19）", text="Ruth just came back from a trip, and now she is listening to the voice messages on her phone.\n\nMessage 1: Hi, Ruth. It's me, Joan. Sorry to call you on the weekend, but you forgot to call Mr. Brown. Mrs. Hall needs him to come to the office next Thursday. So, please give him a call when you can. You know Mrs. Hall. She will be so mad if you don't do your job. Anyway, have a nice weekend!\n\nMessage 2: Hey, Ruth. This is Dylan. Mom's birthday is next Saturday. Let's take her out for a nice dinner. What do you think about Le Ventre? Mom loves the chicken soup there. Call me back.\n\nMessage 3: Good evening, Mrs. Barr. This is Elaine from Mako Bookstore. You ordered a book from us two weeks ago, and it's still in our store. Please stop by our store. We're open 24 hours a day. Thank you!\n\n【字詞】voice message 語音訊息　forget 忘記（過去式為forgot）　if 如果",
      items=[
        dict(q="Ruth will call Dylan and ___ after she listens to the voice message.", options=["Joan","Mrs. Hall","Mr. Brown","Elaine from the bookstore"], correct=2),
        dict(q="Ruth is on the phone with Dylan. What might she say to Dylan?", options=["\"Happy birthday! It's that time of the year again.\"","\"I'm so sorry. I forgot about that. I will stop by soon.\"","\"I just called Le Ventre. They are full on Saturday. Any other ideas?\"","\"Our office is right next to the metro station. Is 3 p.m. this Thursday okay with you?\""], correct=2),
      ]),
    dict(start=20, label="（20－22）", text="    Venice is a unique city. There are canals all over, so many locals have their own boats. Also, there are no cars, buses, motorcycles, or bikes because the streets are small and narrow. To travel around the city, you can only walk or take a boat. People often take a <u>waterbus</u>. Waterbuses run on the water, not on the street. They can take you around the canals in Venice and some other islands. Water taxis can do that too, but you will spend more money for sure. Besides waterbuses and water taxis, gondolas are also very popular. Gondolas are long small boats in beautiful colors, and some people visit Venice just for gondola rides.\n    There are many different ways to enjoy Venice, and you are sure to have a great time in this wonderful city.\n\n【字詞】canal 運河　local 當地人　more 更多的　gondola 鳳尾船　narrow 窄的",
      items=[
        dict(q="What is a <u>waterbus</u>?", options=["A car.","A boat.","A scooter.","A bicycle."], correct=1),
        dict(q="People travel around Venice in many different ways. Which way is NOT one of them（其中之一）?", options=["By boat.","On foot.","By gondola.","By motorcycle."], correct=3),
        dict(q="Why do most people take a boat when they travel around Venice?", options=["It is expensive to take a taxi.","People in Venice don't like bikes or cars.","Venice is too big, so people seldom walk.","There are many canals in and around Venice."], correct=3),
      ]),
    dict(start=23, label="（23－25）", text="    It was late at night. Kylie and Chris were lost and tired in Denver City. They spent an hour looking for their hotel but still couldn't find it. When the clock hit twelve, they saw a hotel on the street. The hotel was really old, and it was very dark inside. They decided to give it a try. \"Excuse me, we'd like to have a room,\" Chris stood at the front desk and said. No one was there. Kylie started looking around. Suddenly, she saw two girls in blue. When she tried to say something, they disappeared. Kylie pulled Chris's arm and said, \"I just saw something really strange. Let's not stay at this scary hotel.\" Just when they were about to leave, a man came and said, \"Good evening, I'm Jack. Welcome to Overlook Hotel. Your room is ready.\" The man took Kylie and Chris to their room and left. When Kylie and Chris opened the door, they couldn't believe their eyes. It was not a room. It was the street. \"Get out!\" someone cried out from behind them. They looked back. The hotel was not there. Kylie and Chris stood on the street and looked at each other. What just happened?\n\n【字詞】suddenly 突然　disappear 消失　stay 停留　be about to 正要…",
      items=[
        dict(q="What were Kylie and Chris doing at half past eleven?", options=["Getting off the plane.","Looking for their hotel.","Sleeping in a hotel room.","Talking to the guy at Overlook Hotel."], correct=1),
        dict(q="What do we know about Kylie and Chris?", options=["They sleepwalked sometimes.","They enjoyed their vacation a lot.","They had a great time at Overlook Hotel.","They had a terrible experience in Denver City."], correct=3),
        dict(q="In what order（順序）did these things happen?<br>a. Kylie saw two girls in blue.<br>b. Kylie and Chris thought about leaving Overlook Hotel.<br>c. Kylie and Chris spent an hour looking for a hotel.<br>d. Someone told Kylie and Chris to get out of the hotel.", options=["a.→d.→b.→c.","c.→a.→b.→d.","b.→c.→a.→d.","c.→d.→b.→a."], correct=1),
      ]),
    dict(start=26, label="（26－28）King Triton's Swimming Club", text="    Summer is coming. It's time to visit the pool. Join King Triton's Swimming Club and learn swimming at our safe and clean Bubble Outdoor Pool.*\n\n★ Who is the club for?\nWe have fun and easy swimming lessons for beginners from age 5 to age 12.\n\n★ Who will you be learning from?\nMrs. Miller is a three-time winner of Sandy Beach Swimming Contest. She is also a mother of three kids. She's great with kids.\n\n★ How do you get to Bubble Outdoor Pool?\nBOP is on Ocean Road in Atlanta City. It's on the corner of Ocean Road and Sandy Street, across from a movie theater. It's only a five-minute walk from Crabby Metro Station.\n\nCall Bubble Outdoor Pool at 936-607-2114 to learn more about the club!\n\n* We also have a small indoor pool. You can still have a great time on rainy days.\n\n【字詞】outdoor 室外的　beginner 初學者　indoor 室內的",
      items=[
        dict(q="Who may want to join King Triton's Swimming Club?", options=["Ursula. She won many swimming contests when she was little.","Sebastian. He's very good at water sports like swimming and surfing.","Flora. She will go to elementary school next year, and she can't swim.","Eric. He goes to the high school near the club, and he wants to learn swimming."], correct=2),
        dict(q="Jim will meet his friend at Bubble Outdoor Pool at 3 p.m. He will take the metro to Crabby Metro Station and walk from there to the pool. The metro station near his house is Oak Station, and the metro ride will take 15 minutes. Jim doesn't want to be late, and he doesn't want to wait for his friend for too long, either（也不）. When does he need to get to Oak Station?", options=["At 2:40.","Around 2:45.","At five to three.","Around two o'clock."], correct=0),
        dict(q="Look at the map. Which is Bubble Outdoor Pool?", image="images/test13/q28_map.png", options=["A.","B.","C.","D."], correct=1),
      ]),
  ]),
]
