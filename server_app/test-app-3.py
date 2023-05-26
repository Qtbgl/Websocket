import asyncio

import websockets

from server_app.game_status import game_s_x, simple_decide
from server_app.pose_provide import pose_s_generator


async def transmission(websocket):
    try:
        i = 0
        generator = pose_s_generator()
        for pose_s in generator:  # 耗时生成
            i += 1
            await websocket.send(str(i))  # TODO
            await asyncio.sleep(0.000001)  # 1 us 来挂起协程

        print('所有Pose都已生成，并传输')
        await websocket.send('transmit completed')

    except asyncio.CancelledError:
        print('传输中断：caught CancelledError')
        await websocket.send('transmit quit')


def complex_decide(obj):
    return '正繁忙中 - ' + simple_decide(obj)


async def connected(websocket):
    print('succeed: ', websocket)
    print('进入第一阶段')
    await game_s_x(websocket, 1, simple_decide)
    print('进入第二阶段')
    tran_task = asyncio.create_task(transmission(websocket))
    recv_task = asyncio.create_task(game_s_x(websocket, 2, complex_decide))

    done, pending = await asyncio.wait([tran_task, recv_task], return_when=asyncio.FIRST_COMPLETED)
    for task in pending:
        print('pending task :')
        print(task)
        print()
        task.cancel()

    print('进入第三阶段')

    print('closed: ', websocket)


async def main():
    async with websockets.serve(connected, "127.0.0.1", 7000):
        print('server just started.')
        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())
