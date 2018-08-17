from common.logging import LoggerHandler
from common.utils import find_config_file, load_config_from_pyfile
from common.cache import Cache
import asyncio
from .extend_drivers import extendDriver

__all__ = ['log', 'config', 'cache_call', 'loop', 'extendDriver']

config_file = find_config_file()
config = load_config_from_pyfile(config_file)
cache_call = Cache()
loop = asyncio.get_event_loop()
log = LoggerHandler(file_path=config['log_file'], log_level=config['log_level']).log_init()

log.info('use config file: "{}"'.format(config_file))
