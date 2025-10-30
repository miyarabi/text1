# 第二幕开始
label act_two:

    scene bg narrative_hall_day with fade
    play music piano fadein 2.0

    show lin at left with dissolve
    show mo at right with dissolve

    lin "墨尘，那天之后……我一直在想。来到这里的人，是不是都和我一样，心里藏着一些无处安放的东西？"

    mo "每个人都是一本厚重的书，有些章节被反复翻阅，有些则被轻轻合上，等待一个合适的时机再次打开。而我们这里，就是那个‘时机’常常降临的地方。"

    play sound "doorbell.wav"
    "*叮铃*"

    # 章节A：苏雨晴
    show su anxious at center with moveinbottom

    su "请问……你就是墨尘先生吗？我的朋友说，你这里……能帮人找到‘丢失的东西’？"

    mo "我是墨尘。我们尽力帮助客人寻找他们内心真正渴望的事物。这位是林晓，我的助手。"

    lin "你好。"

    su "我丢失了我的颜色！我是一个插画师，可是最近……我什么都画不出来了！我的世界，我的画板，全都变成了灰色！截稿日就要到了，我……"

    mo "慢慢说。灰色……是从什么时候开始的？"

    su "不知道……可能就是最近几个月。工作压力越来越大，甲方的要求反反复复……我好像……忘记了自己当初为什么要画画了。"

    mo "林晓，你觉得呢？"

    menu:
        "【温和鼓励】":
            lin "别着急，慢慢来。或许你只是需要暂时放松一下。"
        "【理性分析】":
            lin "是不是最近太累了？休息一下可能会好点。"

    mo "或许，你需要找回的并非‘颜色’，而是你第一次看见‘颜色’时的那份心动。"

    # 林晓递咖啡豆（默契动作）
    lin "（将研磨好的咖啡豆递给墨尘）"

    mo "请给我们一点时间。这杯咖啡，或许能带你回到色彩的源头。"

    # 调制咖啡过程（可加动画或图片）
    show mo making_coffee with dissolve
    mo "‘初心’。请闭上眼睛，感受它。"
    show mo at right with dissolve

    play sound memory_glow
    show memory_glow with dissolve
    pause 1.0

    # 回忆片段：彩虹
    scene bg childhood_window with fade
    play music rainbow_music fadein 1.0
    play sound rain_sound
    play sound bird_sound

    narrator "窗外是刚下过雨的、湿漉漉的世界，天空还是灰蒙蒙的。突然，一弯绚烂的彩虹毫无征兆地出现在天际……"

    narrator "小女孩（苏雨晴）发出“哇”的一声惊叹。一只肉乎乎的小手伸出来，隔着玻璃，努力想去触摸那道彩虹。"

    su "（内心，稚嫩）好漂亮……好像能把所有不开心都赶走……"

    narrator "她拿起一支蜡笔，在窗户的雾气上，笨拙又认真地画下了那道彩虹的轮廓。"

    su "（画外音，哽咽）我想起来了……不是技巧，不是合同，也不是别人的评价……只是……只是因为它很美，我想把它画下来，让所有人都看到这份美丽……"

    # 回到现实
    scene bg narrative_hall_day with fade
    play music piano fadein 1.0
    show su inspired at center with dissolve

    su "我想起来了……是彩虹！是我五岁时看到的那道彩虹！谢谢你们！我知道该怎么画了！我知道我的颜色在哪里了！"

    hide su with moveoutright

    lin "她……好像整个人都在发光。"

    mo "因为她找回了属于自己的星辰。看，林晓，你已经能帮助别人了。"

    # 几天后收到插画
    show cg su_painting with dissolve
    narrator "几天后，林晓收到一幅插画。画的是“心语叙事馆”的夜景，雨丝被画成了七彩的线条。"
    narrator "右下角写着：致叙事馆与两位引路人——雨晴。"

    hide cg su_painting with dissolve

    lin "（内心）帮助别人找到光芒……这种感觉，似乎也不坏。"

    # 章节B：陈爷爷
    show chen kind at center with moveinbottom

    chen "请问……这里就是‘心语叙事馆’吗？老街坊说，这里能帮人……记住想记住的事。"

    mo "老先生，您请坐。林晓。"

    # 林晓搬椅子（动作提示）
    lin "（搬来扶手椅）"

    chen "谢谢你们……我老了，脑子不中用了。很多事，就像旧照片褪了色，模糊了。"

    chen "（拿出照片）这是我老伴，秀娟。我……我怕连和她第一次见面的样子都忘了……"

    chen "没有了这些细节，我连梦，都做不完整了……"

    lin "（内心）想要紧紧抓住最珍贵的回忆……这种感觉……"

    mo "遗忘并不可怕，老先生。可怕的是我们放弃了追寻。林晓，这次需要你和我一起。这段记忆年代久远，需要更稳定的‘锚点’。"

    lin "（点头）"

    mo "‘初见’。请握住您妻子的照片，老先生。林晓，请你将手放在老先生的手背上。"

    play sound memory_glow
    show memory_glow with dissolve
    pause 1.0

    # 在 act2.rpy 中的陈爷爷回忆部分
