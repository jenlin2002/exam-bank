# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEF".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=11, h1="第11回・Unit 6", subtitle="There Are Some Elephants Over There")
I = "images/test11/"
CROPS = [P("zoo", 22, 40, 322, 332, 488)]
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共20分", items=[
    V("E___ts are big gray animals with a long nose（鼻子）.", "Elephants"),
    V("A: Where are the m___ys? B: Look! They are in the tree with bananas in their hands.", "monkeys"),
    V("A: Students, please c___n up the classroom now. It's dirty（髒的）. B: OK, Miss Chen.", "clean"),
    V("A: Mom, look at the black and white animals. What are they? B: Oh, they are z___as.", "zebras"),
    V("A: Are you hungry? Here are some apples. B: No, thank you. I'm f___l now.", "full"),
    V("Many adults（成人）can't swim. I'm an e___e of that. I'm 25 years old, and I can't swim.", "example"),
    V("Look! There's a man on the horse's b___k. He is riding the horse.", "back"),
    V("Taipei 101 is the tallest building（最高的建築）in Taiwan, but it is only the eleventh tallest building in the w___d.", "world"),
    V("Come have dinner with us. There's enough f___d for everyone.", "food"),
    V("A: Is that girl your cousin? B: That's r___t. She's Uncle Roger's only daughter.", "right"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共24分", items=[
    M("___ a rat in the kitchen, Jeremy. Come help!", "He is|They are|There is|There are", "C"),
    M("There are ___ chairs in front of the TV.", "one|some|any|a", "B"),
    M("A: Are there three parks near here? B: No, ___.", "there aren't|they aren't|there isn't|there are three", "A"),
    M("A: ___ a sofa in the living room? B: No, there isn't.", "Is it|Is there|Are they|Aren't there", "B"),
    M("A: Are there any bears behind the house? B: No, there aren't ___.", "one|some|many|any", "D"),
    M("There aren't ___ dogs. There are only two dogs.", "some|many|any|the", "B"),
    M("Is ___ a mouse in the small box? B: Yes, there is.", "there|that|this|it", "A"),
    M("A: Are they lions? B: No. They are tigers. They are ___ India（印度）.", "of|on|from|to", "C"),
    M("A: Are there ___ birds in the tree? B: No, but there is a big bug there.", "a|any|the|one", "B"),
    M("Thank you, Mr. Peterson. You are a big help ___ us.", "for|with|on|to", "D"),
    M("A: ___ any cows on the farm? B: Yes. Look! There is a cow under the tree.", "Are there|Are they|Is it|Is there", "A"),
    M("A: Let's go to Green Park. B: Let's not. It's New Year's Eve. There can ___ a lot of traffic（車流量很大）there.", "×|be|is|are", "B"),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共8分", items=[
    M("A: Are there ten apples on the table? B: ___", "No, they aren't.|Yes, they are apples.|Yes, there are ten.|No, it isn't your apple.", "C"),
    M("A: In an elephant herd, the grandma elephant is the leader（領導者）. B: Really? ___", "Look over there.|There's only one.|The king of animals.|That's new to me.", "D"),
    M("A: Aren't there twelve girls in your class? B: ___", "No, there aren't.|They are over there.|Yes, there is a girl.|No, they aren't in my class.", "A"),
    M("A: ___ B: They are foxes.", "Who are those people?|Where are the foxes?|What are those under the tree?|Are there any foxes over there?", "C"),
  ]),
  dict(type="cloze", title="四、克漏字選擇", meta="每題2分，共12分",
    passage="My favorite ___1___ is the Formosan black bear. It is big and beautiful. ___2___ a big white V on its chest. Bugs, leaves, and fish are the bear's ___3___. Now I am here at the zoo and taking some pictures. Look! There is one baby bear on its mother's ___4___, and there ___5___ two baby bears in the tree. They are playing ___6___ each other. Aren't they cute?\n\n【字詞】Formosan black bear 臺灣黑熊　chest 胸　leaves 樹葉（複數形）",
    items=[
      dict(options=["king", "rat", "tiger", "animal"], correct=3),
      dict(options=["It's", "Here's", "He's", "There's"], correct=3),
      dict(options=["help", "fan", "food", "coat"], correct=2),
      dict(options=["bug", "back", "band", "hand"], correct=1),
      dict(options=["is", "am", "can", "are"], correct=3),
      dict(options=["for", "to", "with", "of"], correct=2),
  ]),
  dict(type="reading", title="五、根據圖片內容，選出正確的答案", meta="每題3分，共9分", passages=[
    dict(label="", text="", image=I+"zoo.png", items=[
      M("What animal is behind the tree?", "A lion.|A monkey.|A zebra.|An elephant.", "D"),
      M("How many zebras are there in the picture?", "One.|Two.|Three.|Four.", "B"),
      M("Who is right?", "Kim: Look! The lion is sleeping.|Bill: There are two lions over there.|Sean: There is only one elephant in the zoo.|May: Come take a look. There are three monkeys in the tree.", "D"),
    ]),
  ]),
  dict(type="reading", title="六、閱讀測驗", meta="每題3分，共9分", passages=[
    dict(label="", text="My name is Donna. I am a cow on Uncle Jon's farm. There are many animals on the farm. There are pigs, cows, turkeys, horses, and a <u>cattle egret</u>. The cattle egret is white. His name is Donald. He is a big help to me. There are bugs on my back. Luckily, Donald is with me. The bugs are food to him. Thanks to his help, I am healthy. Look! He is flying above me. He is my best friend.\n【字詞】fly 飛翔　best 最好的", items=[
      M("What is a <u>cattle egret</u>?", "It's a pig.|It's a bird.|It's a cow.|It's a horse.", "B"),
      M("Which（哪一個）is NOT a farm animal on Uncle Jon's farm?", "The pig.|The cow.|The bug.|The turkey.", "C"),
      M("Which is true（真實的）?", "Cattle egrets eat bugs.|Donna and Donald are not friends.|There aren't any horses on the farm.|With Donna's help, Donald is healthy.", "A"),
    ]),
  ]),
  dict(type="guided", title="七、依提示作答", meta="每題3分，共9分", items=[
    G("There are foxes in the zoo.", "（用 any 改為否定句）", "There aren't any foxes in the zoo. / There are not any foxes in the zoo."),
    G("Are there any monkeys in the tree?", "（先簡答，再用「三隻」詳答）", "Yes, there are. There are three. / Yes, there are. There are three monkeys in the tree."),
    G("There is a bird. / The bird is on the zebra's back.", "（合併兩句）", "There is a bird on the zebra's back. / There's a bird on the zebra's back."),
  ]),
  dict(type="translation", title="八、翻譯", meta="每題3分，共9分（A、B 兩句寫在同一格，例：A: … B: …）", items=[
    T("看！在那裡有許多餅乾。", "Look! There are many cookies over there. / Look! There are a lot of cookies over there."),
    T("幸虧有他們的幫助，那些動物乾淨又健康。", "Thanks to their help, those animals are clean and healthy."),
    T("A：動物園裡面有任何的老虎嗎？B：是的，有一些。", "A: Are there any tigers in the zoo? B: Yes, there are some."),
  ]),
]
