class Cache(object):
    def __init__(self):
        # self.cache = {(ADMIN_USER, ADMIN_PASSWORD): ADMIN_USER, }
        self.cache = {}
        self.keys = []
        self.length = 500

    def __call__(self, func, *args, **kwargs):
        key = str((func.__func__, args, kwargs))
        try:
            return self.cache[key]
        except KeyError:
            value = func(*args, **kwargs)
            self.set_cache(key, value)
            return value
        except TypeError:
            return func(*args, **kwargs)

    def __str__(self):
        return str(self.cache)

    def clean(self):
        if len(self.keys) > self.length:
            split_index = len(self.keys) - self.length
            for k in self.keys[0:split_index]:
                del self.cache[k]
            self.keys = self.keys[split_index:]

    def set_cache(self, key, value):
        self.cache[key] = value
        if key not in self.keys:
            self.keys.append(key)
        else:
            self.keys.sort(key=lambda k: k == key)
        self.clean()
