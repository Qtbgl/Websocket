from app.pose_part.Frame.PoseData import PoseData
from app.pose_part.utils.ToJsonStr import ToJsonStr


class AnimData(ToJsonStr):
    anim_pose: PoseData
    anim_sequ: int
    anim_sec: float
