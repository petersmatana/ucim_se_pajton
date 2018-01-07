import time
import asyncio

start = time.time()


def tic():
    return 'at %1.1f seconds' % (time.time() - start)


async def gr1():
    # Busy waits for a second, but we don't want to stick around...
    print('gr1 started work: {}'.format(tic()))
    await asyncio.sleep(8)
    print('gr1 ended work: {}'.format(tic()))


async def gr2():
    # Busy waits for a second, but we don't want to stick around...
    print('gr2 started work: {}'.format(tic()))
    await asyncio.sleep(2)
    print('gr2 Ended work: {}'.format(tic()))


async def gr3():
    print("gr3 Let's do some stuff while the coroutines are blocked, {}".format(tic()))
    await asyncio.sleep(3)
    print("gr3 Done! {}".format(tic()))


async def gr4():
    """
    tohle se provede po dokonceni celyho programu pukud je tu dlouhy cas
    """

    print("g4 Let's do some stuff while the coroutines are blocked, {}".format(tic()))
    await asyncio.sleep(15)
    print("g4 Done! {}".format(tic()))


print('PROGRAM START: {}'.format(tic()))

ioloop = asyncio.get_event_loop()
tasks = [
    ioloop.create_task(gr1()),
    ioloop.create_task(gr2()),
    ioloop.create_task(gr3()),
    ioloop.create_task(gr4())
]
ioloop.run_until_complete(asyncio.wait(tasks))
ioloop.close()

print('PROGRAM END: {}'.format(tic()))
