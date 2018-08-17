from apistar import ASyncApp, Include, Route
# from apistar.docs import docs_routes
# from apistar.statics import static_routes

import asyncio
import time


def syncwelcome(name=None):
    time.sleep(10)
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


async def asyncwelcome(name=None):
    print('start---')
    await asyncio.sleep(10.0)
    print('end----')
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


routes = [
    Route('/', 'GET', asyncwelcome),
    Route('/sync', 'GET', syncwelcome),
    # Include('/docs', docs_routes),
    # Include('/static', static_routes)
]

app = ASyncApp(routes=routes)
