import asyncio


async def add_one(result):
    print('add 1 to result')
    await asyncio.sleep(1)
    return result + 1

async def compute(x, y):
    print('need to compute ' + str(x) + ' and ' + str(y))
    await asyncio.sleep(1)
    return await add_one(x + y)


async def print_sum(x, y):
    result = await compute(x, y)
    print('result of ' + str(x) + ' and ' + str(y) + ' is ' + str(result))


loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 1))
loop.close()
