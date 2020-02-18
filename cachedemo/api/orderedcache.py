from datetime import datetime, timedelta
import threading
import collections
import functools
import time

# Semaphore for concurrent access
cacheLock = threading.Semaphore()

# decorator to sync the cache access in multithreaded env
def guard(func):
  def guarded(*args, **kwds):
    cacheLock.acquire()
    try:
      return func(*args, **kwds)
    finally:
      cacheLock.release()
  return guarded


class OrderedCache:  
  def __init__(self, size, expiry):
    """Constructor"""
    self.cache = collections.OrderedDict()
    self.max_cache_size = size
    self.expiry = expiry
  
  def state(self):
    print('Cache state --- Count: ', len(self.cache), ' Expiry (minutes):', self.expiry)
    for i in self.cache.items():
      print(' >', i)

  def getTimeStr(self, delta = 0):  
    epochTime = time.time() - delta * 60000
    epochTime = round(epochTime * 1000)
    strTime = str(epochTime)
    return strTime

  @guard
  def put(self, id, timeStamp):
    # set the new element (insert if new)
    self.cache[id] = timeStamp
    self.cache.move_to_end(id)
    self.clean()
    self.state()  

  @guard
  def getupdates(self, refTime):
    refTime = str(refTime)
    res = {} # search newer items in reverse
    for key in list(self.cache)[::-1]:
      if self.cache[key] > refTime:
        res[key] = self.cache[key]
      else:
        break
    
    self.clean()
    self.state()
    return res

  def clean(self):
    expireTime = self.getTimeStr(self.expiry)

    # Iterate from start to delete expired items. Ordered by time.
    for key in list(self.cache):
      if self.cache[key] < expireTime:
        del self.cache[key]
      else:
        break

