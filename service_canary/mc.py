import sys
import socket
try:
    from pymemcache.client.base import Client
except ImportError:
    print("memcached test requested, but pymecache not installed. "
          "Try 'pip install pymemcache' and try again.")
    sys.exit(1)

def mc_check(config):
    host = config.get("host", "localhost")
    port = int(config.get("port", 11211))
    try:
        mc = Client((host, port))
        mc.stats()
    except:
        return False
    else:
        return True

