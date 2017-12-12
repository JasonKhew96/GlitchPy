import json
import logging
from urllib.parse import quote

from requests import Session, Timeout

from glitch.Config import get_username, get_password
from glitch.Utils import generate_ua

logger = logging.getLogger(__name__)
API_ENDPOINT = "http://api.glitchednet.com/V2"


# API_ENDPOINT = "http://127.0.0.1:5000/V2"


def build_json(**kwargs):
    if not kwargs:
        jsonstring = {}
    else:
        jsonstring = kwargs
    jsonstring = json.dumps(jsonstring, separators=(',', ':'))
    return 'Data=' + quote(jsonstring)


def build_url(route, endpoint=API_ENDPOINT):
    return endpoint + route


def post_request(route, endpoint=API_ENDPOINT, **kwargs):
    url = build_url(route, endpoint)
    payload = build_json(**kwargs)

    # proxies = {'http': 'http://127.0.0.1:8888/'}

    headers = {
        'User-Agent': generate_ua(get_username(), get_password()),
        'Host': 'api.glitchednet.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': str(len(payload))}
    s = Session()
    s.headers = headers
    # s.proxies = proxies
    try:
        response = s.post(url, data=payload)
        if response.ok:
            return response
        else:
            return ""
    except Timeout:
        logger.error("Timeout...")
        return ""
    except Exception as e:
        logger.error("Unknown exception: {}".format(e))
        exit(0)
    return ""
