from .compute import ComputeAPI
from apistar.server.components import Component


class CloudFactory(object):
    @classmethod
    def compute(cls, tenant):
        return ComputeAPI(tenant)
