# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEFG".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=14, h1="第14回・Review Test 4", subtitle="Unit 1～Unit 6 全冊總複習")
I = "images/test14/"
CROPS = [P("room", 28, 42, 68, 365, 268)]
BX = '<div style="border:1px solid var(--paper-line);border-radius:6px;padding:4px 8px;margin:2px 0;">{}</div>'
SECTIONS = [
  dict(type="mc", title="一、單題：請依文意選出一個正確或最佳的答案", meta="每題2分，共40分", items=[
    M("Today is Sunday, May 7. It's ___ Sunday of May.", "the first|first|the one|a first", "A"),
    M("A: What's the ___ today? B: It's ___ October 22.", "day; in|day; ×|date; on|date; ×", "D"),
    M("A: What's her uncle's name? B: ___ name is Bob.", "Her|His|Your|Their", "B"),
    M("There aren't ___ pigs on the farm, but there are ___ turkeys there.", "some; two|any; many|some; any|any; any", "B"),
    M("My father's sister is my ___.", "grandma|daughter|aunt|cousin", "C"),
    M("Be ___ with the drink. It's very hot（燙的）.", "special|careful|healthy|important", "B"),
    M("A: ___ is that boy? B: He is Tom's brother.", "Who|What|When|Where", "A"),
    M("A: Is Mrs. White a nurse? B: No, ___.", "she's not|she is|Mrs. White is|Mrs. White isn't", "A"),
    M("A: Is Nick old? B: No, he's not. He's ___ 17. He's ___.", "also; tall|only; tall|so; young|only; young", "D"),
    M("A: What are ___? B: They are markers.", "there|that|this|these", "D"),
    M("Guys, we are in the museum now. Let's ___ talk on the phone or take pictures with it.", "no|not|don't|can't", "B"),
    M("A: ___ is it? B: It's four forty-five.", "How old|What day|What time|What date", "C"),
    M("A: What time is the party? B: It's ___ 6 p.m.", "at|from|on|in", "A"),
    M("Nancy ___ a walk in the park now.", "take|taking|is taking|are taking", "C"),
    M("A: Look! My dog can ___ hands with ___. B: Wow. That's so cute.", "shake; me|clean; I|draw; me|wash; I", "A"),
    M("Thanksgiving is ___ November. It's ___ the fourth Thursday of November.", "in; in|in; on|on; of|on; at", "B"),
    M("A: ___ is your birthday? B: It's on June 14.", "When|What time|Where|What day", "A"),
    M("___ are four notebooks on the table.", "These|Those|They|There", "D"),
    M("A: What are the ___ around the zebras? B: They are lions.", "bugs|people|animals|examples", "C"),
    M("Christmas Eve is the night ___ Christmas.", "before|after|between|on", "A"),
  ]),
  dict(type="cloze", title="二、題組（21－24）", meta="每題2分", start=21,
    passage="(At school)\nTom: Hi, I'm Tom. ___21___\nKelly: I'm Kelly. Nice to meet you, too.\nTom: ___22___ those in that box?\nKelly: They are jump ropes.\nTom: ___23___ By the way, are there any ___24___ in the classroom?\nKelly: No, there aren't. But there are baseballs. They are on the desk over there.\n\n【字詞】by the way 順道一提",
    items=[
      dict(options=["Where are you?", "How are you?", "Good morning.", "Nice to meet you."], correct=3),
      dict(options=["What are", "What is", "Where are", "Where is"], correct=0),
      dict(options=["Oh my!", "I see.", "Not really.", "They really are."], correct=1),
      dict(options=["baseballs", "basketballs", "baseball", "basketball"], correct=1),
  ]),
  dict(type="reading", title="二、題組（25－37）", meta="每題4分", passages=[
    dict(start=25, label="（25－27）", text="This is a picture of Ron's bedroom. The two mice, Wendy and Molly, and the cat, Benjamin, are his pets（寵物）.\n【字詞】which 哪一個　true 真實的", image=I+"room.png", items=[
      M("What can we see in the room?", "Many brushes.|Some books.|Some markers.|A pencil case.", "B"),
      M("Which is NOT true?", "There's a TV on the desk.|There's a basketball on the bed.|There are pictures in front of the sofa.|There are two apples between the mice.", "C"),
      M(BX.format("A: Dear, where's Benjamin? Is he in your room? B: ______") + "Which is the best answer for B?", "Yes, he's eating the apples.|Yes, he's sleeping on the sofa.|Yes, he's sitting under the table.|Yes, he's playing with Ron and Molly.", "C"),
    ]),
    dict(start=28, label="（28－31）", text="Name: Andy　Birthday: 5/1　15 years old\nName: Jessie　Birthday: 2/20　42 years old\nName: Mason　Birthday: 7/20　53 years old\nName: Kathy　Birthday: 12/31　35 years old", items=[
      M(BX.format("A: What day is it today? B: Tuesday.<br>A: Jessie's birthday is next Monday. Let's go to her house that day. B: Okay, I'm free.") + "What's the date today?", "January 14.|January 15.|February 14.|February 15.", "C"),
      M("How old is Mason?", "Thirty-five.|Forty-three.|Fifty-three.|Fifty-six.", "C"),
      M("Which is NOT true?", "Mason's birthday is in July.|Kathy's birthday is in November.|Jessie is forty-two years old.|Andy's birthday is on the first day of May.", "B"),
      M(BX.format("A: Can you go to the birthday party with me? It's on New Year's Eve.<br>B: Okay. I'm free on that day.") + "The two people are talking about ___ birthday party.", "Andy's|Jessie's|Mason's|Kathy's", "D"),
    ]),
    dict(start=32, label="（32－37）", text="Below is Mark's after-school schedule for the week.\n【May 2 Sun.】17:00–18:00 Play basketball at school；19:00–21:00 Go to a magic show\n【May 3 Mon.】17:00–18:00 Dance class；19:00–20:00 Study at home；20:00–21:00 Watch a basketball game at home\n【May 4 Tues.】19:00–20:00 Study at home；20:00–21:00 Play games at home\n【May 5 Wed.】17:00–18:00 Take a walk；19:00–21:00 Yumi's concert\n【May 6 Thurs.】17:00–18:00 Go to the park；19:00–20:00 Study at home；20:00–21:00 Watch a basketball game at home\n【May 7 Fri.】18:00–19:00 Dance class；19:00–20:00 Study at home；20:00–21:00 Play video games at home\n【May 8 Sat.】17:00–18:00 Play baseball at the park；19:00–21:00 Lily's birthday party\n【字詞】below 下方　schedule 行程　show 表演　reply 回答", items=[
      M("What day is May 6?", "Monday.|Tuesday.|Thursday.|Friday.", "C"),
      M("When is the magic show?", "Sunday evening.|Saturday evening.|Sunday morning.|Saturday morning.", "A"),
      M("Today is Friday, and it's eight thirty at night. Where's Mark?", "He's at home.|He's at school.|He's at a party.|He's at the park.", "A"),
      M(BX.format("James: Mark, are you free on Wednesday? Let's go see Jeffery's new movie together that day. The movie is from 6:15 to 8:15 p.m.<br>Mark: ______") + "What can be Mark's reply?", "Sorry, I'm not free.|Sure. Let's go together.|I can't go. Lily's birthday party is at 7 p.m.|Sorry. There's a basketball game that night.", "A"),
      M("What time is the dance class on May 3?", "At 5 p.m.|At 6 p.m.|At 7 p.m.|At 8 p.m.", "A"),
      M("Which is NOT true?", "There aren't any parties on May 4.|It's 5 p.m. on May 7. Mark is free now.|There is only one dance class this week.|It's 7:30 p.m. on May 3. Mark is studying at home.", "C"),
    ]),
  ]),
]
