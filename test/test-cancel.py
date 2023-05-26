from asyncio.exceptions import CancelledError

import asyncio
import time


async def coro():
    try:
        await asyncio.sleep(15)
    except CancelledError:
        print("catched CancelledError :")

        
async def stop_(task_obj):
    print("stop 3 sec later")
    for i in range(3):
        print(i + 1)
        await asyncio.sleep(1)
        
    print("ready to stop now")
    print(task_obj.cancel())


async def co():
    try:
        for i in range(50):
            time.sleep(5)  # 0.050
            try:
                await asyncio.sleep(0.000001)  # 1 us，只在休眠时，才能取消（被其他协程）
                
            except CancelledError:
                print("catched CancelledError - 1")
                raise
                
    except CancelledError:
        print("catched CancelledError - 2")
    
    
async def main():
    ts = asyncio.create_task(co())
    ss = asyncio.create_task(stop_(ts))
    await(ts)
    await(ss)


asyncio.run(main())
