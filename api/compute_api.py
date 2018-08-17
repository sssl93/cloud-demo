from base import log
from base.cloud_factory import CloudFactory
from base.compute import ComputeAPI
import asyncio


def create_node(data: dict):
    ComputeAPI('openstack', 'username', 'key').create_node()


async def list_nodes():
    ex = {
        'ex_force_auth_version': '3.x_password',
        'ex_force_auth_url': 'http://10.22.1.14:5000',
        'ex_tenant_name': 'admin',
    }
    print('prepare ok')
    result = await ComputeAPI('openstack', 'admin', 'Bocloud', ex=ex).list_nodes()
    # print(result)
    print('exec ok')
    return 'ok'
