META = dict(n=4, h1="第4回・Review Test 1", subtitle="Starter Unit～Unit 2 總複習")
I = "images/test4/"
CROPS = [("tree",8,(180,82,410,282)), ("pics",8,(660,480,1012,748)), ("charts",8,(660,1300,1052,1548))]
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="【A部分 基礎題】每格1分，共8分", items=[
    dict(q="A: Who's that? B: That's my u___e. He's my dad's brother.", answer="uncle"),
    dict(q="A: Are they pencils? B: No. They are b___hes.", answer="brushes"),
    dict(q="A: I'm hungry. B: Here are some（一些）c___ies for you. A: Thanks.", answer="cookies"),
    dict(q="A: What color is your cat? B: It's b___n.", answer="brown"),
    dict(q="A: Who's that beautiful w___n? B: That's Kevin's wife.", answer="woman"),
    dict(q="A: Who's your f___e singer? B: Leo Rex. His songs are nice.", answer="favorite"),
    dict(q="A: My grandpa is fifty-two years old. B: Really? He's y___g.", answer="young"),
    dict(q="A: Is Mrs. Molly a junior high school teacher? B: No. She's an e___y school teacher.", answer="elementary"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共28分", items=[
    dict(q="Look! That red car is Mr. Samberg's ___ car.", options=["new","a new","his new","the new"], correct=0),
    dict(q="My aunt is not ___ singer. She is ___ office worker.", options=["a; a","a; an","a; the","the; an"], correct=1),
    dict(q="A: ___ is your sister? B: She's in my room.", options=["How","Who","How old","Where"], correct=3),
    dict(q="A: ___ your husband a teacher, too? B: Yes.", options=["Is","Be","Am","Are"], correct=0),
    dict(q="A: What are ___ in your bag? B: They are oranges.", options=["it","this","that","those"], correct=3),
    dict(q="Dad's watch is ___ the table.", options=["of","on","next","between"], correct=1),
    dict(q="A: Are those Veronica's markers? B: Yes, ___.", options=["they are","these are","those are","they are markers"], correct=0),
    dict(q="A: Where ___ the pictures? B: On the wall.", options=["is","be","are","am"], correct=2),
    dict(q="My friend is between ___.", options=["a tree","that car","the chair","those two women"], correct=3),
    dict(q="A: Who's that in the picture? Is ___ your classmate? B: No. That's my cousin.", options=["she","you","his","these"], correct=0),
    dict(q="This house is big enough for a family ___ four.", options=["at","of","in","on"], correct=1),
    dict(q="A: Is your dog in front of the house? B: No. He is ___ the house.", options=["above","for","inside","between"], correct=2),
    dict(q="A: How old is your baby brother? B: He's ___.", options=["two","two-year","two years","two-year-old"], correct=0),
    dict(q="The park is ___ the zoo ___ the school.", options=["next; to","of; under","above; at","between; and"], correct=3),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共8分", items=[
    dict(q="A: The bathroom is next to my room. B: ___", options=["I see.","It's enough.","You are special.","Maybe it's behind you."], correct=0),
    dict(q="A: ___ B: They are fine.", options=["What are their names?","How old are your dogs?","How are Lisa and Jasper?","Where are the girls' rooms?"], correct=2),
    dict(q="A: Isn't Greg's dad a singer? B: ___", options=["Yes, he is a writer.","No. He is a doctor.","Oh no! That boy isn't Greg.","That's Greg's dad, Mr. Smith."], correct=1),
    dict(q="A: ___ B: They are inside the classroom.", options=["Who are those people?","How are Sam's parents?","Aren't they Jean and Johnson?","Where are Amy and her friend?"], correct=3),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="每題2分，共8分",
    passage="Look at the gap under the sofa. ___1___ is that girl? That's the girl from the gap. She is very thin. She could be in any gaps ___2___. She could be in the gap under the living room table; she could be in the gap behind the kitchen door. She could look at you from the gap ___3___ your chair and your desk, too. Now, look under the bed in your bedroom. ___4___ she's right there.\n\n【字詞】gap 縫隙　could 可能　any 任何的　now 現在",
    items=[
      dict(options=["How","Who","Where","How old"], correct=1),
      dict(options=["in your house","behind the park","in front of the car","inside the classroom"], correct=0),
      dict(options=["on","with","inside","between"], correct=3),
      dict(options=["But","Maybe","Really","Enough"], correct=1),
  ]),
  dict(type="guided", title="五、看圖回答問題", meta="每題2分，共4分", items=[
    dict(prompt="Is Eric's mother a nurse?", hint="（看圖，先簡答，再詳答）", image=I+"tree.png", answer="No, she isn't. She is a police officer."),
    dict(prompt="The girl's brother is eleven years old, and her sister is five. What's the girl's name?", hint="（看圖回答）", image=I+"tree.png", answer="Her name is Sandy."),
  ]),
  dict(type="guided", title="六、依提示作答", meta="每題2分，共6分", items=[
    dict(prompt="Sally's notebook is <u>under the desk</u>.", hint="（依畫線部分造原問句）", answer="Where is Sally's notebook?"),
    dict(prompt="What <u>is that</u> near the wall?", hint="（將畫線部分改為複數）", answer="What are those near the wall?"),
    dict(prompt="No, the mouse is not between the chairs.", hint="（造原問句）", answer="Is the mouse between the chairs?"),
  ]),
  dict(type="translation", title="七、整句式翻譯", meta="每題3分，共6分", items=[
    dict(zh="Katie 在飯廳裡嗎？", answer="Is Katie in the dining room?"),
    dict(zh="這些禮物盒是紫色的。", answer="These gift boxes are purple."),
  ]),
  dict(type="mc", title="一、單題", meta="【B部分 活用題】每題2分，共8分", items=[
    dict(q="Regan's ___ daughter is a housewife.", options=["25-year","25-year-old","25 years","25 years old"], correct=1),
    dict(q="A: ___ B: They are high school teachers.", options=["Who is it?","How is it?","What are they?","Where are they?"], correct=2),
    dict(q="A: Who's that handsome boy? B: ___", options=["Owen's son is tall.","That boy is nineteen.","The boy is at the door.","He's the son of Mr. Owen."], correct=3),
    dict(q="A: ___ B: That's for my baby sister.", options=["Who is the banana for?","Where is your baby sister?","What are those on the table?","How old is your baby sister?"], correct=0),
  ]),
  dict(type="reading", title="二、依短文或圖表選出適當的答案", meta="每題4分，共24分", passages=[
    dict(label="【A】", text="Gordon: Look at this picture.\nJosephine: Wow. Who's that beautiful tall girl in front of you?\nGordon: That's my uncle's daughter. Her name is Laurie.\nJosephine: Is she our age?\nGordon: Yes. She's thirteen, too.\nJosephine: She's very tall for her age. And the person next to her?\nGordon: Oh, that's my big brother, Levitt. He's seventeen years old.\nJosephine: He's handsome. This is a nice picture.\nGordon: Thank you.\n\n【字詞】age 年齡", items=[
      dict(q="Laurie is Levitt's ___.", options=["aunt","cousin","sister","classmate"], correct=1),
      dict(q="How old is Josephine?", options=["Thirteen.","Fourteen.","Sixteen.","Seventeen."], correct=0),
      dict(q="Which（哪一個）is Gordon's picture?", image=I+"pics.png", options=["A","B","C","D"], correct=3),
    ]),
    dict(label="【B】", text="What is your dream job? For 98 students at St. James Junior High School, the top three dream jobs are doctors, writers, and singers. At this school, being a doctor is 14 students' dream job, and being a writer is 28 students' dream job. The top dream job for the students at St. James Junior High School is to be a singer. For the other nine students, their dream jobs are teachers, nurses, and cooks.\n\n【字詞】dream job 理想工作　top 排名最前面的　being / to be 成為；當　other 其他（的）", items=[
      dict(q="___ students' dream job is to be a singer.", options=["Twenty-eight","Forty-seven","Fifty-six","Ninety-eight"], correct=1),
      dict(q="Which is NOT true（真實的）about（關於）the students at St. James Junior High School?", options=["Nine students' dream job is to be a teacher.","Fourteen students' dream job is to be a doctor.","The top two dream jobs are writers and singers.","Twenty-eight students' dream job is to be a writer."], correct=0),
      dict(q="Which picture is for the reading（文章）?", image=I+"charts.png", options=["A","B","C","D"], correct=1),
    ]),
  ]),
]
