import libcloud
from libcloud.compute.drivers import openstack

# OpenStackSource = libcloud.get_driver(libcloud.DriverType.COMPUTE, 'openstack')
extendDriver = {}


class OpenStackExtend(object):
    # def __init__(self, key, secret=None, secure=True, host=None, port=None, api_version=None, region=None, **kwargs):
    #     # cls.__init__(self, key, secret, secure, host, port, api_version, region, **kwargs)
    #     self = OpenStackSource.__init__(key, secret, secure, host, port, api_version, region, **kwargs)
    #     super(OpenStackExtend, self).__init__(key, secret, secure, host, port, api_version, region, **kwargs)

    # def __new__(cls, *args, **kwargs):
    #     # obj = object.__new__(OpenStackSource)
    #     # now_obj = super(OpenStackSource, cls).__new__(cls)
    #     # cls = OpenStackSource
    #     # obj = object.__new__(cls)
    #     super(OpenStackExtend, cls).__new__(OpenStackSource, *args, **kwargs)
    #     return object.__new__(OpenStackExtend)
    # return now_obj.__new__(cls, *args, **kwargs)
    # return super(cls, OpenStackExtend).__new__(cls)
    # TODO auth
    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def extend_func(self, x):
        print(self.name, x)
        return 'extend func of openstack'


# extend[OpenStackSource.__class__] = OpenStackExtend
extendDriver['openstack'] = OpenStackExtend
