META = dict(n=9, h1="第9回・Unit 5", subtitle="How Do We Go to the Hotel?")
SECTIONS = [
  dict(type="vocab", title="一、文意字彙", meta="【A部分 基礎題】8分，每題1分", items=[
    dict(q="Rhonda has a big p___l behind her house. She can go for a swim at any time.", answer="pool"),
    dict(q="A: Can you ride a m___e? B: No, but I can drive.", answer="motorcycle"),
    dict(q="A: Is Amy the girl with short st___t hair? B: No. She's the one with long curly（捲的）hair.", answer="straight"),
    dict(q="A: Where do you want me to put the box? B: Just put it on the g___d next to the tree. Thanks.", answer="ground"),
    dict(q="This robot is not a t___y, so you can't play with it.", answer="toy"),
    dict(q="The sound of the church b___l was beautiful, so we stood and listened for a few minutes.", answer="bell"),
    dict(q="A: Do you have any work e___e? B: Yes. I worked at a coffee shop before.", answer="experience"),
    dict(q="A: Grandpa can't walk. What happened? B: He fell from the tree and broke both f___t.", answer="feet"),
  ]),
  dict(type="mc", title="二、文法選擇", meta="18分，每題2分", items=[
    dict(q="Tom always ___ home, but he ___ a taxi today.", options=["gets; took","gets; used","walks; took","walks; used"], correct=2),
    dict(q="The weather is nice. Let's go ___ by the lake.", options=["picnics","picnicked","to picnic","picnicking"], correct=3),
    dict(q="You're new to this job. Don't be scared to ___ help.", options=["get to","go up","ask for","go along"], correct=2),
    dict(q="Felicia usually goes ___ at the park on weekends.", options=["jog","jogs","jogging","jogged"], correct=2),
    dict(q="A: Why don't we go to JJ Island by ___? B: Great idea!", options=["boat","boats","a boat","the boat"], correct=0),
    dict(q="A: ___ did you go to the beach? B: By train.", options=["Why","How","When","Which"], correct=1),
    dict(q="A: Did you ___ a scooter to the concert? B: No, I didn't. My friend ___ me.", options=["take; rode","ride; gave","take; made","ride; drove"], correct=3),
    dict(q="We didn't have enough money for a taxi, so we took ___ metro.", options=["×","by","the","one"], correct=2),
    dict(q="A: ___ can I get to the bus stop from here? B: Just go straight and turn right on Becker Street. It's right in front of a bank.", options=["How","Why","What","Where"], correct=0),
  ]),
  dict(type="mc", title="三、對話選擇", meta="4分，每題2分", items=[
    dict(q="A: Do you like water sports? B: ___", options=["Yes. I often go bird watching.","No, but I love to go swimming.","Yes. I like to go surfing or sailing.","No. I never go biking in my free time."], correct=2),
    dict(q="A: ___ B: No. It's in another city. We can drive there.", options=["Can we walk to Green Park?","Can you take me to Green Park?","Can we go to Green Park by car?","Can we go camping at Green Park?"], correct=0),
  ]),
  dict(type="guided-multi", title="四、看圖完成填空", meta="22分，每格2分・依地圖回答（①Hank ②Cindy ③Wade ④Becky 為各人所在位置）", image="images/test9/sec4_map.png", items=[
    dict(zh="", lines=["Hank: Is the bookstore far（遠的）from here?","Man: No. It's only a ten-minute walk. Just walk {{along}} Sun Street for two {{blocks}}, and you can see it."]),
    dict(zh="", lines=["Cindy: {{Excuse}} me, sir. I'm looking for the department store.","Woman: Go down Moon Street, turn right on Second Road, and then turn {{left}} on Sun Street. It's on the {{corner}} {{of}} Sun Street and First Road."]),
    dict(zh="", lines=["Wade: {{How}} do I get to the {{bank}}?","Man: Go down Second Road {{for}} one block and turn left on Sun Street. Take a right on First Road. It's next to a bookstore."]),
    dict(zh="", lines=["Becky: Where is the {{supermarket}}?","Woman: Just go straight for one block and turn right on First Road. It's {{on}} the left."]),
  ]),
  dict(type="guided", title="五、依提示作答", meta="4分，每題2分", items=[
    dict(prompt="Is the fire station next to the post office?", hint="（用「在對面」否定詳答）", answer="No, it's not. It's across from the post office."),
    dict(prompt="They walked to the hospital.", hint="（用foot改寫）", answer="They went to the hospital on foot."),
  ]),
  dict(type="translation", title="六、整句式翻譯", meta="6分，每題3分", items=[
    dict(zh="我們在山裡健行，度過了一個美好的時光。（... and had a...）", answer="We went hiking in the mountains and had a wonderful / great / good time."),
    dict(zh="Vincent 昨天迷路了，因為他沒有一張這座城市的地圖。", answer="Vincent was lost yesterday because he didn't have a map of this city."),
  ]),
  dict(type="mc", title="一、單題", meta="【B部分 活用題】14分，每題2分", items=[
    dict(q="Look at the picture. What did Josh do this morning?", image="images/test9/b1_bike.png", options=["He went biking.","He went surfing.","He went jogging.","He went mountain climbing."], correct=0),
    dict(q="A: Can I take the metro to Shilin Night Market? B: Yes. ___ Jiantan Station. The night market is very close to that station.", options=["Walk to","Get off at","Go around","Drive along"], correct=1),
    dict(q="After dinner, Ian and Deborah took a long walk along the river ___.", options=["bank","block","ground","corner"], correct=0),
    dict(q="A: Please ___ a left turn here, and park（停車）in front of the bookstore. B: Yes, sir.", options=["get","make","turn","have"], correct=1),
    dict(q="A: You're late. Didn't you catch the first bus? B: I did, but not long after I ___ the bus, it broke down（拋錨）. Then everyone got off and waited for the next bus. A: Poor you.", options=["got on","took off","turned on","turned into"], correct=0),
    dict(q="Helen went to the department store but didn't plan to buy anything; she went window ___.", options=["sailing","cleaning","watching","shopping"], correct=3),
    dict(q="A: Did Marie take a ship to India? B: No. She ___ there. Her uncle picked her up（接）at the airport.", options=["rode","took","flew","drove"], correct=2),
  ]),
  dict(type="reading", title="二、依短文或圖表選出適當的答案", meta="18分，每題3分", passages=[
    dict(label="【A】", text="Sue: Excuse me. How can I get to Mayo Hospital?\nJim: Go down Beach Road for two blocks and then turn left on Main Street. Go down Main Street for one block; there is a bank on the corner. The hospital is next to the bank.\nSue: Is there a flower shop on the way?\nJim: Yes. There is one on Beach Road. It's between the police station and the bookstore.\nSue: Thank you very much!\nJim: You're welcome. Have a good day.", image="images/test9/b2_map.png",
      items=[
        dict(q="Which is Mayo Hospital?", options=["B.","C.","D.","E."], correct=2),
        dict(q="Which is the flower shop?", options=["A.","C.","F.","G."], correct=1),
        dict(q="Sue is on her way to the hospital. What do we know about her?", options=["She may take the metro to the hospital.","She may walk past Moon Hotel on the way there.","She may stop by the flower shop next to the bookstore.","She can get something from the department store on the way."], correct=2),
        dict(q="Look at the map. Which is NOT true（真實的）?", options=["There is a bus stop in front of the movie theater.","The temple is between the park and the department store.","You can get food from at least（至少）two places on Happy Street.","The metro station is on the corner of Church Road and Park Street."], correct=1),
      ]),
    dict(label="【B】", text="", image="images/test9/b2_ad.png",
      items=[
        dict(q="What is Four Seasons?", options=["A hotel.","A restaurant.","A movie theater.","A swimming pool."], correct=0),
        dict(q="What do we know about Four Seasons?", options=["It's right next to a beautiful beach.","You can go swimming when you are there.","There aren't any restaurants near Four Seasons.","It is on the corner of Green Street and Beach Road."], correct=1),
      ]),
  ]),
  dict(type="cloze", title="三、克漏字選擇", meta="6分，每題2分",
    passage="Elijah: Are you ready to go, Rose?\nRose: I need about ten minutes.\nElijah: It's seven now. The movie is at 7:45.\nRose: Take it easy. ___1___ The movie theater is not that far.\nElijah: It's not far, but there aren't many parking spaces around there.\nRose: You're right. Let's ___2___ Bus 301 then. The bus ride is 15 minutes.\nElijah: But we always wait so long for the bus.\nRose: All right. Let's go ___3___ taxi.\nElijah: Well, that's the only way. It's 7:15 now.\nRose: I'm sorry. Taxi's on me. Let's go.\n\n【字詞】far 遠的　parking space 停車位",
    items=[
      dict(options=["We can walk there.","It's just a ten-minute drive.","The metro ride is about ten minutes.","Taking the train is also fine with me."], correct=1),
      dict(options=["do","get","take","make"], correct=2),
      dict(options=["at","on","in","by"], correct=3),
  ]),
]
