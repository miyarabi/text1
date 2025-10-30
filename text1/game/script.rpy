define memory_fade = Fade(1.0, 0.0, 1.0, color="#000000")
define dream_dissolve = Dissolve(3.0)
define dream_fade = Fade(1.0, 0.5, 1.0)  # 渐暗-暂停-渐明

init python:
    def scene_transition(transition_type="fade", duration=1.0):
        """幕间转场效果"""
        if transition_type == "fade":
            return Fade(duration, 0.5, duration)
        elif transition_type == "dissolve":
            return Dissolve(duration)
        elif transition_type == "pixellate":
            return Pixellate(duration)
        elif transition_type == "wipe":
            return WipeRight(duration)
        elif transition_type == "blinds":
            return Blinds(10, duration)
        
    def memory_transition():
        """回忆专用转场"""
        return Fade(0.5, 0.3, 0.5)

# 游戏从这里开始
label start:
    # 跳转到第一幕
    jump act_one