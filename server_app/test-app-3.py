import asyncio

import websockets

from server_app.game_status import game_s_x, simple_decide, GameNextDecision
from server_app.pose_provide import pose_s_generator


async def transmission(websocket, generator):
    i = 0
    for pose_s in generator:  # 耗时生成
        # print(i, end=' ')  # TODO
        i += 1
        # if i % 30 == 0:
        #     print()
        await websocket.send(str(i))
        await asyncio.sleep(0.000001)  # 1 us 来挂起协程

    print('生成器结束')
    await websocket.send('generator quit')


async def connected(websocket):
    print('succeed: ', websocket)
    print('进入第一阶段')
    await game_s_x(websocket, 1, simple_decide)
    print('进入第二阶段')
    gen = pose_s_generator()
    tran_coro = transmission(websocket, gen)
    tran_task = asyncio.create_task(tran_coro)

    def complex_decide(obj):
        try:
            return '正繁忙中 - ' + simple_decide(obj)
        except GameNextDecision as e:
            print('打断生成 gen.close()', gen.close())  # TODO
            raise e

    recv_task = asyncio.create_task(game_s_x(websocket, 2, complex_decide))

    done, pending = await asyncio.wait([tran_task, recv_task])
    print('进入第三阶段 pending =', pending)

    print('closed: ', websocket)


async def main():
    async with websockets.serve(connected, "127.0.0.1", 7000):
        print('server just started.')
        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())
