from app.pose_part.Frame.AnimData import AnimData
from app.pose_part.Frame.MessageFrame import MessageFrame
from app.pose_part.Frame.PoseData import PoseData


class AnimFrame(MessageFrame):
    anim_data: AnimData
    anim_cancelled: bool
    
    def __init__(self):
        super().__init__()
        self.on_anim = True
        self.on_end = False


def anim_pose(pose_data: PoseData, seq_num: int, anim_sec: float):
    data = AnimData()
    data.anim_pose = pose_data
    data.anim_sequ = seq_num
    data.anim_sec = anim_sec

    am = AnimFrame()
    am.anim_data = data
    return am.json_str()


def anim_end():
    am = AnimFrame()
    am.on_end = True
    return am.json_str()


def anim_cancelled(msg: str = None):
    am = AnimFrame()
    am.on_end = True
    am.anim_cancelled = True
    if msg:
        am.msg = msg

    return am.json_str()
