META = dict(n=12, h1="第12回・3-2 解一元一次方程式", subtitle="3-2 解一元一次方程式", lesson="3-2", title="解一元一次方程式")
IMG = "images/test12/"
CROPS = [("q8",23,(705,255,1122,400)), ("q9_cable",23,(908,452,1112,632)), ("f3",24,(395,58,578,160)),
         ("c2",24,(100,848,578,1108)), ("b3",24,(920,1048,1122,1158))]
FR = "分數寫成 3/4，帶分數寫成 1 3/4"
SECTIONS = [
  dict(type="mc", title="一、選擇題", meta="【A部分 學力基礎題】每題3分，共30分", items=[
    dict(q=r"下列何者是方程式 $x\div7-5=35$ 的解？", options=[r"$x=35+5\times7$",r"$x=(35+5)\times7$",r"$x=35-5\div7$",r"$x=35\div(5\times7)$"], correct=1),
    dict(q=r"下列何者是一元一次方程式 $x-1=\dfrac{x}{3}+\dfrac{x}{6}$ 的解？", options=[r"$x=-\dfrac{1}{2}$",r"$x=\dfrac{1}{3}$","$x=1$","$x=2$"], correct=3),
    dict(q=r"將方程式 $\dfrac{3x+1}{4}-\dfrac{x-2}{5}=1$ 的等號兩邊同乘以 20 之後，下列關於 $x$ 的敘述何者正確？", options=["$x$ 的值會變為原來的 20 倍",r"$x$ 的值變為原來的 $\dfrac{1}{20}$","$x$ 的值與原來相同","$x$ 的值為 7"], correct=2),
    dict(q="若 $-2$ 是 $x$ 的一元一次方程式 $5a-7x=-6$ 的解，則 $a$ 之值為何？", options=["$-3$","$-4$","$-5$","$-6$"], correct=1),
    dict(q="$x=-4$ 是下列哪一個一元一次方程式的解？", options=["$-3x+10=-x+2$","$4(x+3)=2x+2$","$14-3x=8$",r"$\dfrac{x+8}{2}=2$"], correct=3),
    dict(q=r"解一元一次方程式 $\dfrac{1}{3}x-2=\dfrac{1}{2}x+3$，則 $x=$？", options=["$-30$","$-6$","$-5$","30"], correct=0),
    dict(q="$x$ 的一元一次方程式 $x-1=3x-a$ 與 $x-a=1$ 有相同的解，則 $a$ 之值為何？", options=["$-3$","$-2$","$-1$","2"], correct=0),
    dict(q="<u>俊成</u>將三種不同的積木放在天平的兩側，已知相同的積木重量相等，若下列選項中只有一個天平<u>無法</u>平衡，試判斷為下列何者？", image=IMG+"q8.png", options=["A","B","C","D"], correct=2),
    dict(pre="※請閱讀下列敘述後，回答 9.～10. 題\n某旅行團到遊樂區遊玩，右圖為選擇方案與所需費用。已知參加旅行團的所有團員都從這兩種方案中選擇一種，統計後發現，去程總共有 18 人搭乘纜車，回程總共有 9 人搭乘纜車。", preImage=IMG+"q9_cable.png",
         q="若選擇甲方案的有 $x$ 人，則選擇乙方案的有多少人？", options=["$27-x$","$27-2x$","$27+x$","$27+2x$"], correct=1),
    dict(q=r"承 9. 題，若根據選擇的方案列出此旅行團搭乘纜車的總花費方程式為 $400x+(18-x)\times250+(9-x)\times250=6150$，則選擇甲方案的有多少人？", options=["6","7","8","9"], correct=0),
  ]),
  dict(type="fill", title="二、非選擇題－填充", meta="每格4分，共20分", items=[
    dict(num="1.", q=r"解一元一次方程式 $x=1-\dfrac{x}{2}+\dfrac{x}{4}-\dfrac{x}{8}+\dfrac{x}{16}$，則 $x=$", answers=["16/21"], show=r"$\dfrac{16}{21}$", hint=FR),
    dict(num="2.(1)", q=r"解方程式：$2(3-x)+6=-4(x+5)$，$x=$", answers=["-16"], show="$-16$"),
    dict(num="2.(2)", q=r"解方程式：$\dfrac{1}{6}x-\dfrac{2}{3}=\dfrac{4}{3}x-1$，$x=$", answers=["2/7"], show=r"$\dfrac{2}{7}$", hint=FR),
    dict(num="2.(3)", q=r"解方程式：$0.7(x+2)=0.5(-2x-1)+1$，$x=$", answers=["-9/17"], show=r"$-\dfrac{9}{17}$", hint=FR),
    dict(num="3.", q=r"如右表，則 $a\times b\times c\times d=$", image=IMG+"f3.png", answers=["0"], show="0"),
  ]),
  dict(type="calc", title="三、非選擇題－計算", meta="每題10分，共30分（過程寫在計算紙上，每小題填最後答案）", items=[
    dict(q=r"一元一次方程式 $\dfrac{2x+1}{3}-\dfrac{1-x}{2}=1\dfrac{5}{6}$ 的解在兩個連續整數 $a$、$b$ 之間，則：",
         parts=[dict(p="求解 $x=$？", answers=["1 5/7","12/7"], show=r"$1\dfrac{5}{7}$", hint=FR),
                dict(p="$a+b=$？", answers=["3"], show="3")]),
    dict(q=r"黑板上老師出了一題方程式 $\dfrac{3x-0.1}{0.2}=1$，請<u>姿妤</u>和<u>小建</u>兩人同時解題如下表。試回答下列問題：", image=IMG+"c2.png",
         parts=[dict(p="判斷<u>姿妤</u>的解是否正確？", answers=["正確","是"], show="正確", hint="填「正確」或「不正確」"),
                dict(p="判斷<u>小建</u>的解是否正確？若不正確，正確的解 $x=$？", answers=["不正確,x=0.1","不正確,0.1","0.1","x=0.1"], show="不正確，因 $x=0.1$", hint="例：不正確,x=1")]),
    dict(q=r"<u>小夫</u>在計算方程式 $\dfrac{1}{3}x+4=\dfrac{1}{2}(x+a)$ 時，誤將 $\dfrac{1}{3}x+4$ 看成 $\dfrac{1}{3}x\div4$，其他的計算過程皆正確，最後算出 $x=-6$ 的答案，則：",
         parts=[dict(p="$a$ 值＝？", answers=["5"], show="5"),
                dict(p="正確解 $x=$？", answers=["9"], show="9")]),
  ]),
  dict(type="fill", title="非選擇題－填充", meta="【B部分 學力精熟題】每格4分，共20分", items=[
    dict(q=r"若 $\dfrac{1}{5}-\dfrac{1}{5}\left[2-\left(\dfrac{1}{3}x+2\right)\right]=1$，則 $2x-1=$", answers=["23"], show="23"),
    dict(q=r"<u>建銘</u>求出 $-2$ 是 $x$ 的一元一次方程式 $ax+b=c$ 的解，若 $a\neq0$，則 $6ax+5c=5b$ 的解 $x=$", answers=["5/3","1 2/3"], show=r"$\dfrac{5}{3}$", hint=FR),
    dict(q="如右圖，<u>小帆</u>在寫數學作業時，不小心打翻墨水，導致塗汙表格中的兩格數字，則這兩格數字的和為", image=IMG+"b3.png", answers=["-7 4/5","-39/5","-7.8"], show=r"$-7\dfrac{4}{5}$", hint=FR),
    dict(q=r"已知 $x$ 的一元一次方程式 $3x+6=2ax$ 的解是正整數且 $a$ 為整數，則 $a$ 之值可能為", answers=["2或3"], show="2 或 3", hint="多個答案用「或」隔開"),
    dict(q=r"若 $\dfrac{3}{2}$ 是 $x$ 的一元一次方程式 $\dfrac{a-x}{3}=\dfrac{bx-2}{4}$ 的解，其中 $a\times b\neq0$，則 $\dfrac{b}{a}+\dfrac{a}{b}=$", answers=["145/72","2 1/72"], show=r"$\dfrac{145}{72}$", hint=FR),
  ]),
]
