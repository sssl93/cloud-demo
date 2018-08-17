import grequests
import gevent
import requests


def req():
    # resp = requests.get("http://localhost:9055/api/health")
    resp = requests.get("http://localhost:8000/nodes")
    print(resp.content)
    return resp


# gevent.joinall([gevent.spawn(req) for i in range(10)])

async def aiohttp_req():
    from aiohttp import ClientSession
    result = []
    for i in range(10):
        async with ClientSession() as session:
            async with session.get("http://localhost:8000/nodes") as resp:
                return await resp.read()


print(aiohttp_req())
import time
time.sleep(10)
