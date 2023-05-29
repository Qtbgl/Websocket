import numpy as np


class BodyPoint:
    def __init__(self, ue_x, ue_y, ue_z):
        self.r_shoulder = np.array([ue_x[12], ue_y[12], ue_z[12]])
        self.l_shoulder = np.array([ue_x[11], ue_y[11], ue_z[11]])
        self.r_elbow = np.array([ue_x[14], ue_y[14], ue_z[14]])
        self.l_elbow = np.array([ue_x[13], ue_y[13], ue_z[13]])
        self.r_wrist = np.array([ue_x[16], ue_y[16], ue_z[16]])
        self.l_wrist = np.array([ue_x[15], ue_y[15], ue_z[15]])  # debug
        self.r_hip = np.array([ue_x[24], ue_y[24], ue_z[24]])
        self.l_hip = np.array([ue_x[23], ue_y[23], ue_z[23]])
        self.r_knee = np.array([ue_x[26], ue_y[26], ue_z[26]])
        self.l_knee = np.array([ue_x[25], ue_y[25], ue_z[25]])
        self.r_ankle = np.array([ue_x[28], ue_y[28], ue_z[28]])
        self.l_ankle = np.array([ue_x[27], ue_y[27], ue_z[27]])
