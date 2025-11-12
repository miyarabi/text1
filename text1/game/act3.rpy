# 第三幕：林晓的失落星辰

label act_three:

    # 深夜场景
    scene bg narrative_hall_night with fade
    play music "audio/cello_slow.mp3" fadein 2.0

    show lin at left with dissolve
    show mo at right with dissolve

    # 林晓情绪低落的开场
    show lin sad at left
    "客人们都已离开。林晓没有走，他坐在吧台前，手指无意识地摩挲着苏雨晴送来的那幅画，目光却仿佛没有焦点。"

    mo "你的心，很乱。"

    lin "墨尘，我帮助了雨晴姐，帮助了陈爷爷……可是，我自己的问题，却像雪球一样，越滚越大。"
    show lin determined at left
    lin "我想再看一次。关于'小光'的回忆……完整的回忆。我想知道，那份约定的后半部分，到底是什么。"

    show mo serious at right
    mo "林晓，你确定吗？我曾告诉过你，有些记忆被尘封，是心灵自我保护的本能。那段记忆……我感受到的，是巨大的失落和几乎无法承受的悲伤。重温它，无异于再次撕裂即将愈合的伤口。"

    # 玩家选择
    menu:
        "【坚定请求】":
            jump firm_decision
        "【犹豫退缩】":
            jump hesitate_decision

label hesitate_decision:
    show lin hesitant at left
    lin "……也许你说得对。我可能还没准备好。"
    
    mo "没关系，等待勇气积累，本身也是一种前进。我们随时可以开始。"
    
    "故事暂时停滞在这里，直到林晓鼓起勇气……"
    
    # 等待玩家再次选择
    "几天后……"
    show lin determined at left
    lin "墨尘，我想好了。我必须面对。"
    jump firm_decision

label firm_decision:
    show lin determined at left
    lin "我必须知道。如果连面对的勇气都没有，我永远无法真正前进。我不想再这样迷茫地活下去了。"

    mo "我明白了。那么，这次将由我亲自为你引导。这杯'心语'，将会是最真实，也最苦涩的。"

    # 深潜记忆之海
    show mo making_coffee_blue with dissolve
    "墨尘没有使用常见的咖啡器具，而是取出了一个古朴的陶罐和一个小巧的陶杯。"
    "他研磨咖啡豆的动作缓慢而沉重，仿佛每一次研磨都在调动某种力量。"
    "最终倒入杯中的液体，并非星辰般绚烂，而是如同深夜大海般的深邃墨蓝，几乎不透光。"

    show mo at right with dissolve
    mo "'溯源'。林晓，这一次，没有美好的香气引导你。你需要主动沉入心底最深的海沟，去打捞那颗沉睡的'星辰'。我会在这里，确保你不会迷失。"

    # 饮用咖啡，进入回忆
    play sound "audio/heartbeat_slow.mp3" fadein 1.0
    show memory_deep_blue with dissolve
    "林晓双手捧起陶杯，那重量超乎想象。他闭上眼，如同赴死般，将杯中物一饮而尽。"
    
    stop music fadeout 1.0
    play sound "audio/deep_dive.mp3"
    
    # 深度回忆开始
    jump deep_memory

