import requests
import endpoint
from endpoint import base_url, headers
import logging
import json

logger = logging.getLogger(__name__)

def test_hello():

    r = requests.get(endpoint.base_url+'/hello')
    logger.info(json.dumps(r.json()))

    assert r.status_code == requests.codes['not_found']

def test_helloworld():

    r = requests.get(endpoint.base_url+'/hello/world', headers=endpoint.headers)

    logger.info(json.dumps(r.json()))

    assert r.status_code is requests.codes.ok

def test_empty():
    """
    PyTest tests are callables whose names start with "test"
    (by default)
    It looks for them in modules whose name contains "test"
    (by default)
    """
    pass


def empty_test():
    """
    My name doesn't start with "test", so I won't get run.
    (by default ;-)
    """
    pass