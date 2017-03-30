from .args import config
from .db import db_types
from .api import api_check


class DBCheckError(Exception):
    pass

class APICheckError(Exception):
    pass


def _run_db_check(conf):
    dbtype = conf.get("type")
    if dbtype is None:
        raise DBCheckError("can't check DB without knowing DB type")

    if dbtype == "riak":
        from .db.riak_check import riak_check
        return riak_check(conf)
    elif dbtype == "postgres":
        from .db.postgres import pg_check
        return pg_check(conf)
    else:
        raise DBCheckError("unknown DB type: %s" % (dbtype,))


def _run_api_check(conf):
    url = conf.get("url")
    if url is None:
        raise APICheckError("can't check API without a URL")
    return api_check(conf)


def _run_mc_check(conf):
    from .mc import mc_check
    return mc_check(conf)


def _run_rabbit_check(conf):
    from .rabbit import rabbit_check
    return rabbit_check(conf)

    return False


def run_checks(conf):
    result = {}
    for key, val in conf.get("db").items():
        result[key] = _run_db_check(val)

    for key, val in conf.get("api").items():
        result[key] = _run_api_check(val)

    if conf.get("mc"):
        result["mc"] = _run_mc_check(conf.get("mc", {}))
    if conf.get("rabbit"):
        result["rabbit"] = _run_rabbit_check(conf.get("rabbit", {}))

    return result


def cli_app():
    from pprint import pprint
    pprint(run_checks(config))
