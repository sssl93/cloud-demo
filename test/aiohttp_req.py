import asyncio
from aiohttp import ClientSession
import time


async def fetch(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()


async def run(loop, r):
    url = "http://localhost:8000/nodes"
    tasks = []
    for i in range(r):
        task = asyncio.ensure_future(fetch(url))
        tasks.append(task)
    responses = await asyncio.gather(*tasks)
    # you now have all response bodies in this variable
    print(responses)


def print_responses(result):
    print(result)


start = time.time()
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(loop, 101))
loop.run_until_complete(future)
print('cost ---- ', time.time() - start)
