META = dict(n=14, h1="第14回・Review Test 4", subtitle="Review Test 4（Unit 1～Unit 6）", lesson="Review 4", ctitle="Unit 1～Unit 6 總複習")
CROPS = [
  ("q1_pic", 27, (595, 313, 740, 434)),
  ("pie", 27, (790, 1115, 1435, 1410)),
  ("q27_theater", 28, (170, 1692, 655, 1985)),
]
BOX = "background:#fff;border:1px solid var(--paper-line);border-radius:8px;padding:10px 14px;margin-bottom:8px;"
SECTIONS = [
  dict(type="mc", title="一、單題：請依文意選出一個正確或最佳的答案", meta="40分，每題2分", items=[
    dict(q="Look at the picture. The singer is ___ with the fans.", image="images/test14/q1_pic.png", options=["taking a walk","shaking hands","taking pictures","watching a video"], correct=1),
    dict(q="In the Greta Zoo, there are ___ lions, but there are not ___ tigers.", options=["any; any","any; some","some; any","some; some"], correct=2),
    dict(q="A: Who is the tall guy over there? B: That's Camille's ___, Jack. The boy next to him is their son.", options=["uncle","cousin","father","husband"], correct=3),
    dict(q="A: ___ is Melena's basketball game? B: It's on May 4.", options=["What day","What year","What time","What date"], correct=3),
    dict(q="A: What is Ricky doing in the ___? B: He's cooking dinner for us.", options=["kitchen","bedroom","bathroom","living room"], correct=0),
    dict(q="A: Look. Celine is ___ the food on the table. B: Oh no! Bad dog. You can't ___ that.", options=["eat; eat","eating; eat","eat; eating","eating; eating"], correct=1),
    dict(q="Please don't run in the classroom. It's not ___.", options=["safe","enough","clean","important"], correct=0),
    dict(q="A: Are those birthday cards for Cindy? B: Yes, ___ are.", options=["they","these","there","those"], correct=0),
    dict(q="A: Is Brady's favorite ___ black? B: No. It's brown. Everything（一切事物）in his room is brown.", options=["gift","rule","sign","color"], correct=3),
    dict(q="A: Who's Mrs. Lorna? B: She's an English ___ at my school. I'm her student.", options=["teacher","housewife","police officer","office worker"], correct=0),
    dict(q="A: When is the movie? B: It's ___ 5 p.m. ___ today.", options=["at; ×","×; at","on; ×","×; on"], correct=0),
    dict(q="A: What is Ashton doing? B: He is ___ and washing his car.", options=["using","taking","cleaning","following"], correct=2),
    dict(q="A: Let's ___ together after school. B: Sure. You can come to my place.", options=["study","studying","can study","to study"], correct=0),
    dict(q="A: Are there any big ___ in the zoo? B: Yes. There are lions and elephants.", options=["bugs","kings","bands","animals"], correct=3),
    dict(q="A: Please ___ careful with the eggs. B: Yes, Mr. Hyde.", options=["do","be","let's","can"], correct=1),
    dict(q="A: My sister is ten years old. B: My brother is ten years old, ___.", options=["too","also","around","now"], correct=0),
    dict(q="A: Where is your cat? Isn't she in the living room? B: She is, but she's ___ the sofa. You can't see her from here.", options=["above","inside","behind","between"], correct=2),
    dict(q="A: You can have the turkey on the table. B: Thank you, but I am very ___.", options=["full","hungry","healthy","popular"], correct=0),
    dict(q="There is a tree ___ the farm, and there are birds ___ that tree.", options=["in; in","on; in","on; of","in; on"], correct=1),
    dict(q="Please ___ the TV. It's time for bed.", options=["talk to","wait for","turn off","clean up"], correct=2),
  ]),
  dict(type="reading", title="二、題組：請依所附的短文或圖表，選出一個最適當的答案", meta="60分，每題4分", passages=[
    dict(label="（21–23）", start=21, text="Boys and girls can be very different. Their favorite colors can be different, too. ___21___ They are showing the boys' and girls' favorite colors from Town Creek Junior High School. For the girls, the most popular color is purple, but for the boys, the most popular color is blue. And the second most popular color for the girls is blue, but for the boys, it is the color black. From the pictures, you can also see red as some girls' favorite color, but ___22___. For them, red is not a favorite. And the two colors ___23___ are popular with the boys but not the girls.\n\n【字詞】different 不同的　show 顯示　most 最…　as 當作", image="images/test14/pie.png", imageWidth=560,
      items=[
        dict(q="（21）空格應填入：", options=["What is your favorite color?","Take a look at the two pictures.","The two pictures are of the boys and girls.","There are five different colors in the picture."], correct=1),
        dict(q="（22）空格應填入：", options=["red is not in the two pictures","orange is many boys' favorite","it is not a popular color for the boys","it is also very popular with the boys"], correct=2),
        dict(q="（23）空格應填入：", options=["red and green","black and blue","yellow and purple","orange and yellow"], correct=3),
      ]),
    dict(label="（24–26）", start=24, text="Evie: What are you reading on your phone, Jim?\nJim: I am reading about Purple World.\nEvie: What is that?\nJim: It's a park, and there are many trees and some bears. The bears there are very special. The color of their coat is between purple and black, and for baby bears, their coat is purple. The park's name is Purple World thanks to the color of their coat.\nEvie: Wow! Are the bears <u>dangerous</u>?\nJim: No. They are very nice, and they are friends with people.\nEvie: That's great.\nJim: Yes. Sadly, there are not many bears in the park now. Some bad guys are hunting them for their beautiful coat. Now, the police are after those bad people.\nEvie: Good to know <u>that</u>.\n\n【字詞】sadly 令人遺憾地　hunt 獵捕",
      items=[
        dict(q="Which（哪一個）is close to（接近）<u>dangerous</u>?", options=["Lucky.","Not safe.","Nervous.","Important."], correct=1),
        dict(q="What is <u>that</u> in the last line（最後一行）?", options=["People are hunting the bears.","The bears can never eat people.","The police are helping the bears.","The coat of the bears is beautiful."], correct=2),
        dict(q="Which is right about Purple World?", options=["The trees are purple there.","There aren't any baby bears there.","There are too many bears in the park today.","The name of this place is from the color of the bears."], correct=3),
      ]),
    dict(label="（27–29）", start=27, text="There is a big white house in the USA. What is special about it? Well, it is not only a house. It is a home to the president of the USA and the president's family. It is the White House. In the big house, there are 132 rooms, 35 bathrooms, and 412 doors. In those rooms, there are many bedrooms and offices. There is also a game room, a music room, and a big dining room. The big dining room is the State Dining Room. It is big enough for 140 people. Inside the White House, there is a museum and a <u>theater</u>, too. The theater is for the president's family and guests. They can see movies there. The beautiful big white house is not only for the president and the president's family. It is open to everyone. People can have a tour around the White House.\n\n【字詞】president 總統　guest 賓客　tour 參觀",
      items=[
        dict(q="Which is a picture of a <u>theater</u>?", image="images/test14/q27_theater.png", options=["A","B","C","D"], correct=0),
        dict(q="What is the reading mainly（主要的）about?", options=["The rooms in the White House.","The White House tours for people.","The president and the president's family.","The big dining room in the White House."], correct=0),
        dict(q="Which is NOT right about the White House?", options=["There are many bathrooms inside the house.","Some bedrooms there are for the president's family.","The president's guests can see a movie at the theater there.","Only the president and the president's family can go inside the house."], correct=3),
      ]),
    dict(label="（30–31）", start=30, text="I am a number,\nA number with three <i>e</i>'s.\nI am a number,\nA number with three <i>n</i>'s.\nThere aren't any <i>h</i>'s in me,\nYou can see no <i>v</i>'s in me.\nBut yes, there is an <i>i</i>,\nWith an <i>i</i>, there is also a <i>t</i>.\nI am above ten and under twenty,\nWhat number am I?\n\n【字詞】with 有著…",
      items=[
        dict(q="How many <i>v</i>'s are there in the number?", options=["One.","Two.","Three.","There aren't any v's in it."], correct=3),
        dict(q="What number is it?", options=["17.","18.","19.","21."], correct=2),
      ]),
    dict(label="（32–35）", start=32, text="Betty is standing right in front of the door of her house. She cannot open the door. The <u>key</u> to the house is not in her schoolbag. Can it be in the classroom at her school? Now, she can only wait for her parents, but they are not coming home before nine o'clock this evening. It's five o'clock. \"What can I do?\" Betty is looking at the street and thinking. Near the yellow house on the street, there is an old man. He is walking right to Betty. Betty is very nervous. She cannot go inside the house, and that old man is coming up to her. This is not good. <u>Today is really not her day</u>.\n\nBetty: Don't come near me. I'm calling the police.\nOld man: Oh no! I'm not a bad guy. Is this your <u>key</u>?\nBetty: Oh yes! That's my <u>key</u>. I am sorry.\nOld man: It's okay. Here.\nBetty: Thank you.\n\n【字詞】street 街道　call 打電話",
      items=[
        dict(q="Betty's parents are home now. What time can it be?", options=["5:30 p.m.","7:30 p.m.","8:45 p.m.","9:15 p.m."], correct=3),
        dict(q="With a <u>key</u>, people can ______.", options=["open a door","go to school","call the police","fight with each other"], correct=0),
        dict(q="\"<u>Today is really not her day</u>\" means（意指）\"______.\"", options=["today she's a bad girl","today she is not lucky","today is not her birthday","today is important to her"], correct=1),
        dict(q="What can we know from the reading（文章）?", options=["The old man's house is yellow.","At four thirty, the girl is at home.","The old man is not helping Betty.","The old man is giving Betty her key."], correct=3),
      ]),
  ]),
]

