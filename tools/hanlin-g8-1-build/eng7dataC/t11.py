# 翰林一上英語 B 卷第 1 回（PDF 第 1、2 頁）
def M(q, o, c): return dict(q=q, options=o.split("|"), correct="ABCDEFG".index(c))
def V(q, a, **k): return dict(q=q, answer=a, **k)
def P(name, page, x0, y0, x1, y1): k = 110 / 72; return (name, page, (x0*k, y0*k, x1*k, y1*k))  # pt 座標
def GM(zh, *lines, **k): return dict(zh=zh, lines=list(lines), **k)
def G(p, h, a): return dict(prompt=p, hint=h, answer=a)
def T(zh, a): return dict(zh=zh, answer=a)


META = dict(n=11, h1="第11回・Unit 6", subtitle="There Are Some Elephants Over There")
I = "images/test11/"
CROPS = [P("look", 22, 58, 50, 333, 130), P("zoo", 22, 407, 547, 721, 700)]
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="每題2分，共20分", items=[
    V("I'm really f___l; I can't eat the turkey leg.", "full"),
    V("Jason is a great teacher. Thanks to his h___p, my son's English is good now.", "help"),
    V("Look over there! A m___y is eating a banana. Now it's climbing（爬）the tree.", "monkey"),
    V("Z___as are black and white. They're beautiful animals.", "Zebras"),
    V("A: What can we do on the farm? B: We can ride a h___se.", "horse"),
    V("A: Is Grace your cousin? B: That's r___t. She is my cousin.", "right"),
    V("The kitchen is dirty（髒的）. Let's c___n up the kitchen together.", "clean"),
    V("A: How is your grandma? Is she okay? B: Yes. She's h___thy and happy now.", "healthy"),
    V("A: Can I eat the f___d on the table? B: No. That's your brother's dinner.", "food"),
    V("The lion is the king of the animal w___d. Many animals are scared（害怕）of lions.", "world"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="每題2分，共24分", items=[
    M("There ___ two books and a pencil case on the desk.", "is|be|are|am", "C"),
    M("A: Are there ___ cows on the farm? B: Yes, there are.", "any|one|the|a", "A"),
    M("There ___ any men at the party.", "isn't|aren't|is|are", "B"),
    M("A: ___ any English classes this week? B: Yes, there are three.", "Are these|Are those|Are they|Are there", "D"),
    M("A: ___ behind the door? B: There is a dog behind the door.", "Where's|How's|When's|What's", "D"),
    M("There are ___ over there.", "a cat|the cat|many cats|any cats", "C"),
    M("A: ___ there any students from Africa? B: Yes. There ___ one from Africa.", "Are; is|Is; is|Is; are|Are; are", "A"),
    M("A: ___ a park near your house? B: No, there isn't.", "Is there|Is it|Are they|Are there", "A"),
    M("Shh! Don't shout（大叫）! Thanks ___ you, everyone is watching us.", "on|for|to|in", "C"),
    M("A: Look! ___ is a black bug on the wall. B: Oh my! The bug is so big!", "Where|This|What|There", "D"),
    M("A: Is there a pencil in the box? B: Yes, ___.", "it's|it is|there's|there is", "D"),
    M("These birds can clean up the bugs for the zebras. They are a big help ___ the zebras.", "in|to|for|at", "B"),
  ]),
  dict(type="mc", title="三、對話選擇", meta="每題2分，共8分", items=[
    M("A: ___ There are many pigs, and they're eating. B: Wow. They are so cute.", "Is there a pig?|It's a small pink pig.|Look over there!|What's that over there?", "C"),
    M("A: ___ B: Yes. There are two.", "What's in your bag?|Is the comic book in your bag?|Aren't there three comic books in your bag?|Are there any comic books in your bag?", "D"),
    M("A: There's a beautiful park behind the museum. B: ___ Let's take a walk at the park after dinner.", "No, there isn't.|Good to know.|So beautiful, right?|Here is one example.", "B"),
    M("A: Elephants can't jump. B: ___ But they can run, right? A: Well, I'm not sure.", "Not really! They can jump.|Oh, that's new to me.|No, there aren't any elephants.|What's on the elephant's back?", "B"),
  ]),
  dict(type="guided", title="四、看圖回答問題", meta="每題3分，共9分", image=I+"look.png", items=[
    G("1. Is there a pig near the horse?", "（簡答）", "Yes, there is."),
    G("2. Are there any rabbits under the tree?", "（詳答）", "No, there aren't any rabbits under the tree. / No, there aren't. There aren't any rabbits under the tree."),
    G("3. Are there any monkeys in the picture?", "（先簡答，再詳答）", "Yes, there are. There are three monkeys in the tree. / Yes, there are. There are three monkeys in the picture."),
  ]),
  dict(type="guided", title="五、依提示作答", meta="每題3分，共6分", items=[
    G("No, there isn't. There isn't an elephant near the car.", "（造原問句）", "Is there an elephant near the car?"),
    G("There are some bugs. The bugs are on the horse's back.", "（合併兩句）", "There are some bugs on the horse's back."),
  ]),
  dict(type="translation", title="六、翻譯", meta="每題3分，共9分（A、B 兩句寫在同一格，例：A: … B: …）", items=[
    T("幸虧有我的貓咪，我家沒有任何老鼠。", "Thanks to my cat, there aren't any rats in my house. / Thanks to my cats, there aren't any rats in my house. / Thanks to my cat, there aren't any mice in my house."),
    T("A：樹下有三隻棕熊嗎？B：不。有兩隻。", "A: Are there three brown bears under the tree? B: No. There are two."),
    T("A：動物園裡有任何狐狸嗎？B：是的，有一些。", "A: Are there any foxes in the zoo? B: Yes, there are some."),
  ]),
  dict(type="cloze", title="七、看圖完成克漏字選擇", meta="每題3分，共18分", image=I+"zoo.png",
    passage="Look at this picture. It is a picture of a ___1___. There are ___2___ people and animals there. There are ___3___ monkeys in the picture. Two are playing with people. There are also two ___4___ and three koalas. Look. A small koala is on its mother's ___5___. It is so cute! What are those three big animals? They are ___6___.\n\n【字詞】koala 無尾熊",
    items=[
      dict(options=["zoo", "farm", "king", "museum"], correct=0),
      dict(options=["any", "many", "no", "not any"], correct=1),
      dict(options=["three", "four", "five", "six"], correct=3),
      dict(options=["lions", "tigers", "bears", "zebras"], correct=0),
      dict(options=["fox", "food", "bug", "back"], correct=3),
      dict(options=["bears", "lions", "elephants", "monkeys"], correct=2),
  ]),
  dict(type="reading", title="八、閱讀測驗", meta="每題3分，共6分", passages=[
    dict(label="", text="(Amy and Ivan are at the zoo now.)\nAmy: Look! There are some monkeys under the tree.\nIvan: Wow! They are so cute.\nAmy: One, two, three, four, five. There are five monkeys.\nIvan: Five? No. There are six.\nAmy: Where is the sixth one? I can't see six monkeys.\nIvan: There's a small monkey on that big monkey's back. Maybe they are a mother and her baby.\nAmy: Ah, you're right. There are six. Hey, there's a black and white horse behind the big tree.\nIvan: Ha ha! That's not a horse. That's a zebra.\nAmy: Oops!\n【字詞】sixth 第六個　how many 多少　which 哪一個　true 真實的", items=[
      M("How many monkeys are there under the tree?", "Three.|Four.|Five.|Six.", "D"),
      M("Which is NOT true?", "There is a zebra behind the big tree.|There is a monkey on the zebra's back.|There are no horses behind the big tree.|Amy and Ivan are looking at monkeys and a zebra.", "B"),
    ]),
  ]),
]
