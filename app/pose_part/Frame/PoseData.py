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
        elif arr.shape == (4,):
            self.x = float(arr[0])  # debug
            self.y = float(arr[1])
            self.z = float(arr[2])
            self.w = float(arr[3])
        else:
            raise TypeError("UEQuat 构造异常，输入维度问题：", arr.shape)
