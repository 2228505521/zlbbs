
import memcache

cache = memcache.Client(['127.0.0.1:11211'], debug=True)

def set(key, value, timeout=60):
    if key and value:
        return cache.set(key.strip(), value.strip(), timeout)
    else:
        print('%s本地存储失败' % key)

def get(key):
    if key:
        return cache.get(key.strip())
    else:
        print('%s为空，获取失败' % key)

def delete(key):
    return cache.delete(key)