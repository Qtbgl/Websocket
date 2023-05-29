from numpy import ndarray

from app.pose_part.utils.ToJsonStr import ToJsonStr


class PoseData(ToJsonStr):
    def __init__(self):
        self.upperarm_l = UEQuat()   # 所有关节的旋转，都有初始值
        self.upperarm_r = UEQuat()
        self.lowerarm_l = UEQuat()
        self.lowerarm_r = UEQuat()


class UEQuat(ToJsonStr):
    def __init__(self, arr: ndarray = None):  # scipy.spatial.transform.Rotation
        if arr is None:
            self.x = 0
            self.y = 0
            self.z = 0
            self.w = 0
        elif arr.shape == (3,):
            self.x = arr[0]
            self.y = arr[1]
            self.z = arr[2]
        else:
            raise TypeError
