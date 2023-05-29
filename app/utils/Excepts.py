class MsgNotFit(Exception):
    pass


class ConnQuit(Exception):
    pass


class VideoCaptureFailed(Exception):
    def __init__(self, on_open):
        self.on_open = on_open


class ImgProcessExc(Exception):
    pass
