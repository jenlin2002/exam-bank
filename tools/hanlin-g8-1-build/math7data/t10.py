META = dict(n=10, h1="第10回・2-1～2-4 複習", subtitle="2-1～2-4 複習", lesson="2-1～2-4", title="複習")
IMG = "images/test10/"
CROPS = [("q9_tiles",19,(688,548,1042,672)), ("c3",20,(985,58,1122,295))]
FR = "分數寫成 3/4"
SECTIONS = [
  dict(type="mc", title="一、選擇題", meta="【A部分 學力基礎題】每題3分，共30分", items=[
    dict(q=r"算式 $\dfrac{2}{3}+\dfrac{5}{3}\div\left(-1\dfrac{1}{4}\right)$ 之值為何？", options=[r"$-\dfrac{35}{12}$",r"$-\dfrac{28}{15}$",r"$-\dfrac{2}{3}$",r"$\dfrac{5}{12}$"], correct=2),
    dict(q=r"已知甲 $=-2\dfrac{7}{8}$，乙 $=-2+\dfrac{7}{8}$，丙 $=-2.875$，則下列何者正確？", options=["甲＝乙","乙＝丙","甲＝丙","甲×乙×丙＞0"], correct=2),
    dict(q=r"算式 $\left(-\dfrac{2}{3}\right)^0\div\left(-\dfrac{5}{4}\right)^2+1$ 之值為何？", options=[r"$\dfrac{41}{25}$",r"$\dfrac{9}{25}$",r"$-\dfrac{9}{25}$",r"$-\dfrac{41}{25}$"], correct=0),
    dict(q=r"若七位數 $2a9608b$ 是 66 的倍數，則 $a+b=$？", options=["2","5","9","11"], correct=1),
    dict(q=r"若 $A=1.04\times10^5$，則下列哪一個數<u>不是</u> $A$ 的因數？", options=["26","65","128","320"], correct=2),
    dict(q=r"已知 $A=2^2\times3^2\times5^4$，$B=2\times3^2\times5^2\times7^2$，$C=2\times3^4\times5^3$，則 $A$、$B$、$C$ 三數的大小關係為何？", options=["$A>B>C$","$B>A>C$","$A>C>B$","$B>C>A$"], correct=0),
    dict(q="<u>建明</u>和<u>宏志</u>兩人到運動用品店買了若干顆價格相同的棒球，已知<u>建明</u>花了 840 元，<u>宏志</u>花了 960 元。若一顆棒球價格在 50～100 元間，則他們共買了多少顆棒球？", options=["28","30","32","34"], correct=1),
    dict(q=r"算式 $\left(1+\dfrac{1}{2}\right)\times\left(1+\dfrac{1}{3}\right)\times\left(1+\dfrac{1}{4}\right)\times\cdots\times\left(1+\dfrac{1}{99}\right)\times\left(1+\dfrac{1}{100}\right)$ 之值為何？", options=[r"$\dfrac{99}{100}$",r"$\dfrac{101}{99}$",r"$\dfrac{2}{101}$",r"$\dfrac{101}{2}$"], correct=3),
    dict(pre="※請閱讀下列敘述後，回答 9.～10. 題\n張老師有 3 種不同形狀的磁磚，分別是正方形，等腰直角三角形及長方形，他將 3 種磁磚發給小真、小正、小美，請 3 人同時拼貼相同大小的正方形區域，則 3 人在磁磚拼貼彩繪後的作品，如下圖所示。", preImage=IMG+"q9_tiles.png",
         q="<u>小正</u>的作品中彩繪（塗色）部分占整個正方形區域的幾分之幾？", options=[r"$\dfrac{3}{8}$",r"$\dfrac{1}{2}$",r"$\dfrac{5}{8}$",r"$\dfrac{7}{8}$"], correct=2),
    dict(q="承 9. 題，3 人的塗色面積最小的是誰？比塗色面積最大的少了多少？", options=[r"<u>小正</u>最小，比<u>小美</u>少 $\dfrac{1}{8}$",r"<u>小正</u>最小，比<u>小真</u>少 $\dfrac{1}{9}$",r"<u>小真</u>最小，比<u>小美</u>少 $\dfrac{1}{9}$",r"<u>小美</u>最小，比<u>小正</u>少 $\dfrac{1}{8}$"], correct=2),
  ]),
  dict(type="fill", title="二、非選擇題－填充", meta="每格4分，共20分", items=[
    dict(q=r"計算 $\left(-2\dfrac{1}{3}\right)-(-4.25)+3.125=$", answers=["121/24","5 1/24"], show=r"$\dfrac{121}{24}$", hint=FR),
    dict(q=r"若 $a=2^5\times3^4\times7$，$b=2^3\times3^2\times5$，則 $\dfrac{[a,b]}{(a,b)}=$", answers=["1260"], show="1260"),
    dict(q="為迎接聖誕節，<u>美琳</u>買了 3 條彩帶來佈置教室，彩帶長度分別為 126 公分、147 公分、189 公分，若想將這些彩帶剪成每條等長的小彩帶，則最少可剪成幾條？", answers=["22"], show="22 條"),
    dict(q="<u>我家便利商店</u>因全年無休，每天都必須有人輪班，採輪休制，若店員<u>陳</u>先生每上班 4 天休息 1 天，而店員<u>李</u>小姐則是每上班 3 天休息 1 天。若兩人在 3 月 28 日（週四）同時休假，則下一次兩人同時在週四休假是幾月幾日？", answers=["8月15日","8/15"], show="8 月 15 日", hint="例：4月1日"),
    dict(q=r"計算 $\left(-\dfrac{16}{33}\right)\times\dfrac{9}{17}+\dfrac{18}{33}\div\left(-\dfrac{17}{9}\right)=$", answers=["-6/11"], show=r"$-\dfrac{6}{11}$", hint=FR),
  ]),
  dict(type="calc", title="三、非選擇題－計算", meta="每題10分，共30分（過程寫在計算紙上，每小題填最後答案）", items=[
    dict(q="<u>兩津</u>、<u>本田</u>、<u>寺井</u>三人繞著一個周長為 120 公尺的操場慢跑，已知<u>兩津</u>每秒跑 6 公尺，<u>本田</u>每秒跑 5 公尺，<u>寺井</u>每秒跑 4 公尺，且三人同時同地點同方向出發，則：",
         parts=[dict(label="(1)", p="<u>兩津</u>跑一圈操場需幾秒？", answers=["20"], show="20 秒"),
                dict(label="　", p="<u>本田</u>跑一圈操場需幾秒？", answers=["24"], show="24 秒"),
                dict(label="　", p="<u>寺井</u>跑一圈操場需幾秒？（(1) 共 6分）", answers=["30"], show="30 秒"),
                dict(label="(2)", p="當從起點起跑後，3 人第一次在起跑點相遇時，<u>寺井</u>已經跑了多少圈？（4分）", answers=["4"], show="4 圈")]),
    dict(q=r"<u>靜涵</u>在賣場買了一罐水果彩虹糖，她發現裡面有 $\dfrac{1}{5}$ 是紅色糖果，$\dfrac{1}{4}$ 是橙色糖果，$\dfrac{1}{3}$ 是黃色糖果，其餘都是綠色糖果。回家後，弟弟馬上挑了綠色糖果出來吃，並且說：「我吃了綠色糖果的一半，共有 13 顆！」，則：",
         parts=[dict(p="綠色糖果占全部的幾分之幾？", answers=["13/60"], show=r"$\dfrac{13}{60}$", hint=FR),
                dict(p="罐子裡的黃色糖果有多少顆？", answers=["40"], show="40 顆")]),
    dict(q=r"<u>國銀</u>買了相同容量且瓶蓋大小相同的洗衣精和柔軟精各 1 瓶，其使用說明如圖(一)、圖(二)所示。他先按照自己的使用習慣，每次洗衣服都用 $\dfrac{2}{5}$ 瓶蓋的洗衣精加上 $\dfrac{1}{2}$ 瓶蓋的柔軟精，在洗衣服 20 次後，感覺洗衣的效果不好，此時柔軟精剩 $\dfrac{3}{4}$ 瓶，則：", image=IMG+"c3.png",
         parts=[dict(p="每瓶柔軟精的容量可倒滿幾瓶蓋？", answers=["40"], show="40 瓶蓋"),
                dict(p="若之後<u>國銀</u>改成圖(一)的使用方式，則洗衣精最多還可再完整使用多少次？", answers=["53"], show="53 次")]),
  ]),
  dict(type="fill", title="非選擇題－填充", meta="【B部分 學力精熟題】每格4分，共20分", items=[
    dict(q=r"計算 $6^7\times7^2\times15^6\times13^2$ 乘開後，末尾有幾個 0？", answers=["6"], show="6 個"),
    dict(q=r"已知 $-5\dfrac{2}{11}$ 和 $7\dfrac{4}{13}$ 同乘以一個正分數後，均可化為整數，則此正分數最小為", answers=["143/19","7 10/19"], show=r"$\dfrac{143}{19}$", hint=FR),
    dict(q=r"有紅、白兩色的卡片共 96 張，甲、乙兩人各拿 48 張。若甲拿的卡片中有 $\dfrac{7}{16}$ 是紅色的，乙拿的白色卡片是甲拿的白色卡片的 $\dfrac{2}{3}$，則此 96 張卡片中，紅色卡片比白色卡片多幾張？", answers=["6"], show="6 張"),
    dict(q=r"若 $a=8^9$，$b=16^7$，$c=32^5$，則 $a$、$b$、$c$ 的大小關係為", answers=["b>a>c","c<a<b"], show="$b>a>c$", hint="例：a>b>c"),
    dict(q="有一個整數介於 300～400 之間，此數除以 8 餘 6，除以 9 餘 7，除以 15 餘 13，則這個正整數為", answers=["358"], show="358"),
  ]),
]
