import asyncio

from app.pose_part.AnimFrame import anim_end
from app.pose_part.pose_generator import pose_simulator
from app.utils.Context.TransOkay import TransOkay


class MyState:
    def __init__(self, websocket):
        self.websocket = websocket
        self.state_i = 0

    def state_deal(self, message):
        if self.state_i == 0:
            self.idle_deal(message)
        else:
            self.tran_deal(message)

    def idle_deal(self, message):
        pass

    def tran_deal(self, message):
        pass

    async def transmit(self):
        with TransOkay('TRANSMIT') as okay:
            for frame in pose_simulator():
                await self.websocket.send(frame)  # debug - 程序连接直接关闭后会卡在这里
                await asyncio.sleep(0.000001)

            await self.websocket.send(anim_end(is_cancel=False))

        self.state_i = 0  # 任务结束或取消，改回标志位
