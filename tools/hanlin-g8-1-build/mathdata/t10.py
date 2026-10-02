META = dict(n=10, h1="第10回・2-2～3-2 複習", subtitle="2-2～3-2 複習", lesson="2-2～3-2", title="複習")
IMG = "images/test10/"
CROPS = [("q2",19,(400,470,560,530)), ("q5",19,(444,1160,562,1242)), ("q8",19,(882,298,1110,400)), ("q9_pw",19,(610,680,1096,844)),
         ("f1",19,(948,1126,1110,1260)), ("c3",20,(970,56,1108,238)), ("b5",20,(882,1322,1110,1402))]
SQ = "根號可打 √ 或 sqrt"
SECTIONS = [
  dict(type="mc", title="一、選擇題", meta="【A部分 學力基礎題】每題3分，共30分", items=[
    dict(q=r"下列何者<u>不是</u>多項式 $(x+5)(x-5)$ 的因式？", options=["$5+x$","$2x-10$","$x^2-10$","$x^2-25$"], correct=2),
    dict(q=r"如右圖，$10-2\sqrt{5}$ 在數線上的位置應在哪兩點之間？", image=IMG+"q2.png", options=["$A$ 點和 $B$ 點","$B$ 點和 $C$ 點","$C$ 點和 $D$ 點","$D$ 點和 $E$ 點"], correct=1),
    dict(q=r"計算 $\sqrt{8}-\sqrt{50}+6\sqrt{5}+3\sqrt{2}-\sqrt{125}$ 之值為何？", options=["0",r"$\sqrt{2}$",r"$\sqrt{5}$",r"$5\sqrt{2}-\sqrt{5}$"], correct=1),
    dict(q=r"若 $a=\sqrt{3}-\sqrt{2}$，則 $-(a+2)(a-2)$ 之值為何？", options=[r"$-9+2\sqrt{6}$", r"$-1+2\sqrt{6}$", r"$1-2\sqrt{6}$", "$-1$"], correct=1),
    dict(q=r"利用十字交乘法作多項式 $A$ 的因式分解，過程如右，則下列關於多項式 $A$ 的敘述，何者正確？", image=IMG+"q5.png", options=[r"$A$ 的二次項係數為 3", r"$A$ 的常數項為 1", r"$x+1$ 是 $A$ 的因式", r"$1-3x$ 是 $A$ 的因式"], correct=3),
    dict(q="下列哪一個式子<u>無法</u>再作係數為整數的因式分解？", options=["$x^2-18$","$x^2-81$","$x^2+5x+6$","$x^2+5x-6$"], correct=0),
    dict(q=r"已知 $x-2$ 是 $3x^2-x+k$ 的因式，則下列何者也是 $3x^2-x+k$ 的因式？", options=["$3x+5$","$3x-5$","$3x+2$","$x-2$"], correct=0),
    dict(q=r"如右圖，有甲、乙、丙三種不同大小的長方形圖卡。用 2 張甲、12 張乙和 16 張丙可以緊密且不重疊的方式拼成一個大長方形。若大長方形的長為 $2x+4$，則寬為下列何者？", image=IMG+"q8.png", options=["$x$","$x+2$","$x+4$","$x+6$"], correct=2),
    dict(pre="※請閱讀下列敘述後，回答 9.～10. 題\n下圖是小花與小美利用數學設計生日密碼的經過。生日密碼設計規則：1. 將生日的日期寫成 abcd（例：1月20日→0120，10月2日→1002）；2. 將 (dx＋c)(bx＋a) 展開。小花：我的密碼是 6x²＋7x＋2；小美：我的是 4x²＋2x。", preImage=IMG+"q9_pw.png",
         q="請問<u>小花</u>的生日為何？", options=["11 月 13 日","11 月 26 日","12 月 16 日","12 月 23 日"], correct=0),
    dict(q="請問<u>小美</u>的生日有幾種可能？", options=["1","2","3","4"], correct=2),
  ]),
  dict(type="fill", title="二、非選擇題－填充", meta="每格4分，共20分", items=[
    dict(q=r"如右圖，有一梯形紙片 $ABCD$，$\overline{AB}=5$ 公分，$\overline{BC}=12$ 公分，$\angle B=\angle C=90^\circ$，將 $D$ 點摺向 $A$ 點時，$\overline{CD}$ 與 $\overline{AC}$ 剛好重疊，則梯形 $ABCD$ 的面積為多少平方公分？", image=IMG+"f1.png", answers=["108"], show="108 平方公分"),
    dict(q=r"計算 $\sqrt{\dfrac{887^2+387^2}{2}-887\times387}=$", answers=["250√2"], show=r"$250\sqrt{2}$", hint=SQ),
    dict(q=r"若 $x=\sqrt{7}+\sqrt{6}$，$y=\sqrt{6}-\sqrt{7}$，則 $2x^2+4xy+2y^2=$", answers=["48"], show="48"),
    dict(q=r"坐標平面上，原點 $O$ 到方程式 $3x-4y=12$ 的圖形的最短距離為", answers=["12/5","2.4","2 2/5"], show=r"$\dfrac{12}{5}$", hint="分數寫成 12/5"),
    dict(q=r"設 $x^2+px+q=(x+a)(x+b)$，若 $p<0$，$q<0$，且 $|a|>|b|$，則點 $(a,b)$ 在坐標平面上的第幾象限？", answers=["二","2","第二","第二象限","二象限"], show="第二象限", hint="填一、二、三或四"),
  ]),
  dict(type="calc", title="三、非選擇題－計算", meta="每題10分，共30分（過程寫在計算紙上，每小題填最後答案）", items=[
    dict(q="比較下列各組數的大小關係：",
         parts=[dict(p=r"$x=-\sqrt{2}-\sqrt{6}$，$y=-\sqrt{3}-\sqrt{5}$，$z=-\sqrt{4}-\sqrt{4}$。", answers=["x>y>z","z<y<x"], show=r"$x>y>z$", hint="由大到小寫，例：a>b>c"),
                dict(p=r"$a=\sqrt{8}-\sqrt{4}$，$b=\sqrt{6}-\sqrt{2}$，$c=\sqrt{7}-\sqrt{3}$。", answers=["b>c>a","a<c<b"], show=r"$b>c>a$")]),
    dict(q="因式分解下列各式：",
         parts=[dict(p=r"$(3x+2)^2-15(3x+2)+56$。", answers=["3(x-2)(3x-5)"], show=r"$3(x-2)(3x-5)$"),
                dict(p=r"$x(x+60)+891$。", answers=["(x+33)(x+27)"], show=r"$(x+33)(x+27)$")]),
    dict(q=r"如右圖，四邊形 $ABCD$ 中，$\angle ABC=\angle ADC=90^\circ$，甲、乙、丙、丁皆為正方形。若甲的面積為 25 平方單位，乙的面積為 169 平方單位，丁的面積為 40 平方單位，請回答下列問題：", image=IMG+"c3.png",
         parts=[dict(p=r"$\overline{BC}=$？", answers=["8"], show="8"),
                dict(p="丙的面積為多少平方單位？", answers=["49"], show="49 平方單位")]),
  ]),
  dict(type="fill", title="非選擇題－填充", meta="【B部分 學力精熟題】每格4分，共20分", items=[
    dict(q=r"若 $a+b=3\sqrt{5}+2\sqrt{3}$，且 $a-b=3\sqrt{5}-2\sqrt{3}$，則 $9a^2-9b^2=$", answers=["297"], show="297"),
    dict(q=r"計算 $\dfrac{1998^3+3\times1998^2+3996}{1998^2+1998}=$", answers=["2000"], show="2000"),
    dict(q=r"計算 $(\sqrt{2^3}-1)(\sqrt{2^3}+1)(\sqrt{2^6}+1)(\sqrt{2^{12}}+1)=$", answers=["4095"], show="4095"),
    dict(q=r"若 $x^2-(a-1)x+4=(x+b)^2$，則 $a+b$ 的值可能為", answers=["-1或3"], show="$-1$ 或 3", hint="兩個答案用「或」隔開"),
    dict(q=r"如右圖，有甲、乙、丙三種不同的正方形或長方形紙片。<u>小恩</u>拿 3 張甲紙片、13 張乙紙片與 $a$ 張丙紙片，他想將這些紙片以緊密且不重疊的方式全部拼成一個長方形，則 $a$ 的可能值有幾個？", image=IMG+"b5.png", answers=["4"], show="4 個"),
  ]),
]
