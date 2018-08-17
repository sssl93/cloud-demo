from functools import wraps
import time


def timing(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        begin = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        cost = end - begin
        print("[%s] invoke end, apply [%s] seconds" % (str(func), cost))
        return ret

    return wrap
