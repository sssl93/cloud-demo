from base.license import License
from base import log


async def get_license_configs(user_id: int):
    print(user_id)
    return {1: 1, 2: 2}


async def post_license(data: dict):
    print(data)
    return 'post ok'


async def put_license(data: dict):
    print(data)
    return 'put ok'


async def patch_license(data: dict):
    print(data)
    return 'patch ok'


async def delete_license(user_id: int):
    print(user_id)
