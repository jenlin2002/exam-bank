META = dict(n=6, h1="第6回・2-2 根式的運算", subtitle="2-2 根式的運算", lesson="2-2", title="根式的運算")
IMG = "images/test6/"
CROPS = [("q9_shapes",11,(884,352,1100,446)), ("c1",12,(330,90,566,214))]
SQ = "根號可打 √ 或 sqrt，例：sqrt13+sqrt7"
SECTIONS = [
  dict(type="mc", title="一、選擇題", meta="【A部分 學力基礎題】每題3分，共30分", items=[
    dict(q=r"下列根式的運算，正確的有哪些？<br>(甲) $\sqrt{2}+\sqrt{10}=\sqrt{12}$　(乙) $\sqrt{13}-\sqrt{8}=\sqrt{5}$<br>(丙) $\sqrt{3}\times\sqrt{5}=\sqrt{15}$　(丁) $\sqrt{14}\div\sqrt{2}=\sqrt{7}$", options=["(甲)(乙)","(甲)(丙)","(乙)(丁)","(丙)(丁)"], correct=3),
    dict(q="下列哪一個算式的值最大？", options=[r"$\sqrt{\dfrac{5}{3}}\div\sqrt{\dfrac{25}{3}}\times\sqrt{\dfrac{5}{2}}\div\sqrt{\dfrac{9}{4}}$", r"$\sqrt{24}\div\sqrt{8}\times\sqrt{3}$", r"$\sqrt{(-4)^2}$", r"$\sqrt{13^2-12^2}$"], correct=3),
    dict(q=r"解方程式 $(\sqrt{5}+1)x=4$，得 $x=$？", options=["1","2",r"$\sqrt{5}-1$",r"$\dfrac{2}{3}(\sqrt{5}+1)$"], correct=2),
    dict(q=r"比較 $\sqrt{2}+\sqrt{3}$ 與 $\sqrt{5}$ 的大小關係，何者較大？", options=[r"$\sqrt{2}+\sqrt{3}$", r"$\sqrt{5}$", "一樣大", "無法比較"], correct=0),
    dict(q=r"若 $\sqrt{18}+\sqrt{98}-\sqrt{72}=\sqrt{a}$，則 $a$ 之值為何？", options=["16","32","48","64"], correct=1),
    dict(q=r"計算 $(1+\sqrt{3}-\sqrt{5})(1-\sqrt{3}+\sqrt{5})$ 之值為何？", options=[r"$5-2\sqrt{3}$", r"$7-4\sqrt{15}$", r"$-7+2\sqrt{15}$", r"$-10+3\sqrt{5}$"], correct=2),
    dict(q=r"$-\sqrt{12}$ 與下列何者<u>不是</u>同類方根？", options=[r"$\sqrt{75}$", r"$\sqrt{27}$", r"$-\sqrt{24}$", r"$-\sqrt{48}$"], correct=2),
    dict(q=r"計算 $\dfrac{9\sqrt{3}+7\sqrt{12}-5\sqrt{48}}{(\sqrt{5}+\sqrt{2})(\sqrt{2}-\sqrt{5})}$ 之值為何？", options=[r"$\sqrt{3}$", r"$-\sqrt{3}$", "3", "$-3$"], correct=1),
    dict(pre="※請閱讀下列敘述後，回答 9.～10. 題\n右圖是小強用電腦軟體設計的正方形與長方形圖案，已知兩個圖案的面積均為 45 平方單位。", preImage=IMG+"q9_shapes.png",
         q="請問正方形的邊長為何？", options=[r"$3\sqrt{3}$", r"$3\sqrt{5}$", r"$5\sqrt{3}$", r"$5\sqrt{5}$"], correct=1),
    dict(q=r"若長方形的長為 $5\sqrt{3}$，則長方形的寬為何？", options=[r"$3\sqrt{3}$", r"$3\sqrt{5}$", r"$5\sqrt{3}$", r"$5\sqrt{5}$"], correct=0),
  ]),
  dict(type="fill", title="二、非選擇題－填充", meta="每格4分，共20分", items=[
    dict(q=r"若 $\sqrt{5}+\sqrt{5}+\sqrt{5}=\sqrt{m}$，$\sqrt{5}\times\sqrt{5}\times\sqrt{5}=\sqrt{n}$，則 $m+n=$", answers=["170"], show="170"),
    dict(q=r"計算 $(\sqrt{7}+\sqrt{8})^{2025}\times(\sqrt{8}-\sqrt{7})^{2025}=$", answers=["1"], show="1"),
    dict(q=r"利用平方差公式計算 $\sqrt{43^2-18^2-25^2}=$", answers=["30"], show="30"),
    dict(q=r"介於 $\dfrac{1}{2+\sqrt{3}}$ 與 $\dfrac{3}{2\sqrt{7}-5}$ 之間的整數共有幾個？", answers=["10"], show="10 個"),
    dict(q=r"已知 $\sqrt{37}\approx6.08$，$\sqrt{370}\approx19.24$，利用根式的運算規則計算 $\sqrt{0.037}\approx$", answers=["0.1924"], show="0.1924"),
  ]),
  dict(type="calc", title="三、非選擇題－計算", meta="每題10分，共30分（過程寫在計算紙上，每小題填最後答案）", items=[
    dict(q=r"團康搶旗遊戲，三位參加者分別從三個不同的點同時出發，經不同路徑到達 $A$ 點，如右上圖，<u>小歐</u>、<u>熙熙</u>、<u>阿迪</u>三人依次分別走 $O\to B\to A$、$P\to C\to A$、$E\to D\to A$ 路徑到達 $A$ 點，其中 $\overline{AB}=\sqrt{7}$，$\overline{AC}=\sqrt{5}$，$\overline{AD}=\sqrt{3}$，$\overline{OB}=\sqrt{13}$，$\overline{PC}=\sqrt{15}$，$\overline{ED}=\sqrt{17}$，請回答下列問題：（註：「→」表示直線前進）", image=IMG+"c1.png",
         parts=[dict(label="(1)", p="<u>小歐</u>所走的路徑長為多少？", answers=["√13+√7","√7+√13"], show=r"$\sqrt{13}+\sqrt{7}$", hint=SQ),
                dict(label="　", p="<u>熙熙</u>所走的路徑長為多少？", answers=["√15+√5","√5+√15"], show=r"$\sqrt{15}+\sqrt{5}$"),
                dict(label="　", p="<u>阿迪</u>所走的路徑長為多少？（(1) 共 3分）", answers=["√17+√3","√3+√17"], show=r"$\sqrt{17}+\sqrt{3}$"),
                dict(label="(2)", p="如果三人的速率相同，則誰先到達 $A$ 點？（7分）", answers=["阿迪"], show="阿迪")]),
    dict(q="計算下列各式，並將結果化為最簡根式：",
         parts=[dict(p=r"$\dfrac{1}{\sqrt{2}+1}=$？（4分）", answers=["√2-1","-1+√2"], show=r"$\sqrt{2}-1$", hint=SQ.replace("sqrt13+sqrt7","sqrt2-1")),
                dict(p=r"$\dfrac{1}{\sqrt{2}+1}+\dfrac{1}{\sqrt{3}+\sqrt{2}}+\dfrac{1}{\sqrt{4}+\sqrt{3}}+\cdots+\dfrac{1}{\sqrt{49}+\sqrt{48}}=$？（6分）", answers=["6"], show="6")]),
    dict(q=r"已知 $a$、$b$ 皆為正整數，且 $a$、$b$ 均不超過 100，若 $\sqrt{48\times a}$ 與 $\sqrt{\dfrac{72}{b}}$ 的值也都是正整數，請回答下列問題：",
         parts=[dict(p=r"求 $a$、$b$ 的最大值。（6分）", answers=["75,72","a=75,b=72"], show=r"$a$ 的最大值 75，$b$ 的最大值 72", hint="依序填 a,b，例：1,2"),
                dict(p=r"承 (1)，此時 $\sqrt{48\times a}$、$\sqrt{\dfrac{72}{b}}$ 的值分別為何？（4分）", answers=["60,1"], show=r"$\sqrt{48\times a}=60$，$\sqrt{\dfrac{72}{b}}=1$", hint="依序填兩個值，例：1,2")]),
  ]),
  dict(type="fill", title="非選擇題－填充", meta="【B部分 學力精熟題】每格4分，共20分", items=[
    dict(num="1.(1)", q=r"計算並化為最簡根式：$\dfrac{2\sqrt{3}-1}{2-\sqrt{3}}-\dfrac{2\sqrt{3}+1}{2+\sqrt{3}}-\left(\dfrac{4}{\sqrt{6}+\sqrt{2}}\right)^2=$", answers=["4√3"], show=r"$4\sqrt{3}$", hint="根號可打 √ 或 sqrt"),
    dict(num="1.(2)", q=r"計算並化為最簡根式：$\dfrac{3+\sqrt{6}}{5\sqrt{3}-\sqrt{32}+\sqrt{50}-2\sqrt{12}}=$", answers=["√3"], show=r"$\sqrt{3}$"),
    dict(num="2.", q=r"若 $\sqrt{13}$ 的小數部分為 $a$，$\dfrac{1}{a}$ 的小數部分為 $b$，則 $b=$", answers=["(√13-1)/4","(-1+√13)/4"], show=r"$\dfrac{\sqrt{13}-1}{4}$", hint="寫成 (sqrt13-1)/4"),
    dict(num="3.", q=r"若 $x=2\sqrt{5}-\sqrt{3}$，$y=2\sqrt{5}+\sqrt{3}$，則 $\dfrac{y}{x}+\dfrac{x}{y}=$", answers=["46/17"], show=r"$\dfrac{46}{17}$", hint="分數寫成 46/17"),
    dict(num="4.", q=r"計算 $\sqrt{359\dfrac{1}{361}}=$", answers=["360/19","18 18/19"], show=r"$\dfrac{360}{19}$", hint="分數寫成 360/19"),
  ]),
]
