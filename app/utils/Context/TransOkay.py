from asyncio import CancelledError

from websockets.exceptions import ConnectionClosedOK


class TransOkay:
    """
    上下文管理类
    """
    def __init__(self, where):
        self.where = where

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # 忽视所有异常
        if exc_type:
            if exc_type == CancelledError:
                print(f'({self.where}) with 退出：动画生成打断：任务被取消')

            elif exc_type == ConnectionClosedOK:
                print(f'({self.where}) with 退出：动画生成打断：连接中断')

            else:
                print(f'({self.where}) with 退出：存在特殊异常：', exc_type)

            return True
