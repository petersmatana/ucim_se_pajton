from random import randint
from time import sleep, time
import asyncio

start = time()
time_pause = randint(0, 2) * 0.5


def tic():
    return ' at %1.1f seconds' % (time() - start)


def task(pid):
    """Synchronous non-deterministic task.
    """
    sleep(time_pause)
    print('\tbegin{}'.format(tic()))
    print('Task %s done' % pid)
    print('\tend{}'.format(tic()))


async def task_coro(pid):
    """Coroutine non-deterministic task
    """
    await asyncio.sleep(time_pause)
    print('\tbegin{}'.format(tic()))
    print('Task %s done' % pid)
    print('\tend{}'.format(tic()))


def synchronous():
    for i in range(1, 10):
        task(i)


async def asynchronous():
    tasks = [asyncio.ensure_future(task_coro(i)) for i in range(1, 10)]
    await asyncio.wait(tasks)


print('Synchronous start: {}'.format(tic()))
synchronous()
print('Synchronous end: {}'.format(tic()))

ioloop = asyncio.get_event_loop()
print('Asynchronous start: {}'.format(tic()))
ioloop.run_until_complete(asynchronous())
ioloop.close()
print('Asynchronous end: {}'.format(tic()))
