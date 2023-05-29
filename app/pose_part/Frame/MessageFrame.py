from app.pose_part.utils.ToJsonStr import ToJsonStr


class MessageFrame(ToJsonStr):
    msg: str

    def __init__(self):
        super().__init__()
        self.on_error = False  # 任何出错
        self.on_anim = False
