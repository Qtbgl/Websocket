import asyncio
import time

import websockets


class MkFuture:
    fut: asyncio.Future = None

    def mk(self):  # 调用在事件循环中
        self.fut = asyncio.Future()
        return self.fut


mkr = MkFuture()


async def nap_async(dl, say):
    await asyncio.sleep(dl)  # 必须要asyncio.sleep，而不是time.sleep
    print(say)


async def nap_awake(sl):
    print('111')
    await asyncio.sleep(sl)  # 必须要asyncio.sleep，才能让接收消息不阻塞
    print('222')


async def handler(websocket):
    global mkr
    print("succeed: ", websocket)
    async for message in websocket:
        print(f"(msg: {message})")
        await websocket.send(message)
        if message == 'END_S':
            await websocket.close(reason='server turn down')  # 先关闭连接
            mkr.fut.set_result('关闭服务器')  # 立即关闭了服务
        elif message == 'NAP_A':
            t1 = asyncio.create_task(nap_async(5, 'i'))
            t2 = asyncio.create_task(nap_async(5, 'j'))
            print(f"started at {time.strftime('%X')}")
            await t1
            print('???')
            await t2
            print(f"finished at {time.strftime('%X')}")
        elif message == 'NAP_W':
            loop = asyncio.get_running_loop()
            loop.create_task(nap_awake(5))  # 与await的区别

    print('closed:', websocket)


async def main():
    global mkr
    async with websockets.serve(handler, "127.0.0.1", 7000):
        print('server just start')
        fut = mkr.mk()
        print('future arrived: ', await fut)


if __name__ == "__main__":
    asyncio.run(main())
