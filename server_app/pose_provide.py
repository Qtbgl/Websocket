import time
import json


class ContextTest:
    def __init__(self, pics):
        self.pics = pics
        self.gen_cnt = 0

    def __enter__(self):
        print('simulate mediapipe: 创建 mp.pose + 初始化')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'simulate mediapipe: 完成/打断 + 关闭 ({self.gen_cnt}/{self.pics})')
        if exc_type is not None:
            print('__exit__ Exception: ', exc_type, exc_val, exc_tb)
            return False  # 不忽视异常


def pose_s_generator():
    c = ContextTest(20)
    with c:
        for i in range(c.pics):  # TODO
            time.sleep(0.05)  # 50 ms 模拟推理时间
            upper_arm_q = {'x': 0, 'y': 1, 'z': 2, 'w': 3}
            lower_arm_q = {'x': 0, 'y': 1, 'z': 2, 'w': 3}
            pose = {'upper_arm_q': upper_arm_q, 'lower_arm_q': lower_arm_q}
            yield json.dumps(pose)  # gen.close() yield会抛出异常，上下文管理器能接收到
            c.gen_cnt += 1
