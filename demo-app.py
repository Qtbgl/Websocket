import asyncio

import websockets


async def handler(websocket):
    print("succeed: ", websocket)
    message = await websocket.recv()  # 接收一次消息后，即关闭连接
    print("msg: ", message)


async def main():
    print("run coroutine 1")
    async with websockets.serve(handler, "127.0.0.1", 7000):
        print("the server started 2")
        await asyncio.Future()  # 必须有，保持服务开启
        
    print("end 3")



if __name__ == "__main__":
    asyncio.run(main())
    
