import socket
import time
import sys
''' Demo for callable instances. In order to call an instance of a object as callable as function'''
class Dnscache():
    def __init__(self):
        self._cache = {}
    
    def __call__(self, host):
        if host in self._cache.keys():
            addr = self._cache[host]
        else:
            addr = socket.gethostbyname(host)
            self._cache[host] = addr
        return addr

    def clear(self):
        self._cache.clear()

def get_hostbyname(host):
    obj = Dnscache()
    start = time.time()
    print(obj(host))
    end = time.time()
    print('First time DNS lookup time {} seconds'.format(end-start))
    start = time.time()
    print(obj(host))
    end= time.time()
    print('Serving from stored DS, DNS lookup time {} seconds'.format(end-start))
    obj.clear()
    start = time.time()
    print(obj(host))
    end = time.time()
    print('After clearing local DS cache, DNS lookup time {} seconds'.format(end-start))

if __name__ == '__main__':
   get_hostbyname(sys.argv[1])
