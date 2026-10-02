META = dict(n=8, h1="第8回・2-3 分數的四則運算", subtitle="2-3 分數的四則運算", lesson="2-3", title="分數的四則運算")
IMG = "images/test8/"
CROPS = [("q9_table",15,(898,408,1110,560)), ("q9_pizza",15,(1025,612,1122,705)), ("c2",16,(465,972,575,1145)), ("c3",16,(895,58,1125,190))]
FR = "分數寫成 3/4，帶分數寫成 1 3/4"
SECTIONS = [
  dict(type="mc", title="一、選擇題", meta="【A部分 學力基礎題】每題3分，共30分", items=[
    dict(q=r"算式 $1+\dfrac{3}{2}\times2$ 之值為何？", options=["5","4","3","2"], correct=1),
    dict(q=r"$3\dfrac{5}{7}-6\dfrac{4}{9}$ 可化簡為下列哪一個算式？", options=[r"$3+\dfrac{5}{7}-6+\dfrac{4}{9}$",r"$(3-6)-\left(\dfrac{5}{7}-\dfrac{4}{9}\right)$",r"$3-\dfrac{5}{7}-6-\dfrac{4}{9}$",r"$(3-6)+\left(\dfrac{5}{7}-\dfrac{4}{9}\right)$"], correct=3),
    dict(q=r"算式 $(-1.7)\div\left(\dfrac{5}{3}\times\dfrac{85}{4}\right)$ 之值為何？", options=[r"$-\dfrac{3}{25}$",r"$-\dfrac{25}{3}$",r"$-\dfrac{125}{6}$",r"$-\dfrac{6}{125}$"], correct=3),
    dict(q=r"算式 $\dfrac{11}{7}-\left[\left(-\dfrac{3}{7}\right)-\dfrac{11}{19}\right]$ 之值為何？", options=[r"$2\dfrac{11}{19}$",r"$2\dfrac{8}{19}$",r"$1\dfrac{11}{19}$",r"$1\dfrac{8}{19}$"], correct=0),
    dict(q=r"若 $x=-\dfrac{9}{13}$，$y=-\dfrac{29}{39}$，則介於 $x$、$y$ 之間，且分母為 78 的最簡分數為何？", options=[r"$-\dfrac{53}{78}$",r"$-\dfrac{55}{78}$",r"$-\dfrac{59}{78}$",r"$-\dfrac{61}{78}$"], correct=1),
    dict(q=r"若 $\left(\dfrac{4}{7}-\dfrac{3}{11}\right)\div\square=\dfrac{-4}{7}\times\dfrac{7}{13}+\dfrac{3}{11}\times\dfrac{7}{13}$，則 $\square=$？", options=[r"$\dfrac{7}{13}$",r"$\dfrac{-7}{13}$",r"$\dfrac{13}{7}$",r"$\dfrac{-13}{7}$"], correct=3),
    dict(q=r"算式 $2024\times\dfrac{-2024}{2023}$ 最接近下列哪一個整數？", options=["$-2022$","$-2023$","$-2024$","$-2025$"], correct=3),
    dict(q=r"甲為邊長 $3\dfrac{1}{3}$ 公分的正方形，乙為邊長 $9\dfrac{1}{9}$ 公分的正方形，則甲面積是乙面積的幾倍？", options=[r"$\dfrac{1}{3}$",r"$\dfrac{1}{9}$",r"$\dfrac{9}{100}$",r"$\dfrac{225}{1681}$"], correct=3),
    dict(pre="※請閱讀下列敘述後，回答 9.～10. 題\n九年 1 班在會考完後，決定將剩下的班費用來購買 pizza 舉行同樂會。已知所有尺寸的 pizza 厚度均相同，且 pizza 尺寸為其直徑長度，其尺寸與價格關係如下表所示。", preImage=IMG+"q9_table.png",
         q="如右圖，已知全班有 25 人，若每個大 pizza 可切成 8 片，每人至少都吃到 2 片，則至少需要幾個大 pizza 才夠？", image=IMG+"q9_pizza.png", options=["8","7","6","5"], correct=1),
    dict(q="pizza 店有外帶買大送大的優惠，已知九年 1 班的班費足夠買 6 個大 pizza，再加上買大送大，共可拿到 12 個大 pizza。若改成全部購買個人 pizza，則最多可以買幾個？（個人 pizza 沒有買一送一）", options=["88","86","44","43"], correct=3),
  ]),
  dict(type="fill", title="二、非選擇題－填充", meta="每格4分，共20分", items=[
    dict(q=r"$1\dfrac{5}{7}$ 的倒數與 $\left(-\dfrac{6}{49}\right)$ 的相反數之乘積為", answers=["1/14"], show=r"$\dfrac{1}{14}$", hint=FR),
    dict(q=r"九年甲班有 28 位學生，其中有 $\dfrac{4}{7}$ 戴眼鏡，而且戴眼鏡的學生中有 $\dfrac{5}{8}$ 是男生，則班上戴眼鏡的女生有幾人？", answers=["6"], show="6 人"),
    dict(q=r"計算 $\dfrac{2}{3}-10\dfrac{3}{4}-\left(2\dfrac{1}{3}-1\dfrac{5}{6}\right)=$", answers=["-10 7/12","-127/12"], show=r"$-10\dfrac{7}{12}$", hint=FR),
    dict(q=r"已知 $a=\dfrac{-2019}{2020}$，$b=\dfrac{-2018}{2019}$，$c=\dfrac{-2017}{2018}$，則 $a$、$b$、$c$ 三數的大小關係為", answers=["a<b<c","c>b>a"], show="$a<b<c$", hint="例：a<b<c"),
    dict(q=r"分數 $\dfrac{72}{173}$ 的分母減去 $\square$ 後，新的分數可約分為 $\dfrac{3}{7}$，則 $\square=$", answers=["5"], show="5"),
  ]),
  dict(type="calc", title="三、非選擇題－計算", meta="每題10分，共30分（過程寫在計算紙上，每小題填最後答案）", items=[
    dict(q=r"<u>小霜</u>、<u>大金</u>、<u>小立</u>三人一起喝一瓶 1500 毫升的可樂，<u>小霜</u>喝了 $\dfrac{3}{10}$ 瓶，<u>大金</u>喝的量比<u>小霜</u>多 $\dfrac{1}{12}$ 瓶，最後剩下的都被<u>小立</u>喝光了，則：",
         parts=[dict(p="<u>小霜</u>喝了多少毫升？", answers=["450"], show="450 毫升"),
                dict(p="3 人中喝最多的比喝最少的多了幾毫升？", answers=["125"], show="125 毫升")]),
    dict(q=r"如右圖，有一竹竿垂直插入一水池中，已知竹竿的 $\dfrac{1}{5}$ 在泥土中，剩下的 $\dfrac{2}{3}$ 在水中，且有 $\dfrac{8}{5}$ 公尺的竹竿露出水面上，則：", image=IMG+"c2.png",
         parts=[dict(p="在水中的竹竿占全長的幾分之幾？（3分）", answers=["8/15"], show=r"$\dfrac{8}{15}$", hint=FR),
                dict(p="竹竿的總長度為多少公尺？（7分）", answers=["6"], show="6 公尺")]),
    dict(q="右圖為 <u>GoGo</u> 茶飲販售 3 種飲料的價目表，試問：", image=IMG+"c3.png",
         parts=[dict(p="錫蘭紅茶大杯和中杯每毫升（ml）的價差是多少元？", answers=["1/150"], show=r"$\dfrac{1}{150}$ 元", hint=FR),
                dict(p="若自備環保杯購買者，不論中杯或大杯，每杯均可折價 5 元。<u>小玉</u>帶了 5 個環保杯和 300 元，預計要買 2 杯大杯珍珠奶茶和數杯大杯茉香綠茶，在最省錢的考量下可買幾杯茉香綠茶？（包含裝環保杯的茉香綠茶）", answers=["7"], show="7 杯")]),
  ]),
  dict(type="fill", title="非選擇題－填充", meta="【B部分 學力精熟題】每格4分，共20分", items=[
    dict(q=r"計算 $78\times\left(\dfrac{3}{91}+\dfrac{1}{65}\right)-63\times\left(\dfrac{3}{49}+\dfrac{2}{35}\right)=$", answers=["-129/35","-3 24/35"], show=r"$-\dfrac{129}{35}$", hint=FR),
    dict(q=r"若 $a$、$b$、$c$ 皆為負數，且 $a\div1\dfrac{3}{7}=b\div2\dfrac{1}{3}=c\div\dfrac{11}{8}$，則 $a$、$b$、$c$ 三數的大小關係為", answers=["c>a>b","b<a<c"], show="$c>a>b$", hint="例：a>b>c"),
    dict(q=r"計算 $\dfrac{1}{2}-\dfrac{3}{4}+\dfrac{7}{8}-\dfrac{15}{16}+\dfrac{31}{32}-\dfrac{63}{64}=$", answers=["-21/64"], show=r"$-\dfrac{21}{64}$", hint=FR),
    dict(q=r"<u>杰夫</u>參加萬人健走活動，已知他在走完全程的 $\dfrac{3}{7}$ 後，若再走 1500 公尺，則距終點只剩下全程的 $\dfrac{1}{3}$。請問這次健走活動全程有多少公里？", answers=["6.3"], show="6.3 公里"),
    dict(q=r"數線上有 $A\left(4\dfrac{2}{9}\right)$、$B\left(-1\dfrac{5}{18}\right)$ 兩點。若有一點 $C$ 使得 $\overline{AC}=\overline{BC}$，則 $C$ 點坐標為", answers=["1 17/36","53/36"], show=r"$1\dfrac{17}{36}$", hint=FR),
  ]),
]
