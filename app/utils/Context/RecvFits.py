from app.utils.Excepts import MsgNotFit


class RecvFits:
    """
    上下文管理类
    """
    def __init__(self, where: str, show_exc=True):
        self.where = where
        self.show_exc = show_exc
        self.is_failed = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == MsgNotFit:
            self.is_failed = True
            if self.show_exc:
                print(self.where, ':', exc_val)

            return True
