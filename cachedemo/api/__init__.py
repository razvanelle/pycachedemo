from .orderedcache import OrderedCache

EXPIRY_TIME = 10   # time in minutes until expiry
CACHE_SIZE = 1000

print('')
print('=========== CACHE SETUP ==============')
print('INITIALIZING project cache...')

prjcache = OrderedCache(CACHE_SIZE, EXPIRY_TIME)

print('CACHE initialized:', prjcache)
print('Expire Delta:', EXPIRY_TIME)
print('=========== CACHE OK ==============')
print('')
