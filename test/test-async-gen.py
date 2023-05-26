import asyncio


async def async_gen():
    for i in range(10):
        await asyncio.sleep(0.1)
        yield i


gen = async_gen()
gen.aclose()

