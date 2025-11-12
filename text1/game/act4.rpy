# 第四幕：新的篇章与心的传承

label act_four:

    # 开场 - 与第一幕呼应的雨夜
    scene bg narrative_hall_rain with fade
    play music "audio/piano_rain_theme.mp3" fadein 3.0
    play sound "audio/rain_steady.wav" fadein 1.0

    show lin mature at left with dissolve
    show mo at right with dissolve

    "数月后的一个雨夜，场景与第一幕开场惊人地相似。"
    "但馆内温暖明亮的灯光，此刻更像一个坚定存在的港湾，而非偶然的奇迹。"

    show lin looking_out at left
    "林晓站在窗边，望着窗外的雨景。他的身影依旧清瘦，但站姿却挺拔而稳定。"
    "他手中拿着的，是那张和小光一起放风筝的旧照片，但他的嘴角带着一丝温柔的弧度。"

    lin "（内心独白）同样的雨，同样迷茫的夜晚……但这一次，我的心境却完全不同了。小光，你看到了吗？我没有停留在原地。"

    show mo approving at right
    "墨尘在吧台后，看着林晓的背影，眼中是毫不掩饰的赞许与欣慰。"

    mo "（轻声地）星辰一旦被擦亮，便会自己发光了。"

    # 新客人到来
    play sound "audio/doorbell.wav"
    "*叮铃——*"

    show a_zhe confused at center with moveinbottom
    "门被有些迟疑地推开。一位年轻男子站在门口，约莫二十岁出头，浑身湿透，头发凌乱，脸上写满了疲惫、焦虑与一丝不知所措。"

    a_zhe "请问……这里还营业吗？"

    show lin mature at left
    show mo at right
    "林晓与墨尘对视一眼，墨尘微微颔首，给予了默许和鼓励。"

    show lin welcoming at left
    "林晓转过身，脸上浮现出墨尘初次见他时那种温和、但如今更加沉稳且充满理解的笑容。他主动迎了上去。"

    lin "营业。欢迎光临'心语叙事馆'。"
    lin "外面雨很大吧？请进来避避雨，暖和一下。"

    "阿哲有些拘谨地走进来，手足无措地站在门口，水滴从他身上落下。"

    a_zhe "我……我会弄湿地板的……"

    lin "没关系，座椅的存在，就是为了承载疲惫的旅人。湿气总会干的。"
    "他引导阿哲在靠近吧台的座位坐下，那是他曾经坐过的位置。"

    "墨尘默契地递上一杯温水给林晓，由林晓转交给阿哲。"

    a_zhe "谢谢……"

    lin "需要喝点什么吗？或许，一杯热咖啡能让你感觉好一些。"

    a_zhe "随便吧……什么都行。我只是……只是想找个地方待一会儿。"

    # 玩家选择 - 体现林晓的成长
    menu:
        "【推荐特调】":
            lin "或许，你可以试试本店的'特调'？它没有固定的味道，但能帮你找到你真正需要的东西。"
            jump continue_guidance
            
        "【温和引导】":
            lin "看起来你遇到了些麻烦。如果你愿意，可以聊聊。有时候，说出来会好受很多。"
            
            a_zhe "（苦笑着摇摇头）聊……也不知道从何说起。就是觉得……一切都糟透了，找不到方向。"
            
            lin "我明白那种感觉。那么，或许一杯'特调'更适合现在的你。"

