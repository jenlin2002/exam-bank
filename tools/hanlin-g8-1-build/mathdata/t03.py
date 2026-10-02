META = dict(n=3, h1="第3回・1-3 多項式的乘除", subtitle="1-3 多項式的乘除", lesson="1-3", title="多項式的乘除")
IMG = "images/test3/"
CROPS = [("q8",5,(968,150,1102,272)), ("q9_frame",5,(910,496,1094,642)), ("f3",5,(938,1263,1107,1420)), ("c1",6,(390,203,560,327)), ("c2",6,(393,738,560,852))]
SECTIONS = [
  dict(type="mc", title="一、選擇題", meta="【A部分 學力基礎題】每題3分，共30分", items=[
    dict(q=r"若 $(x+10)(x-3)=x^2+ax+b$，則 $a-b$ 之值為何？", options=["$-37$","$-23$","23","37"], correct=3),
    dict(q=r"若 $6x^2+3x+2$ 除以 $3x$ 的商式為 $A$，餘式為 $B$，則 $A+B=$？", options=["$2x+1$","$2x+2$","$2x+3$","$2x+4$"], correct=2),
    dict(q="下列選項何者正確？", options=[r"$2x^2\div(-x)=2x$", r"$4x^2\div(-2x)^2=-2$", r"$(-25x^2)\div5x=-5x$", r"$(4x^2+6x)\div(-2x)=-2x+3$"], correct=2),
    dict(q=r"求 $[(2x^2+x-3)-(-x^2-3x+4)]\div(x-1)$ 的商式為何？", options=["$3x-7$","$3x+7$","$x-1$","$x+1$"], correct=1),
    dict(q=r"若 $A$ 為 $x$ 的二次多項式，$B$ 為 $x$ 的一次多項式，$C$ 為 $x$ 的一次多項式，則 $(A-B)\div C$ 的商式為 $x$ 的幾次多項式？", options=["四","三","二","一"], correct=3),
    dict(q=r"若 $[(2x+3)-(5x-2)]^2=ax^3+bx^2+cx+d$，則 $a+b+c+d$ 之值為何？", options=["64","4","$-4$","$-64$"], correct=1),
    dict(q=r"$A$、$B$ 為兩多項式，且 $4A=-4x^2+3x-8$，$3B=8x^2-5x-4$，則 $A\times B$ 的常數項為何？", options=["$-1$",r"$-\dfrac{3}{8}$",r"$\dfrac{8}{3}$","32"], correct=2),
    dict(q=r"右圖是<u>小霍</u>利用直式除法求出 $(x^2-6x)\div(x-3)$ 的商式與餘式的過程與結果，判斷下列哪一個式子是<u>錯誤</u>的？", image=IMG+"q8.png",
         options=[r"$(x^2-6x)\div(x-3)=(x-3)-9$", r"$x^2-6x=(x-3)(x-3)-9$", r"$x^2-6x=(x-3)^2-9$", r"$(x^2-6x+9)\div(x-3)=x-3$"], correct=0),
    dict(pre="※請閱讀下列敘述後，回答 9.～10. 題\n某工廠製作的畫框如右圖所示，此畫框為長方形，其長為 (2x＋5) 公分，寬為 (x＋7) 公分，邊框的寬度均為 2 公分。", preImage=IMG+"q9_frame.png",
         q="若不計厚度，則此畫框的邊框面積為多少平方公分？", options=["$12x+32$","$12x+48$","$6x+16$","$6x+24$"], correct=0),
    dict(q="若工廠為節省材料，欲將邊框的寬度縮減為原來的一半，則省下的邊框面積為多少平方公分？", options=["$3x+4$","$3x+6$","$6x+8$","$6x+12$"], correct=3),
  ]),
  dict(type="fill", title="二、非選擇題－填充", meta="每格4分，共20分", items=[
    dict(q=r"計算多項式 $-4(2x+7)^2-5$ 除以 $2x+7$ 後，所得商式與餘式兩者之和為", answers=["-8x-33"], show=r"$-8x-33$"),
    dict(q=r"若 $(ax-6)(2x-b)=10x^2+cx-18$，則 $a+b+c=$", answers=["5"], show="5"),
    dict(q=r"右圖多邊形的面積可以 $x$ 的多項式表示為", image=IMG+"f3.png", answers=["13x^2+18x+22"], show=r"$13x^2+18x+22$"),
    dict(q=r"已知 $2x^2+3x+1$ 除以多項式 $A$ 得商式為 $2x-1$，餘式為 3，則多項式 $A=$", answers=["x+2"], show=r"$x+2$"),
    dict(q=r"若 $(x-2)$ 與 $(x-3)$ 均能整除 $2x^2+mx+n$，則 $m+n=$", answers=["2"], show="2"),
  ]),
  dict(type="calc", title="三、非選擇題－計算", meta="每題10分，共30分（過程寫在計算紙上，每小題填最後答案）", items=[
    dict(q=r"老師以直式除法做一個多項式的除法示範後，擦掉計算過程中的部分數字，並以 $a$、$b$、$c$、$d$、$e$、$f$、$g$ 表示，如右上圖所示，請回答下列問題：", image=IMG+"c1.png",
         parts=[dict(p=r"$a$、$d$ 之值分別為何？（4分）", answers=["a=4,d=-16","d=-16,a=4"], show=r"$a=4$，$d=-16$", hint="例：a=1,d=2"),
                dict(p=r"$c+f+e=$？（6分）", answers=["-17"], show="$-17$")]),
    dict(q=r"如右圖，四邊形 $ABCD$ 中，$\angle A=\angle C=90^\circ$，$E$、$F$ 兩點分別在 $\overline{AD}$、$\overline{BC}$ 上。若 $\overline{AB}=2x+1$，$\overline{CD}=2x-5$，$\overline{BF}=5x-3$，$\overline{DE}=3x+5$，請回答下列問題：", image=IMG+"c2.png",
         parts=[dict(p=r"請以 $x$ 的多項式表示四邊形 $EBFD$ 的面積。（7分）", answers=["8x^2-9x+10","(8x^2-9x+10)"], show=r"$(8x^2-9x+10)$ 平方單位"),
                dict(p=r"若 $x=6$，則四邊形 $EBFD$ 的面積為何？（3分）", answers=["244"], show="244 平方單位")]),
    dict(q=r"若 $2x^2-6x+9=a(x+3)^2+b(x-2)+c$，請回答下列問題：",
         parts=[dict(p=r"$a=$？", answers=["2"], show="2"),
                dict(p=r"$b+c=$？", answers=["-63"], show="$-63$")]),
  ]),
  dict(type="fill", title="非選擇題－填充", meta="【B部分 學力精熟題】每格4分，共20分", items=[
    dict(q=r"若 $x-3$ 能同時整除 $3x^2-10x+a$ 與 $2x^2+bx-3$，則 $ab=$", answers=["-15"], show="$-15$"),
    dict(q=r"已知一梯形的上底為 $4x-14$，下底為 $9x+15$，面積為 $13x^2+27x+2$ 平方單位，則高為", answers=["2x+4"], show=r"$2x+4$"),
    dict(q=r"已知 $4x^2+1$ 除以 $4x+3$ 的商式為 $x-\dfrac{3}{4}$，餘式為 $\dfrac{13}{4}$，若 $8x^2+2$ 除以 $2x+\dfrac{3}{2}$ 的商式為 $A$，餘式為 $B$，則 $A+B=$", answers=["4x+7/2","7/2+4x","4x+3.5"], show=r"$4x+\dfrac{7}{2}$", hint="分數寫成 7/2"),
    dict(q=r"多項式 $(6x+2)^2+9x-7$ 除以 $3x+1$ 的餘式為", answers=["-10"], show="$-10$"),
    dict(q=r"若多項式 $9x^2-(m-1)x+25$ 可化為 $(3x+k)^2$ 的形式，則 $m=$", answers=["-29或31"], show="$-29$ 或 31", hint="兩個答案用「或」隔開"),
  ]),
]
