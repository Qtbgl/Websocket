class FrameSourceChoose:
    def __init__(self, from_simulate=True):
        if from_simulate:
            from app.pose_part.generators.pose_simulator import pose_simulator
            self.__choose = pose_simulator
            print('(FrameSourceChoose) : 正在使用姿态数据模型生成器')
        else:
            from app.pose_part.generators.pose_generator import pose_generator
            print('(FrameSourceChoose) : blazepose generator 加载完成')
            self.__choose = pose_generator

        self.from_simulate = from_simulate

    def __call__(self, video):
        return self.__choose(video)
