# 第一幕：迷途的邂逅
label act_one:

    # 场景1：迷途的街道
    scene bg rainy_street
    play music rain_piano fadein 2.0
    play sound rain_ambient loop

    "傍晚时分。都市的街道被淅淅沥沥的秋雨笼罩。路灯的光芒在湿漉漉的柏油路上晕染开，形成模糊而冰冷的光斑。行人神色匆匆，撑着黑色的雨伞，如同无声流动的剪影。"

    show lin back at center with dissolve

    lin "（……又失败了。）"
    lin "（第几次了？'很遗憾，您的经历与我们岗位不符'……这些打印出来的铅字，比这雨水还冷。）"
    lin "（回家吗？回到那个安静得只能听见时钟滴答声的房间……）"

    "林晓停下脚步，站在一个红绿灯前。红灯的数字一下下跳动，映在他有些空洞的眼睛里。"

    lin "（未来……到底该往哪里走？）"

    "绿灯亮起，周围的人流迅速穿过马路。林晓却迟疑着，没有动。他下意识地转向了那条平时不会走的、更幽静的岔路。"

    # 场景2：温暖的邂逅
    scene bg narrative_hall with fade
    stop music fadeout 2.0
    play music warm_theme fadein 2.0
    stop sound fadeout 1.0

    "岔路的尽头，暖黄色的光芒如同一颗落入凡间的星辰，驱散了周围的阴冷。'心语叙事馆'的木质招牌清晰起来。招牌上的藤蔓雕刻细腻，那颗星辰的中心，似乎有微光在缓缓流动。"

    lin "（……这家店？）"
    lin "（什么时候开的？昨天这里……好像还是一面空白的墙？）"
    lin "（但是……这光……让人忍不住想靠近。）"

    "林晓伸出手，轻轻触碰那扇有着复古花纹的玻璃木门。门把手是冰凉的黄铜，却奇异地不让人觉得寒冷。"

    play sound door_bell
    "清脆悦耳的'叮铃——'声，是门铃的声音。"

    # 场景3：叙事馆的内景
    scene bg inside_shop with fade
    play music shop_bgm fadein 2.0

    "温暖的光线瞬间包裹了他。巨大的落地书架占据整面墙，塞满了各种颜色和厚度的书籍。几张舒适的沙发和茶几散落在各处，上面放着柔软的抱枕。空气中仿佛能看到细微的光尘在舞动。"

    show mo normal at right with dissolve
    show lin front at left with dissolve

    mo "欢迎光临。外面的雨似乎没有停歇的意思呢。请不用拘束，找个喜欢的位置坐下吧。"

    "墨尘站在吧台后，正用一块白色的软布，细致地擦拭着一个陶瓷咖啡杯。他闻声抬起头。"

    lin "……会弄湿座位。"

    mo "座椅的存在，就是为了承载疲惫的旅人。湿气总会干的，请别在意。"

    "林晓犹豫了一下，最终还是选择在吧台前的高脚凳上坐下。"

    mo "需要喝点什么，驱散身上的寒意吗？"

    lin "请给我一杯热美式。谢谢。"

    mo "热美式……纯粹的苦涩，有时确实能提神。但今晚，它或许无法温暖你真正需要温暖的地方。"

    lin "……什么意思？"

    mo "或许，你可以尝试一下本店的'特调'。"

    # 第一个选项
    menu:
        "【好奇地询问】'特调？是什么样的咖啡？'":
            jump ask_about_special
        "【保持距离】'不用了，我还是习惯美式。'":
            jump refuse_special

label refuse_special:
    mo "好的，尊重您的习惯。一杯热美式，请稍等。"
    "墨尘转身制作美式。林晓喝完咖啡后，支付离开。"
    "【您未能推开那扇门，故事尚未开始……】"
    return

label ask_about_special:
    lin "特调？是什么样的咖啡？"

    mo "它没有固定的名字，也没有固定的配方。它会倾听客人的'心音'，呈现出独一无二的风味。有时是回忆里的甜，有时是释然后的醇，有时……是解开谜题的钥匙。"

    "墨尘的目光似乎无意地扫过林晓紧锁的眉头。"

    mo "也许，它能帮你找到……你此刻正在寻找的东西。"

    # 第二个选项
    menu:
        "【接受邀请】'听起来很神奇……好吧，请给我一杯特调。'":
            jump accept_special
        "【再次婉拒】'还是算了，听起来不太靠谱。'":
            jump refuse_again

label refuse_again:
    "林晓选择了婉拒，故事未能继续。"
    "【您未能推开那扇门，故事尚未开始……】"
    return

label accept_special:
    lin "……好吧。麻烦您了，请给我一杯'特调'。"

    mo "明智的选择。"

    # 场景4：星辰咖啡的诞生
    show closeup_hand with dissolve
    play sound coffee_brew

    "墨尘的手部特写。他的手指修长而稳定，操作行云流水。取豆、研磨、闷蒸……每一个步骤都像是一种仪式。"

    show closeup_coffee with dissolve

    "当他将热水注入时，氤氲的蒸汽仿佛带着微光。最后，他将咖啡液倒入一个预冷的玻璃杯中，杯中底层是深蓝色的糖浆，如同夜空。咖啡液与糖浆交融，形成了美丽的星云漩涡，最后，墨尘用一根细签蘸取奶油，在表面点缀上几个小小的白色光点，宛如星辰 "

    "他将完成的'特调'放在林晓面前。那杯咖啡，就像一个小小的、独立的宇宙。"

    mo "请用。当咖啡的香气拥抱你时，不妨闭上眼……暂时放下思考，只是去'感受'。你内心最深处的回响，会指引你。"

    "林晓看着这杯不可思议的咖啡，犹豫了一下，然后双手捧起杯子。温度透过杯壁，温暖了他冰凉的手指。他闭上眼，轻轻啜饮了一口。"

play sound heartbeat

# 使用自定义的渐暗渐明效果
scene black with dream_fade

"在嘴唇接触杯沿的瞬间，所有声音骤然停止，变为一种空灵的、心跳放大的'嗡——'声。"

# 从黑色渐亮到白色
scene white with Fade(0.5, 0, 1.0)

"眼前泛起柔和的、水波状的白色光晕，所有景物变得模糊……"

label act1_end:
    # 第一幕结束转场
    show text "{size=36}第一幕 结束{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    
    # 幕间转场
    scene black with Fade(1.0, 0.5, 1.0)
    
    # 显示幕间标题
    show text "{size=48}心语叙事馆{/size}\n{size=36}第二幕：客人们的心之星辰{/size}" at truecenter with dissolve
    pause 3.0
    hide text with dissolve
    
    # 跳转到第二幕
    jump act_two