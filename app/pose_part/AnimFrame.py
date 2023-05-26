from app.pose_part.MessageFrame import MessageFrame


class AnimFrame(MessageFrame):
    anim_pose: dict  # TODO
    anim_sequ: int
    anim_sec: float
    anim_cancelled: bool

    def __init__(self):
        super().__init__()
        self.on_anim = True
        self.on_begin = False
        self.on_end = False

    def json_str(self):
        return super().json_str()


def anim_begin():
    am = AnimFrame()
    am.on_begin = True
    return am.json_str()


def anim_end(is_cancel: bool):
    am = AnimFrame()
    am.on_end = True
    am.anim_cancelled = is_cancel
    return am.json_str()


def anim_pose(pose_obj, seq_num: int, anim_sec: float):
    am = AnimFrame()
    am.anim_pose = pose_obj
    am.anim_sequ = seq_num
    am.anim_sec = anim_sec
    return am.json_str()
