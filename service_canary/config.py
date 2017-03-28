import re
from os import environ

config = {x.replace("CANARY_", "").lower(): y
          for (x,y) in environ.items() if x.startswith("CANARY_")}

def _extract_db(key_prefix, config):
    ret = {}
    suffixes = ["type", "host", "port", "user", "pass", "db_name", "test_query"]
    for sfx in suffixes:
        key = "{}_{}".format(key_prefix, sfx)
        if key in config:
            ret[sfx] = config.get(key)
    return ret

def _extract_api(key_prefix, config):
    ret = {}
    suffixes = ["url", "token", "endpoint"]
    for sfx in suffixes:
        key = "{}_{}".format(key_prefix, sfx)
        if key in config:
            ret[sfx] = config.get(key)
    return ret

def _extract_mc(config):
    ret = {}
    suffixes = ["host", "port"]
    for sfx in suffixes:
        key = "memcached_{}".format(sfx)
        if key in config:
            ret[sfx] = config.get(key)
    return ret

def _extract_rabbit(config):
    ret = {}
    suffixes = ["host", "port"]
    for sfx in suffixes:
        key = "rabbitmq_{}".format(sfx)
        if key in config:
            ret[sfx] = config.get(key)
    return ret


db_re = re.compile("db_\d+")
db_prefixes = set([x.group(0) for x in map(db_re.search, config.keys())
                   if x is not None])

api_re = re.compile("api_\d+")
api_prefixes = set([x.group(0) for x in map(api_re.search, config.keys())
                    if x is not None])

db = {}
api = {}
mc = _extract_mc(config)
rabbit = _extract_rabbit(config)

for pfx in db_prefixes:
    db_conf = _extract_db(pfx, config)
    if db_conf:
        db[pfx] = db_conf

for pfx in api_prefixes:
    api_conf = _extract_api(pfx, config)
    if api_conf:
        api[pfx] = api_conf


print(db)
print(api)
print(mc)
print(rabbit)


