import asyncio
import websockets

global data
PORT = 7000
print(f"Running on PORT {PORT}")


async def echo(websocket, path):
    global data
    print("A client just connected")
    async for message in websocket:
        print(message)
        await websocket.send(f"Echo From Python {message}")


start_server = websockets.serve(echo, "127.0.0.1", PORT)  # 0.0.0.0
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()
