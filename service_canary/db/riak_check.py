import sys
import socket
try:
    import riak
except ImportError:
    print("Riak test requested, but riak library not installed. "
          "Try 'pip install riak' and try again.")
    sys.exit(1)

def riak_check(config):
    host = config.get("host", "localhost")
    port = int(config.get("port", 8087))
    def_timeout = socket.getdefaulttimeout()
    socket.setdefaulttimeout(1.5)
    rc = riak.RiakClient(nodes=[{"host": host, "pb_port": port}])
    try:
        res = rc.ping()
    except:
        return False
    else:
        return True
    finally:
        rc.close()
        socket.setdefaulttimeout(def_timeout)