label continue_guidance:
    lin "墨尘，麻烦你了。"

    show mo making_coffee with dissolve
    "墨尘微笑着开始准备。但这一次，他的动作更像是一种仪式性的授权。"
    "他将研磨好的咖啡粉交给林晓，由林晓进行后续的冲煮步骤。"
    "林晓的动作虽不如墨尘那般行云流水，却异常认真和专注。"

    show lin making_coffee at left with dissolve
    "最终，一杯呈现出温暖琥珀色、仿佛内里蕴藏着光晕的'特调'由林晓亲手放在了阿哲面前。"

    show lin guiding at left
    show mo at right
    lin "请用。当咖啡的香气环绕你时，不妨闭上眼，倾听自己内心最真实的声音。它会指引你。"

    show a_zhe thinking at center
    "阿哲看着这杯充满善意的咖啡，又看了看林晓真诚的眼睛，最终迟疑地闭上了眼，端起了杯子。"

    play sound "audio/memory_glow_soft.mp3"
    "在林晓的引导下，阿哲仿佛也进入了一段短暂的内心平静。"

    show a_zhe relaxed at center
    "片刻后，阿哲睁开眼，虽然迷茫未完全散去，但紧绷的神情舒缓了许多，他长长地舒了一口气。"

    a_zhe "感觉……好像没那么压抑了。谢谢你们。"

    "林晓只是微笑着点了点头。"
    "阿哲静静地坐在那里，开始小口地喝着咖啡，望着窗外的雨景，陷入了自己的思绪，但不再是完全的绝望。"

    show lin mature at left
    show mo at right
    "林晓退回到墨尘身边。"

    mo "你做得很好。"

    lin "因为我也曾被这样温柔地接住过。"

    # 结尾定格画面
    scene bg narrative_hall_rain with fade
    show mo at right
    show lin mature at left
    show a_zhe relaxed at center
    
    "镜头缓缓拉远，定格在这一幕：温暖的咖啡馆内，墨尘和林晓并肩站在吧台后，如同两位守护者；"
    "而一位新的迷途者，正在这里暂时停靠，寻找内心的答案。"

    # 画面淡出，进入结尾CG蒙太奇
    scene black with fade
    stop sound fadeout 2.0
    play music "audio/hopeful_ending_full.mp3" fadein 3.0

    # 结尾CG蒙太奇
    show cg su_painting_studio with dissolve
    "苏雨晴在洒满阳光的画室里，画笔挥洒，画板上是绚烂的色彩，她的脸上洋溢着创造的热情。"
    pause 2.0

    show cg grandpa_chen_park with dissolve
    "陈爷爷坐在公园的长椅上，膝上放着妻子的照片，他正微笑着对空中飞过的小鸟说着什么，神情安详而满足。"
    pause 2.0

    show cg lin_future with dissolve
    "林晓站在'心语叙事馆'的窗前，眼神明亮而坚定地望着远方。"
    "他的书桌上，放着一本打开的旅行计划册和一张世界地图，几个地点被清晰地标记出来。"
    "地图的一侧，小光的照片静静躺着。"
    pause 2.0

    # 最终定格画面
    show cg narrative_hall_final with dissolve
    "最终画面定格在心语叙事馆的全景，它静静地坐落在城市角落，"
    "招牌上的星辰徽记，散发着柔和而永恒的光芒。"
    pause 2.0

    # 结尾字幕
    scene black with fade
    show text "{size=36}{color=#ffffff}每一段心语，都是一颗独特的星辰。{/color}{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve

    show text "{size=36}{color=#ffffff}每一次倾听，都是一次温柔的点亮。{/color}{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve

    show text "{size=32}{color=#ffffff}或许我们都会迷路，{/color}{/size}" at truecenter with dissolve
    pause 1.5
    hide text with dissolve

    show text "{size=32}{color=#ffffff}但请相信，{/color}{/size}" at truecenter with dissolve
    pause 1.5
    hide text with dissolve

    show text "{size=36}{color=#ffffff}总有一处灯火，为你而明。{/color}{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve

    show text "{size=28}{color=#ffffff}心语叙事馆——{/color}{/size}" at truecenter with dissolve
    pause 1.5
    hide text with dissolve

    show text "{size=32}{color=#ffffff}愿你在此，找到属于自己的星辰大海。{/color}{/size}" at truecenter with dissolve
    pause 3.0
    hide text with dissolve

    # 全剧终
    show text "{size=48}{color=#ffffff}全剧终{/color}{/size}" at truecenter with dissolve
    pause 3.0

    stop music fadeout 5.0
    return