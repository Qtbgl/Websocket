import asyncio

import websockets

from server_app_2.state_idle import state_idle

from server_app_2.state_transmit import state_transmit
from server_app_2.utils.Excepts import ConnQuit


async def connected(websocket):
    try:
        while True:
            info = await state_idle(websocket)
            await state_transmit(websocket, info)
    except websockets.ConnectionClosedOK as e:
        print('连接异常切断：', e)
    except ConnQuit:
        print('请求终止连接')


async def main():
    async with websockets.serve(connected, "127.0.0.1", 7000):
        print('server just started...')
        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())
