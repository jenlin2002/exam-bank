# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEF".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=14, h1="第14回・Review Test 4", subtitle="Unit 1～Unit 6 全冊總複習")
I = "images/test14/"
CROPS = [P("cat", 27, 620, 105, 712, 165)]
BX = '<div style="border:1px solid var(--paper-line);border-radius:6px;padding:4px 8px;margin:2px 0;">{}</div>'
SECTIONS = [
  dict(type="mc", title="一、單題", meta="每題2分，共40分", items=[
    M('<img src="' + I + 'cat.png" alt="題目附圖" style="width:100%;max-width:140px;display:block;margin:4px 0;border-radius:8px;">Look at the picture. The cat is sleeping on the ___.', "bed|wall|sofa|table", "C"),
    M("Kelly, my ___, is my uncle's only daughter.", "wife|housewife|aunt|cousin", "D"),
    M("Don't talk in class. It's ___ number one. Please follow it.", "rule|case|turn|report", "A"),
    M("A: How old are your ___? B: My father is forty-six, and my mother is forty-three.", "classmates|parents|babies|people", "B"),
    M("Be ___! There are many bugs over there. Don't step（踩踏）on them.", "quiet|sure|lucky|careful", "D"),
    M("Monica is a popular ___. She is my favorite, and I'm going to her concert next Saturday.", "singer|writer|police officer|office worker", "A"),
    M("A: Are you free this ___? There are baseball games on Saturday and Sunday. B: I can go on Sunday.", "month|year|weekend|day", "C"),
    M("The lion is the ___ of animals. They are big and strong（強壯的）.", "son|bug|king|food", "C"),
    M("A: Beth, ___ at this picture. This is my brother, Jason. B: He's handsome.", "wake up|turn off|take a walk|take a look", "D"),
    M("Look! That is our new teacher, Mr. Hills. He's ___ hands with the principal（校長）.", "taking|shaking|using|studying", "B"),
    M("A: ___ Emma and Bill singing with? B: Their friends.", "Who are|Who is|Where are|Where is", "A"),
    M("Hey, don't ___. Nick is not here. Let's wait for ___!", "go; he|going; him|go; him|going; he", "C"),
    M("A: Where's the ___ mom? B: Their mom is in the kitchen.", "girl's|girls'|girl|girls", "B"),
    M("Look! The monkeys ___ up and down near the tree.", "jump|jumping|are jumping|is jumping", "C"),
    M("A: What's the ___ today? B: It's December ___.", "time; twenty|day; the twentieth|date; twenty|date; twentieth", "D"),
    M("Look at the sign—no food or drink. Let's ___ here.", "eat|can't eat|not eat|not eating", "C"),
    M("A: What are ___? B: They are notebooks, and the blue notebook ___ for you.", "those; is|these; are|there; is|they; are", "A"),
    M("Scott's birthday party is ___ six ___ Sunday night.", "at; in|at; on|between; and|from; to", "B"),
    M("___ house is big and beautiful. There are five bedrooms and four bathrooms.", "Sam and Peggy|Sam and Peggy's|Sam's and Peggy|Sam's and Peggy's", "B"),
    M("A: Are there ___ horses on the farm? B: Yes, ___.", "any; they are|some; they are|any; there are|some; there aren't", "C"),
  ]),
  dict(type="cloze", title="二、題組（21－25）", meta="每題3分", start=21,
    passage="Hi, my name is Leah. Today is ___21___. It is an important day. It is my ___22___ day at Orange Elementary School. I am a new student here. I am happy ___23___ nervous. Luckily, ___24___. They are friends with me. Now we are sitting ___25___ and talking. We are having a good time.",
    items=[
      dict(options=["September", "on Monday", "September second", "the second week"], correct=2),
      dict(options=["one", "the one", "first", "the first"], correct=2),
      dict(options=["or", "with", "before", "but"], correct=3),
      dict(options=["my classmates are nice", "not many people can help me", "I'm not here for friends", "there's only one popular student"], correct=0),
      dict(options=["up and down", "around the table", "above the chairs", "right inside the table"], correct=1),
  ]),
  dict(type="cloze", title="二、題組（26－30）", meta="每題3分", start=26,
    passage="Students, please ___26___ and listen. Here are the rules. ___27___ eat or drink here. You can take pictures ___28___ the museum, but don't touch the pictures on the wall. Look at the signs. ___29___ the rules and be safe. It's ___30___ now. Let's meet in front of the museum at 12.\n\n【字詞】touch 觸摸",
    items=[
      dict(options=["turn off", "be quiet", "clean up", "look at"], correct=1),
      dict(options=["Not", "There's no", "Do not", "Cannot"], correct=2),
      dict(options=["on", "inside", "between", "above"], correct=1),
      dict(options=["Follow", "Report", "Take", "Fight"], correct=0),
      dict(options=["at ten", "10 a.m.", "in the morning", "on the tenth"], correct=1),
  ]),
  dict(type="reading", title="二、題組（31－40）", meta="每題3分", passages=[
    dict(start=31, label="（31－33）", text="Good morning, everyone. Welcome to Happy Cow. There are sixty cows here. There are some turkeys, too. You can feed the cows in the morning from 9 to 10. There are great classes for you in the afternoon. We can cook or make cookies together. And, look at the cute small house over there. There are some rabbits inside. You can feed and play with them in the afternoon from 3 to 4.\n【字詞】feed 餵　make 製作", items=[
      M("What is Happy Cow?", "A concert.|A museum.|A farm.|A party.", "C"),
      M(BX.format("A: Mom, can we feed the cows now? B: OK. Let's go.") + "What time can it be?", "9:30 a.m.|10:30 a.m.|3 p.m.|4 p.m.", "A"),
      M("Lisa and Phil are at Happy Cow. They can ___.", "wash the cows|go to a class in the afternoon|feed the turkeys in the small house|feed the rabbits in the morning", "B"),
    ]),
    dict(start=34, label="（34－36）", text="Party Time!\nJennifer's 3rd Birthday\nSaturday, September 14\nOne o'clock in the afternoon\n10 Apple Road\nPlease reply to Cathy at 2701-6769 before September 1.\n【字詞】road 路　reply 回覆", items=[
      M("When is Jennifer's birthday party?", "On September 1.|On September 3.|On September 10.|On September 14.", "D"),
      M("Jennifer's party is today. How old is Jennifer?", "She's one.|She's three.|She's ten.|She's fourteen.", "B"),
      M("Which is NOT true?（何者為非？）", "Jennifer's birthday party is at 1 a.m.|Cathy's phone number is 2701-6769.|Jennifer's birthday party is on Saturday afternoon.|People can reply to Cathy two weeks before the birthday party.", "A"),
    ]),
    dict(start=37, label="（37－38）", text="Lora's Shop Is for Everyone!\nWelcome to Lora's Shop. There are many beautiful bags in our shop. We are open from 10:30 a.m. to 9:30 p.m., Monday to Saturday. We are on Farm Street. It's next to Happy Zoo and right behind Morning Park. Come here this Wednesday. There are gifts for you.\n【字詞】shop 商店　street 街", items=[
      M("Where is Lora's Shop?", "It's on a farm.|It's near a park.|It is in a zoo.|It's behind a bag shop.", "B"),
      M("Jill is now in Lora's Shop for a gift. Which is true?（何者為真？）", "It's 9:20 in the morning.|It is 11 a.m. on Sunday.|It's 1:30 p.m. on Wednesday.|It's ten on Wednesday night.", "C"),
    ]),
    dict(start=39, label="（39－40）", text="Dear Maggie,\nHow are you? Look at the picture. This is my bedroom at my new school. There are two beds. My bed is next to the wall, and the other bed is my classmate Joe's bed. Our room is not big, but <u>it</u> is enough for Joe and me. There is a school party on New Year's Eve. Please come. We can eat great food and play some games.\nYour friend,\nJonathan\n【字詞】the other 另一個", items=[
      M("What is \"<u>it</u>\"?", "New Year's Eve.|Joe's bed.|The school party.|Jonathan and Joe's room.", "D"),
      M("Which is true?", "Maggie and Joe are classmates.|Jonathan isn't happy with his room.|Jonathan and Joe's bedroom is not big.|Jonathan's school party is on the day after New Year's Day.", "C"),
    ]),
  ]),
]
