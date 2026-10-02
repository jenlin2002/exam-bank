META = dict(n=7, h1="第7回・2-3 畢氏定理", subtitle="2-3 畢氏定理", lesson="2-3", title="畢氏定理")
IMG = "images/test7/"
CROPS = [("q6",13,(438,1166,562,1292)), ("q8",13,(970,150,1106,314)), ("q9_radar",13,(944,426,1102,614)),
         ("f1",13,(956,1124,1108,1238)), ("f3",13,(966,1432,1108,1534)), ("f5",14,(424,242,564,384)),
         ("c1",14,(422,508,564,632)), ("c2",14,(400,1080,564,1202)), ("c3",14,(1004,54,1108,194)),
         ("b1",14,(992,566,1108,694)), ("b2",14,(1000,806,1108,932)), ("b3",14,(928,1082,1108,1202)), ("b4",14,(956,1282,1108,1410))]
SQ = "根號可打 √ 或 sqrt"
SECTIONS = [
  dict(type="mc", title="一、選擇題", meta="【A部分 學力基礎題】每題3分，共30分", items=[
    dict(q=r"直角三角形 $ABC$ 中，$\overline{AB}=3$，$\overline{BC}=5$，$\overline{AC}=4$，$\overline{AD}$ 為斜邊上的高，則 $\overline{AD}=$？", options=[r"$\dfrac{6}{5}$",r"$\dfrac{9}{5}$",r"$\dfrac{12}{5}$",r"$\dfrac{16}{5}$"], correct=2),
    dict(q="下列敘述何者正確？", options=[r"$\sqrt{5}$、$\sqrt{12}$、$\sqrt{17}$ 為直角三角形的三邊長", r"若直角三角形的三邊長分別為 $a$、$b$、$c$，則 $a^2+b^2=c^2$", r"若直角三角形的三邊長分別為 $3a$、$4b$、$5c$，則 $(3a)^2+(4b)^2=(5c)^2$", "若直角三角形的兩股長分別為 7、25，則斜邊長等於 24"], correct=0),
    dict(q="下列哪一點與坐標平面上原點的距離最遠？", options=["$(5,-5)$","$(3,3.5)$","$(0,-7)$","$(-4,-6)$"], correct=3),
    dict(q=r"若直角三角形的三邊長為 5、12、$x$，則 $x=$？", options=["13",r"$\sqrt{119}$",r"13 或 $\sqrt{119}$","無法判斷"], correct=2),
    dict(q=r"$\triangle ABC$ 中，已知 $\angle C=54^\circ$，且 $\angle A:\angle B=5:2$，則下列何者正確？", options=[r"$\overline{AB}^2+\overline{AC}^2=\overline{BC}^2$", r"$\overline{AB}^2+\overline{BC}^2=\overline{AC}^2$", r"$\overline{AC}^2+\overline{BC}^2=\overline{AB}^2$", r"$\overline{AB}+\overline{BC}=\overline{AC}$"], correct=0),
    dict(q=r"如右圖，四邊形 $ABCD$ 中，$\angle A=\angle C=90^\circ$。若 $\overline{BC}=\overline{CD}=5$，$\overline{AD}=2$，則 $\overline{AB}$ 長度的範圍為何？", image=IMG+"q6.png", options=[r"$5<\overline{AB}<6$", r"$6<\overline{AB}<7$", r"$7<\overline{AB}<8$", r"$8<\overline{AB}<9$"], correct=1),
    dict(q=r"坐標平面上有 $A(1,3)$、$B(2,5)$ 兩點，則下列各組兩點間的距離何者與 $\overline{AB}$ <u>不相等</u>？", options=["$(3,1)$、$(5,2)$","$(-1,-3)$、$(-2,-5)$","$(1+50,3+80)$、$(2+50,5+80)$",r"$(1\times11,3\times11)$、$(2\times11,5\times11)$"], correct=3),
    dict(q=r"如右圖，兩個正方形重疊，若正方形 $ABDE$ 的面積為 169 平方公分，正方形 $BCFG$ 的面積為 144 平方公分，則 $\overline{AF}$ 的長度為多少公分？", image=IMG+"q8.png", options=["5","6","7","8"], correct=2),
    dict(pre="※請閱讀下列敘述後，回答 9.～10. 題\n右圖是陳博士發明的一款海洋探測器，只要當船隻與探測器的距離不超過 50 公里時，探測器均會發出聲音通知，今以探測器的位置為坐標平面上的原點，且單位長為 1 公里。", preImage=IMG+"q9_radar.png",
         q="若有一艘船隻位於 $(35,35)$，則此船隻與探測器距離多少公里？此時探測器是否會發出聲音通知？", options=[r"距離 $35\sqrt{2}$ 公里，此時探測器會發出聲音通知", r"距離 $35\sqrt{3}$ 公里，此時探測器會發出聲音通知", r"距離 $35\sqrt{2}$ 公里，此時探測器不會發出聲音通知", r"距離 $35\sqrt{3}$ 公里，此時探測器不會發出聲音通知"], correct=0),
    dict(q="若有一艘船隻位於 $(100,240)$，並以時速 105 公里直線往探測器前進，且中間不停留，則幾小時後，探測器會開始發出聲音通知？", options=["1.5","2","2.5","3"], correct=1),
  ]),
  dict(type="fill", title="二、非選擇題－填充", meta="每格4分，共20分", items=[
    dict(q=r"如右圖，<u>小鶯</u>將 $\overline{AD}=100$ 公分、$\overline{AB}=80$ 公分的長方形色紙 $ABCD$ 摺疊，使得頂點 $D$ 落在 $\overline{BC}$ 上的 $F$ 點，則 $\overline{EF}=$ 多少公分？", image=IMG+"f1.png", answers=["50"], show="50 公分"),
    dict(q=r"在坐標平面上，原點 $O$ 到方程式 $x+y=8$ 的圖形的最短距離為", answers=["4√2"], show=r"$4\sqrt{2}$", hint=SQ),
    dict(q="如右圖，某款平板電腦的螢幕是長方形，其長寬比為 4：3，若對角線長為 15 吋，則此平板電腦螢幕面積為多少平方吋？", image=IMG+"f3.png", answers=["108","108平方吋"], show="108 平方吋"),
    dict(q="<u>振益</u>、<u>學俄</u>兩人騎腳踏車從學校的大門口同時出發，<u>振益</u>以每小時 16 公里的速率向南行，<u>學俄</u>以每小時 12 公里的速率向東行，則幾小時之後兩人相距 72 公里？", answers=["3.6","3.6小時"], show="3.6 小時"),
    dict(q="如右圖，以四個完全相同的直角三角形和一個小正方形，組合成一個大正方形。已知直角三角形的兩股分別是 20 公分和 15 公分，則大、小兩正方形的邊長相差多少公分？", image=IMG+"f5.png", answers=["20"], show="20 公分"),
  ]),
  dict(type="calc", title="三、非選擇題－計算", meta="每題10分，共30分（過程寫在計算紙上，每小題填最後答案）", items=[
    dict(q=r"如右圖，$\triangle ABC$ 中，$\overline{AB}=13$，$\overline{BC}=14$，$\overline{AC}=15$，$\overline{AH}$ 是 $\overline{BC}$ 上的高，請回答下列問題：", image=IMG+"c1.png",
         parts=[dict(p=r"$\overline{AH}$ 的長度為何？（6分）", answers=["12"], show="12"),
                dict(p=r"利用 (1) 的結果，求 $\triangle ABC$ 中，$\overline{AC}$ 上的高為多少？（4分）", answers=["56/5","11.2","11 1/5"], show=r"$\dfrac{56}{5}$", hint="分數寫成 56/5")]),
    dict(q=r"如右圖，一直線通過 $A(-5\sqrt{2},0)$，且交 $y$ 軸於 $B$ 點，若 $\overline{AB}=5\sqrt{3}$，請回答下列問題：", image=IMG+"c2.png",
         parts=[dict(p=r"$B$ 點坐標為何？", answers=["(0,5)"], show="$(0,5)$", hint="寫成 (0,1) 的形式"),
                dict(p=r"$O$ 點到此直線的距離為多少？", answers=["5√6/3","(5√6)/3","5/3√6"], show=r"$\dfrac{5\sqrt{6}}{3}$", hint="寫成 5sqrt6/3")]),
    dict(q="如右圖，<u>靜萍</u>將一竹竿在離牆腳 7 公尺處斜放在牆邊，此時竹竿頂剛好離地面 24 公尺。請回答下列問題：", image=IMG+"c3.png",
         parts=[dict(p="此竹竿長為多少公尺？", answers=["25"], show="25 公尺"),
                dict(p="今移動此竹竿使它在離牆腳 15 公尺處斜放，此時竹竿頂離地面多少公尺？", answers=["20"], show="20 公尺")]),
  ]),
  dict(type="fill", title="非選擇題－填充", meta="【B部分 學力精熟題】每格4分，共20分", items=[
    dict(num="1.", q=r"如右圖，在等腰直角三角形 $ABC$ 中，$\angle B=90^\circ$，$\overline{AB}=\overline{BC}=14$，將 $\triangle ADE$ 沿 $\overline{DE}$ 對摺，使 $A$ 點落在 $\overline{BC}$ 中點 $F$，則 $\overline{BD}=$", image=IMG+"b1.png", answers=["21/4","5.25","5 1/4"], show=r"$\dfrac{21}{4}$", hint="分數寫成 21/4"),
    dict(num="2.", q=r"如右圖，四邊形 $ABCD$ 中，$\angle B=\angle C=90^\circ$，$\overline{DF}\perp\overline{AE}$。若 $\overline{AB}=4$，$\overline{BE}=3$，$\overline{CE}=2$，$\overline{CD}=3$，$\overline{DF}=\dfrac{17}{5}$，則 $\overline{AF}=$", image=IMG+"b2.png", answers=["19/5","3.8","3 4/5"], show=r"$\dfrac{19}{5}$", hint="分數寫成 19/5"),
    dict(num="3.", q=r"如右圖，半圓 $O$ 的半徑為 17，若 $\overline{AB}\perp\overline{OE}$，$\overline{DC}\perp\overline{OE}$，$\overline{AB}=15$，$\overline{DC}=8$，$\overline{CE}=2$，則 $\overline{AD}=$", image=IMG+"b3.png", answers=["7√2"], show=r"$7\sqrt{2}$", hint=SQ),
    dict(num="4.", q=r"如右圖，正方形 $ABCD$ 外有一個 $\triangle ABO$。今固定 $B$ 點，將 $\triangle ABO$ 依逆時針方向旋轉，使得 $\overline{AB}$ 與 $\overline{BC}$ 重疊，形成新的 $\triangle BCP$。若 $\angle PBC=\angle OBA=40^\circ$，$\overline{OB}=4$，則 $\overline{OP}=$", image=IMG+"b4.png", answers=["4√2"], show=r"$4\sqrt{2}$", hint=SQ),
    dict(num="　", q=r"承上題，$B$ 點到 $\overline{OP}$ 的距離為", answers=["2√2"], show=r"$2\sqrt{2}$"),
  ]),
]
