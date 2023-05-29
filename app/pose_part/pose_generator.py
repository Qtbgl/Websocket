import time

from app.pose_part.Frame.AnimFrame import anim_pose
from app.pose_part.Frame.PoseData import PoseData


def pose_simulator():
    with ContextTest():
        for i in range(100):  # TODO
            time.sleep(0.05)  # 50 ms 模拟推理时间
            pose = PoseData()
            pose.upperarm_l = {'x': 0, 'y': 1, 'z': 2, 'w': 3}
            pose.lowerarm_l = {'x': 0, 'y': 1, 'z': 2, 'w': 3}
            am = anim_pose(pose, i + 1, 0.02)
            yield am


class ContextTest:
    def __enter__(self):
        print('simulate mediapipe: 创建 mp.pose + 初始化')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'simulate mediapipe: 完成/打断 + 关闭')
        if exc_type is not None:  # 不忽略异常
            print('simulate mediapipe: __exit__ Exception: ', exc_type, exc_val, exc_tb)
