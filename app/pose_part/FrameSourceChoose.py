class FrameSourceChoose:
    def __init__(self, from_simulate=True):
        if from_simulate:
            from app.pose_part.generators.pose_simulator import pose_simulator
            self.__choose = pose_simulator
        else:
            from app.pose_part.generators.pose_generator import pose_generator
            self.__choose = pose_generator

        self.from_simulate = from_simulate

    def __call__(self, video):
        return self.__choose(video)
