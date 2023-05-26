import asyncio
import json

from server_app_2.pose_part.AnimFrame import anim_begin, anim_end
from server_app_2.utils.Excepts import MsgNotFit, ConnQuit
from server_app_2.utils.RecvDecide import RecvDecide
from server_app_2.pose_part.pose_generator import pose_simulator
from server_app_2.state_idle import IdleDecide


async def transmit(websocket):
    await websocket.send(anim_begin())
    try:
        for frame in pose_simulator():
            await websocket.send(frame)
            await asyncio.sleep(0.000001)

        print('正常结束动画生成')
        await websocket.send(anim_end(is_cancel=False))
    except asyncio.CancelledError:
        print('动画生成打断')
        await websocket.send(anim_end(is_cancel=True))


async def quit_trans(websocket):
    async for message in websocket:
        info = TransDecide()
        if info.fit(message):
            if info.msg:
                print('(TRANSMIT) 接收到消息: ', info.msg)

            if info.to_quit_tran or info.to_quit_conn:
                return info


async def state_transmit(websocket, info: IdleDecide):
    tran_task = asyncio.create_task(transmit(websocket))
    recv_task = asyncio.create_task(quit_trans(websocket))
    done, pending = await asyncio.wait([tran_task, recv_task], return_when=asyncio.FIRST_COMPLETED)
    for task in pending:  # 停止另一个任务
        task.cancel()

    if recv_task.done():
        if recv_task.result().to_quit_conn:
            raise ConnQuit


class TransDecide(RecvDecide):
    to_quit_conn = False
    to_quit_tran = False

    def _decide_fit(self, obj, decide):
        if self.decide == 1:
            self.to_quit_tran = True
        elif self.decide == 2:
            self.to_quit_conn = True
        elif self.decide is not None:
            raise MsgNotFit(f'the decide of input is ignored: {decide}')  # 过滤 3
