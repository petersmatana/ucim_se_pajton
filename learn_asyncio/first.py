import asyncio

async def foo():
    print('- begin foo')
    await asyncio.sleep(1)
    print('-- end foo')


async def bar():
    print('- begin bar')
    await asyncio.sleep(3)
    print('-- end bar')


ioloop = asyncio.get_event_loop()

tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]


wait_tasks = asyncio.wait(tasks)

ioloop.run_until_complete(wait_tasks)
# ioloop.run_forever()

# ani kdyz metody na "jakoby spousteni zkopiruju" tak
# se to neprovede 2x...


ioloop.close()
