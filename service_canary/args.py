import sys

from .config import (_get_prefixes, db_re, api_re, config, _extract_db,
                     _extract_api, _extract_mc, _extract_rabbit)


class ArgumentError(Exception):
    pass


def _split_arg(arg):
    if "=" not in arg:
        raise ArgumentError(
            "commandline arguments must be on the form --db-1-host=localhost")
    return arg.split("=")

args = [x.replace("--", "").replace("-", "_").lower()
        for (x) in sys.argv[1:] if x.startswith("--")]

if "config" in args:
    args.pop(args.index("config"))
    dump_config = True
else:
    dump_config = False


args = dict(map(_split_arg, args))


db_prefixes = _get_prefixes(db_re, args)
api_prefixes = _get_prefixes(api_re, args)


for pfx in db_prefixes:
    db_conf = _extract_db(pfx, args)
    if db_conf:
        db = config.get("db", {})
        if pfx in db:
            db[pfx].update(db_conf)
        else:
            db[pfx] = db_conf


for pfx in db_prefixes:
    db_conf = _extract_db(pfx, args)
    if db_conf:
        db = config.get("db", {})
        if pfx in db:
            db[pfx].update(db_conf)
        else:
            db[pfx] = db_conf

for pfx in api_prefixes:
    api_conf = _extract_api(pfx, args)
    if api_conf:
        api = config.get("api", {})
        if pfx in api:
            api[pfx].update(api_conf)
        else:
            api[pfx] = api_conf


mc = _extract_mc(args)
if mc:
    config["mc"].update(mc)

rabbit = _extract_rabbit(args)
if rabbit:
    config["rabbit"].update(rabbit)


if dump_config:
    from pprint import pprint
    pprint(config)
    sys.exit(0)
