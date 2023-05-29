from app.pose_part.MessageFrame import MessageFrame


class AnimData:
    anim_pose: dict  # TODO
    anim_sequ: int
    anim_sec: float
    
    def json_dict(self):
        D = self.__dict__
        return D


class AnimFrame(MessageFrame):
    anim_data: AnimData
    anim_cancelled: bool
    
    def __init__(self):
        super().__init__()
        self.on_anim = True
        self.on_end = False

    def json_dict(self):  # 自定义魔法方法
        D = self.__dict__
        
        for k in D:
            if isinstance(D[k], AnimData):
                D[k] = D[k].json_dict()
                
        return D


def anim_end(is_cancel: bool):
    am = AnimFrame()
    am.on_end = True
    am.anim_cancelled = is_cancel
    return am.json_str()


def anim_pose(pose_obj, seq_num: int, anim_sec: float):
    data = AnimData()
    data.anim_pose = pose_obj
    data.anim_sequ = seq_num
    data.anim_sec = anim_sec
    
    am = AnimFrame()
    am.anim_data = data
    return am.json_str()
