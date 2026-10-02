META = dict(n=9, h1="第9回・2-4 指數律", subtitle="2-4 指數律", lesson="2-4", title="指數律")
IMG = "images/test9/"
CROPS = []
FR = "分數寫成 3/4"
SECTIONS = [
  dict(type="mc", title="一、選擇題", meta="【A部分 學力基礎題】每題3分，共30分", items=[
    dict(q=r"下列何者之值與 $\left(-\dfrac{3}{2}\right)^4$ <u>不相等</u>？", options=[r"$\left(\dfrac{9}{4}\right)^2$",r"$\left(\dfrac{3}{2}\right)^4$",r"$\dfrac{6^2}{2^4}$",r"$\dfrac{3^4}{2^4}$"], correct=2),
    dict(q=r"算式 $\left(-\dfrac{2}{3}\right)^3\times9$ 之值為何？", options=[r"$-\dfrac{8}{3}$","$-2$","2",r"$\dfrac{8}{3}$"], correct=0),
    dict(q="下列算式何者<u>錯誤</u>？", options=[r"$\left(-5\dfrac{1}{7}\right)^3\times\left(5\dfrac{1}{7}\right)^2=\left(-5\dfrac{1}{7}\right)^5$",r"$\left[\left(-7\dfrac{1}{2}\right)^2\right]^3\times\left(-7\dfrac{1}{2}\right)^2=\left(-7\dfrac{1}{2}\right)^7$",r"$\left(-5\dfrac{1}{3}\right)^4\div\left(-5\dfrac{1}{3}\right)^3=-5\dfrac{1}{3}$",r"$\left(-2\dfrac{1}{2}\times7\dfrac{4}{5}\right)^2=\left(-\dfrac{5}{2}\right)^2\times\left(7\dfrac{4}{5}\right)^2$"], correct=1),
    dict(q="下列何者正確？", options=[r"$2^8\times2^4=2^{32}$",r"$(4^3)^4=4^7$",r"$7^9\div7^4=7^5$",r"$9^2\times5^4=15^2$"], correct=2),
    dict(q=r"已知 $a=\left(-\dfrac{4}{5}\right)^6$，$b=\left(-\dfrac{4}{5}\right)^7$，$c=\left(-\dfrac{4}{5}\right)^8$，則 $a$、$b$、$c$ 三數的大小關係為何？", options=["$c>a>b$","$a>c>b$","$c>b>a$","$a>b>c$"], correct=1),
    dict(q=r"算式 $\dfrac{1}{-3}+\dfrac{3}{(-3)^2}+\dfrac{3}{(-3)^3}+\dfrac{3}{(-3)^4}+\dfrac{3}{(-3)^5}$ 之值為何？", options=[r"$-\dfrac{1}{3}$",r"$-\dfrac{1}{9}$",r"$-\dfrac{5}{27}$",r"$-\dfrac{7}{81}$"], correct=3),
    dict(q=r"已知 $(-2^6)^4=(-2^3)^7\times A$，則 $A$ 之值為何？", options=["8","6","$-6$","$-8$"], correct=3),
    dict(q=r"算式 $(-5)^7\times2^6\div(-10)^3$ 之值為何？", options=["5000","1000","$-1000$","$-5000$"], correct=0),
    dict(pre=r"※請閱讀下列敘述後，回答 9.～10. 題" + "\n藥物在人體內經過正常的代謝程序後會排出體外，人體在服用藥物後，藥物在身體血液中的濃度下降為原來的一半所經過的時間，稱為藥物半衰期。例如：某藥物經過 3 個半衰期，血液中藥物濃度已降為原來濃度的 (1/2)³＝1/8，約為 12.5％。",
         q="若某種止痛藥的半衰期是 2.5 小時，<u>小君</u>在早餐後吃了一顆止痛藥，則在經過 2.5 小時後，血液中藥物濃度約為原來藥物濃度的百分之幾？", options=["80％","50％","25％","5％"], correct=1),
    dict(q="已知醫學界定義，若「藥物在血液中濃度降到原來的 5％以下，視為代謝完畢」，則承 9. 題，<u>小君</u>大概在幾個小時後，才會代謝完畢這顆止痛藥？", options=["5","8","10","13"], correct=3),
  ]),
  dict(type="fill", title="二、非選擇題－填充", meta="每格4分，共20分", items=[
    dict(q=r"計算 $\left(-\dfrac{5}{2}\right)^3\times\left(\dfrac{2}{25}\right)^2=$", answers=["-1/10","-0.1"], show=r"$-\dfrac{1}{10}$", hint=FR),
    dict(q=r"計算 $\left(-\dfrac{3}{5}\right)^2\div\left(-\dfrac{3}{2}\right)^3+\left(-\dfrac{3}{5}\right)^2\times\left(-\dfrac{4}{9}\right)=$", answers=["-4/15"], show=r"$-\dfrac{4}{15}$", hint=FR),
    dict(q=r"計算 $(-3)\times2+16\times\left(-\dfrac{1}{2}\right)^2-(-2024)^0=$", answers=["-3"], show="$-3$"),
    dict(q=r"計算 $(2024-2023)^{2025}\times(2023-2024)^{2025}=$", answers=["-1"], show="$-1$"),
    dict(q=r"已知 $(-2)^5\times(-2)^3=2^a$，$27\times5^3=b^3$，$\left(-\dfrac{3}{5}\right)^2\times\left(-\dfrac{5}{3}\right)^2=15^c$，則 $a+b+c=$", answers=["23"], show="23"),
  ]),
  dict(type="calc", title="三、非選擇題－計算", meta="每題10分，共30分（過程寫在計算紙上，每小題填最後答案）", items=[
    dict(q="有 3 個細胞進行細胞分裂，第 1 次分裂後有 9 個細胞，第 2 次分裂後有 27 個細胞，依此規則不斷分裂，如果分裂過程中所有細胞均不會死亡，則：",
         parts=[dict(p="第 4 次分裂後有多少個細胞？", answers=["243"], show="243 個"),
                dict(p="要分裂幾次後會有超過 500 個細胞？", answers=["5"], show="5 次")]),
    dict(q=r"若 $2^2+2^2+2^2+2^2=2^x$，$3^7\times3^7\times3^7=3^y$，則：",
         parts=[dict(p="$x=$？", answers=["4"], show="4"),
                dict(p=r"$3^y=27^z$，則 $y+z=$？", answers=["28"], show="28")]),
    dict(q=r"$a$、$b$ 皆是大於 1 的整數，且 $a>b$。若 $(a,b)=6$，$[a,b]=2^2\times3^3\times5$，則：",
         parts=[dict(p="若 $b=6$，則 $a$ 值為何？", answers=["540"], show="540"),
                dict(p="若 $a$ 值為三位數，且百位數字為 1，此時 $b$ 值為何？", answers=["30"], show="30")]),
  ]),
  dict(type="fill", title="非選擇題－填充", meta="【B部分 學力精熟題】每格4分，共20分", items=[
    dict(num="1.", q=r"若 $a$、$b$、$c$ 三數滿足 $10^{a-1}=100^b=1000^{c+1}=1000000000000$，則 $a+b+c=$", answers=["22"], show="22"),
    dict(num="2.", q=r"若 $a=2^{60}$，$b=3^{45}$，$c=5^{30}$，則 $a$、$b$、$c$ 的大小關係為", answers=["b>c>a","a<c<b"], show="$b>c>a$", hint="例：a>b>c"),
    dict(num="3.(1)", q=r"已知 $11^3=1331$，則 $110^3=$", answers=["1331000"], show="1331000"),
    dict(num="3.(2)", q=r"承上，$(1.1)^3=$", answers=["1.331"], show="1.331"),
    dict(num="4.", q=r"計算 $\dfrac{(-274)^3}{137^3}\div\dfrac{741^2}{(-247)^2}=$", answers=["-8/9"], show=r"$-\dfrac{8}{9}$", hint=FR),
  ]),
]