label deep_memory:
    # 第一部分：阳光与风筝
    scene bg childhood_park_sunny with fade
    play music "audio/music_box_happy.mp3" fadein 2.0
    
    "阳光灿烂，绿草如茵。色彩饱和明亮，如同最美的梦境。"
    
    "小林晓和小光奔跑着，风筝在高空翱翔。小光的笑容比阳光还耀眼。"
    
    young_guang "晓！快看！我们的风筝飞得最高！"
    young_lin "嗯！小光最厉害了！"
    
    young_guang "我们以后也要一起去看更高更远的风景！一起去环游世界！约好了！"
    
    # 第二部分：阴霾初现
    scene bg childhood_park_faded with fade
    play music "audio/music_box_tense.mp3" fadein 2.0
    
    "阳光依旧，但色彩开始微微泛黄、失真，仿佛旧照片开始褪色。"
    "小光的脸色有些苍白，奔跑时偶尔会咳嗽。"
    
    young_lin "小光，你没事吧？脸色好白。"
    young_guang "没事！就是有点感冒！我们的约定，你可别忘了！"
    
    # 第三部分：白色的房间
    scene bg hospital_room with fade
    play music "audio/piano_sad_slow.mp3" fadein 2.0
    
    "画面色调急剧转为冷色，以惨白和淡蓝为主。"
    
    "小林晓趴在病床前。床上的小光戴着氧气面罩，瘦弱得几乎被白色的被子淹没。"
    
    young_lin "小光……你说好要一起去环游世界的……你答应我的……"
    
    young_guang "晓，对不起……我们的约定……我可能……无法一起完成了……"
    
    "小林晓的眼泪大颗滚落，拼命摇头。"
    
    young_guang "别哭……你要……替我去看……那些风景……连同我的那一份……"
    
    "小光的眼神开始涣散，但依旧紧紧盯着小林晓。"
    
    young_guang "要……勇敢地……走下去……一定……"
    
    play sound "audio/heart_monitor_flatline.wav"
    show white_screen with dissolve
    "握住的手，无力地滑落。心电监护仪刺耳的'嘀——'声长鸣响起。"
    
    # 第四部分：灰色的世界
    scene bg park_empty with fade
    play sound "audio/empty_wind.mp3"
    
    "小林晓独自一人站在空荡荡的公园。"
    
    scene bg window_rain with fade
    "小林晓看着窗外的雨，眼神空洞。"
    
    scene bg room_cluttered with fade
    "他把自己锁在房间里，桌上散落着世界地图和旅游画册，却被他用笔胡乱地划掉。"
    
    # 回忆结束，回到现实
    scene bg narrative_hall_night with fade
    play music "audio/cello_comfort.mp3" fadein 2.0
    
    show lin breaking_down at center with dissolve
    "林晓猛地睁开眼，整个人如同虚脱般从高脚凳上滑落，单膝跪在地上，大口地喘息着。"
    "泪水无法抑制地汹涌而出，是压抑了多年的、无声的痛哭。他的肩膀剧烈地颤抖着。"
    
    show mo comforting at right with dissolve
    "墨尘静静地蹲下身，没有阻止他，只是将一只手轻轻放在他的背上，传递着无声的支持。"
    
    lin "他……走了。他让我……替他去看……替他走下去……可我……我弄丢了他的风筝……我把自己困在了那里……"
    lin "我不敢去看，我不敢往前走……因为我怕……怕一个人走的每一步，都会忘记他……"
    
    mo "林晓，看着我的眼睛。"
    
    show lin tearful at left with dissolve
    show mo at right with dissolve
    
    mo "记忆从未消失，爱也是。小光他，从未离开。他只是化作了你心中的一颗星辰。"
    "墨尘的手指向林晓的心脏位置。"
    
    mo "他一直在这里，为你指引方向。你的迷茫，不是因为失去了他，而是因为你误解了约定的意义。"
    mo "他最后的愿望，不是要你背负着悲伤和愧疚前行，而是希望你能'勇敢'、'快乐'地走下去，去体验他未能体验的人生。"
    mo "你停滞不前的每一步，才是对他最大的遗忘。"
    
    show lin realization at left
    "林晓的哭声渐渐止住，墨尘的话语如同惊雷，在他心中炸响。"
    
    lin "（内心独白）……我误解了？他不是要我记住悲伤，而是要我带着他的祝福，去活得精彩？"
    "他脑海中再次浮现小光最后的笑容，那笑容里，没有对死亡的恐惧，只有对他的期盼和祝福。"
    
    show lin determined at left
    "林晓缓缓站起身，擦干眼泪。虽然眼睛红肿，但他的眼神不再迷茫，而是充满了某种释然和前所未有的坚定。"
    
    lin "我……明白了。"
    lin "小光希望看到的，是一个勇敢、快乐的林晓。他是我心中的星辰，不是枷锁……我不能……再让他失望了。"
    
    show lin bowing at center with dissolve
    "他转向墨尘，深深地鞠了一躬。"
    
    lin "谢谢你，墨尘。谢谢你……让我找回了这颗最重要的星辰。"
    
    show mo warm_smile at right
    mo "欢迎回来，林晓。"
    
    # 黎明将至的结尾
    scene bg dawn_breaking with fade
    play music "audio/hopeful_ending.mp3" fadein 3.0
    
    "窗外，黎明将至，最深沉的黑暗正在褪去。"
    
label act3_end:
    # 第三幕结束转场
    show text "{size=36}第三幕 结束{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    
    # 幕间转场 - 情感化的效果
    scene black with Fade(2.0, 0.0, 2.0)  # 缓慢的淡出淡入
    
    # 显示幕间标题
    show text "{size=48}心语叙事馆{/size}\n{size=36}最终幕：新的篇章与心的传承{/size}" at truecenter with dissolve
    pause 3.0
    hide text with dissolve
    
    # 跳转到第四幕
    jump act_four