import asyncio

import websockets


async def handler(websocket):
    # global fut
    print("succeed: ", websocket)
    message = await websocket.quit_trans()  # 接收一次消息后，即关闭连接
    print("msg: ", message)
    # fut.set_result('... world')


async def when_end(fut: asyncio.Future):
    print('进入', end=' ')
    for i in range(3):
        print(1 + i, end=' ')
        await asyncio.sleep(1)

    fut.set_result('hello future!')
    print('结束', end='\n')


async def main():
    print("running coroutine - 1")
    async with websockets.serve(handler, "127.0.0.1", 7000):
        print("server just start - 2")
        fut = asyncio.Future()
        loop = asyncio.get_running_loop()
        loop.create_task(when_end(fut))
        print('未堵塞？？？')
        print('future arrived: ', await fut)
        
    print("end - 3")


if __name__ == "__main__":
    asyncio.run(main())
    
