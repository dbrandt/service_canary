import requests


def api_check(config):
    url = config.get("url")  # Existance of url is checked in args.
    ep = config.get("endpoint")
    token = config.get("token")

    headers = {}
    if token is not None:
        headers["Authorization"] = "Token {}".format(token)
    if not url.endswith("/"):
        url += "/"
    if ep is not None:
        if ep.startswith("/"):
            url += ep[1:]
        else:
            url += ep

    try:
        r = requests.get(url, headers=headers)
    except:
        return False
    else:
        return True