label grandpa_memory:
    # 回忆开始转场
    scene black with memory_fade
    
    # 回忆片段：栀子花下的相遇
    scene bg old_courtyard with fade
    play music violin fadein 1.0
    play sound cicada_sound

    "画面是柔和的黑白怀旧色调，唯有两个元素是鲜活的彩色：栀子花树，和穿着淡蓝色碎花旗袍的秀娟。"

    "年轻的陈文有些紧张地站在院子门口。秀娟抬起头，看到他，先是一愣，随即低下头，嘴角弯起好看的弧度。"

    "少女的声音清脆，带着笑意。"
    "'你是……隔壁新搬来的陈先生？我父亲等你很久了。'"

    "陈文有些笨拙地回应。"
    "'啊，是、是的。这花……真香。'"

    "'你喜欢栀子花？'少女的笑意更深了。"

    "一阵风吹过，几片花瓣落下。陈文下意识地伸手，接住一片，然后鼓起勇气，上前一步，轻轻地将那片花瓣别在秀娟的发间。"

    "秀娟惊讶地睁大眼睛，随即脸上的红晕更深了，她没有躲闪，只是眼波温柔地流转。"

    "陈文轻声说道，声音里满是真诚。"
    "'人比花娇。'"

    "没有更多的言语，但那一刻的心动，穿越了半个多世纪的时光，清晰地传递过来。"

    # 回忆结束转场,回到现实
    scene black with dissolve
    scene bg narrative_hall_day with fade
    play music piano fadein 1.0
    show chen kind at center with dissolve

    chen "看见了……我看得清清楚楚！她穿的是淡蓝色的碎花旗袍，领子上绣着小小的茉莉……她笑了，右边脸上有个浅浅的梨涡……她先对我说的话……谢谢！谢谢你们！"

    chen "（对墨尘）我这辈子，值了。"

    chen "（对林晓）年轻人，要珍惜啊……能在一起的时光，都是老天爷的礼物。"

    hide chen with moveoutleft

    lin "（望着门口）"

    mo "感受到了吗？"

    lin "（声音沙哑）嗯……那么沉重，又那么温暖。这就是……爱的重量吗？"

    lin "（内心）和小光在一起的时光……也是我的礼物。可我好像……一直在逃避去正视它。"

label act2_end:
    # 第二幕结束转场
    show text "{size=36}第二幕 结束{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    
    # 幕间转场 - 使用不同的效果
    scene black with Fade(1.0, 0.5, 1.0)
    
    # 显示幕间标题
    show text "{size=48}心语叙事馆{/size}\n{size=36}第三幕：林晓的失落星辰{/size}" at truecenter with dissolve
    pause 3.0
    hide text with dissolve
    
    # 跳转到第三幕
    jump act_three