from asyncio import CancelledError

from websockets.exceptions import ConnectionClosedOK


class TransOkay:
    """
    上下文管理类
    """
    def __init__(self, where):
        self.where = where
        self.occ_exc = False
        self.is_closed = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(f'({self.where}) with 退出：正常结束动画生成')
            self.occ_exc = True

        elif exc_type == CancelledError:
            print(f'({self.where}) with 退出：动画生成打断——任务被取消')
            return True

        elif exc_type == ConnectionClosedOK:
            print(f'({self.where}) with 退出：动画生成打断——连接中断')
            self.is_closed = True
            return True
