import asyncio

import websockets

from server_app.game_status import game_s_x, simple_decide, GameNextDecision
from server_app.pose_provide import pose_s_generator


async def transmission(websocket):
    i = 0
    generator = pose_s_generator()
    for pose_s in generator:  # 耗时生成
        i += 1
        await websocket.send(str(i))  # TODO
        try:
            await asyncio.sleep(0.000001)  # 1 us 来挂起协程
        except asyncio.CancelledError:
            # generator.close()
            break
            print('caught CancelledError')
            raise

    print('生成器结束')
    await websocket.send('generator quit')


async def connected(websocket):
    print('succeed: ', websocket)
    print('进入第一阶段')
    await game_s_x(websocket, 1, simple_decide)
    print('进入第二阶段')
    tran_coro = transmission(websocket)
    tran_task = asyncio.create_task(tran_coro)

    def complex_decide(obj):
        try:
            return '正繁忙中 - ' + simple_decide(obj)
        except GameNextDecision as e:
            print('task.cancel() ready...')  # TODO
            print(tran_task.cancel())
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

r"""log python
E:\Software2022Spring\Python\Python310\python.exe "E:/Temp/Intellij IDEA/PycharmProjects/WebSocket/server_app/test-app-3.py"
server just started.
succeed:  <websockets.legacy.server.WebSocketServerProtocol object at 0x0000021EE44D66B0>
进入第一阶段
进入第二阶段
simulate mediapipe: 创建 mp.pose + 初始化
task.cancel() ready...
True
simulate mediapipe: 完成/打断 + 关闭 (13/100)
__exit__ Exception:  <class 'GeneratorExit'>  <traceback object at 0x0000021EE44F58C0>
caught CancelledError
进入第三阶段 pending = set()
closed:  <websockets.legacy.server.WebSocketServerProtocol object at 0x0000021EE44D66B0>

"""


r"""  log cmd
C:\Users\lenovo>python -m websockets "ws://127.0.0.1:7000/"
Connected to ws://127.0.0.1:7000/.
> {"game_next": true}
< game s 1 < 进入下一阶段
< 1
< 2
< 3
< 4
< 5
< 6
< 7
< 8
< 9
< 10
< 11
< 12
> {"game_next": true}
< 13
< 14
< game s 2 < 进入下一阶段
Connection closed: 1000 (OK).


C:\Users\lenovo>
"""