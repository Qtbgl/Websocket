import asyncio

import websockets

from server_app_2.states import state_idle, state_transmit


async def connected(websocket):
    cc = state_idle()  # current coroutine
    b_i = True
    try:
        while not await cc:  # when to quit connection
            cc = state_transmit() if b_i else state_idle()
            b_i = not b_i

    except websockets.ConnectionClosedOK as e:
        print(e)


async def main():
    async with websockets.serve(connected, "127.0.0.1", 7000):
        print('server just started...')
        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())
