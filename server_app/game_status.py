import asyncio
import json
from json import JSONDecodeError


class GameNextDecision(Exception): pass


async def game_s_x(websocket, x, decider):
    try:
        async for message in websocket:  # 异步等待信息
            try:
                echo = decider(json.loads(message))
                await websocket.send(f'game s {x} < {echo}')
            except JSONDecodeError:
                await websocket.send(f'game s {x} < JSON 解析异常')
            except KeyError:
                await websocket.send(f'game s {x} < JSON 缺失键')
            except GameNextDecision:
                await websocket.send(f'game s {x} < 进入下一阶段')
                return
            except asyncio.CancelledError:
                print('caught CancelledError - 1')
                raise
    except asyncio.CancelledError:
        print('caught CancelledError - 2')  # 在此处捕获
        websocket.aclose()
        raise


def simple_decide(obj):
    if type(obj) == dict and obj['game_next']:
        raise GameNextDecision
    else:
        return 'echo: ' + json.dumps(obj)
