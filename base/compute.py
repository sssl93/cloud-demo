import libcloud
from base import log, cache_call, loop, extendDriver
import asyncio
import concurrent.futures
import apistar
from types import MethodType


class ComputeAPI(object):
    def __init__(self, provider, username, api_key, auth=None, ex=None):
        self.provider = provider
        self.username = username
        self.api_key = api_key
        self.auth = auth
        self.ex = ex or {}

    @staticmethod
    def data_format(data):
        # TODO data format
        return data

    def _get_driver(self):
        cls = libcloud.get_driver(libcloud.DriverType.COMPUTE, self.provider)
        return extendDriver.get(cls.__class__, cls)(self.username, self.api_key, **self.ex)

    def _get_driver_method(self, func):
        cls = libcloud.get_driver(libcloud.DriverType.COMPUTE, self.provider)
        ins = cls(self.username, self.api_key, **self.ex)
        extend = extendDriver.get(self.provider)
        if hasattr(ins, func):
            pass
        elif hasattr(extend, func):
            method = getattr(extend, func)
            setattr(ins, func, MethodType(method, ins))
        else:
            raise Exception('invalid method "%s" in the driver "%s"' % (func, cls.__class__))
        return getattr(ins, func)

    async def driver_call(self, func, *args):
        method = self._get_driver_method(func)
        return await loop.run_in_executor(None, method, *args)

    def create_node(self):
        result = self.driver_call(self.create_node.__name__)
        return self.data_format(result)

    async def list_nodes(self):
        await self.driver_call('extend_func', 1)
        result = await self.driver_call(self.list_nodes.__name__)
        return self.data_format(result)
