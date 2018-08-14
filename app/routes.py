from api import license
from apistar import Route

license_routes = [
    Route('/license', method='GET', handler=license.get_license_configs),
    Route('/license', method='POST', handler=license.post_license),
    Route('/license', method='PATCH', handler=license.patch_license),
    Route('/license', method='DELETE', handler=license.delete_license),
    Route('/license', method='PUT', handler=license.put_license),
]
