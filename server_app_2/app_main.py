import asyncio

import websockets

from server_app_2.State.GameState import GameState
from server_app_2.utils.Excepts import ConnQuit


async def connected(websocket):
    try:
        print('succeed: ', websocket)
        gs = GameState(websocket)
        async for message in websocket:  # 会自动处理 ConnectionClosedOK 异常
            gs.state_deal(message)

    except ConnQuit:
        print('(websocket) 请求终止连接')
    except:
        print('(websocket) 捕获到其他异常')

    print('closed: ', websocket)


async def main():
    async with websockets.serve(connected, "127.0.0.1", 7000):
        print('server just started...')
        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())
