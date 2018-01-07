import random
from time import sleep, time
import asyncio

start = time()


def tic():
    return ' at %1.1f seconds' % (time() - start)


def task(pid):
    """Synchronous non-deterministic task.
    """
    sleep(random.randint(0, 2) * 0.01)
    print('\tbegin{}'.format(tic()))
    print('Task %s done' % pid)
    print('\tend{}'.format(tic()))


async def task_coro(pid):
    """Coroutine non-deterministic task
    """
    await asyncio.sleep(random.randint(0, 2) * 0.001)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


async def asynchronous():
    tasks = [asyncio.ensure_future(task_coro(i)) for i in range(1, 10)]
    await asyncio.wait(tasks)


print('Synchronous:')
synchronous()

ioloop = asyncio.get_event_loop()
print('Asynchronous:')
ioloop.run_until_complete(asynchronous())
ioloop.close()
