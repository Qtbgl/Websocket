import numpy as np

from app.pose_part.solve.BodyPoint import BodyPoint
from app.pose_part.solve.vector_sci import from2vector


class BoneRotate:
    _thigh_l_v1 = np.array([-1, 0, 0])
    _calf_l_v1 = np.array([-1, 0, 0])
    _thigh_r_v1 = np.array([1, 0, 0])
    _calf_r_v1 = [1, 0, 0]
    _upperarm_l_v1 = np.array([1, 0, 0])
    _lowerarm_l_v1 = np.array([1, 0, 0])
    _upperarm_r_v1 = np.array([-1, 0, 0])
    _lowerarm_r_v1 = np.array([-1, 0, 0])

    def __init__(self, bodyPoint: BodyPoint):
        thigh_l_v2 = bodyPoint.l_knee - bodyPoint.l_hip
        calf_l_v2 = bodyPoint.l_ankle - bodyPoint.l_knee
        thigh_r_v2 = bodyPoint.r_knee - bodyPoint.r_hip
        calf_r_v2 = bodyPoint.r_ankle - bodyPoint.r_knee
        upperarm_l_v2 = bodyPoint.l_elbow - bodyPoint.l_shoulder
        lowerarm_l_v2 = bodyPoint.l_wrist - bodyPoint.l_elbow
        upperarm_r_v2 = bodyPoint.r_elbow - bodyPoint.r_shoulder
        lowerarm_r_v2 = bodyPoint.r_wrist - bodyPoint.r_elbow

        self.l_thigh = from2vector(self._thigh_l_v1, thigh_l_v2)
        self.l_calf = from2vector(self._calf_l_v1, calf_l_v2)
        self.r_thigh = from2vector(self._thigh_r_v1, thigh_r_v2)
        self.r_calf = from2vector(self._calf_r_v1, calf_r_v2)
        self.l_upperarm = from2vector(self._upperarm_l_v1, upperarm_l_v2)
        self.l_lowerarm = from2vector(self._lowerarm_l_v1, lowerarm_l_v2)  # ?结果可疑
        self.r_upperarm = from2vector(self._upperarm_r_v1, upperarm_r_v2)
        self.r_lowerarm = from2vector(self._lowerarm_r_v1, lowerarm_r_v2)
        