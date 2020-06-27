#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains functionality to send GET requests for different types of resources.

import requests

from bvlapi.common.exceptions import HttpRequestFailed
from bvlapi.common.exceptions import HttpResponseBadStatusCode
from bvlapi.common.exceptions import HttpResponseInvalidJSON


def get_bytes(url):
    """ Sends a HTTP request to retrieve a resource that is a string of bytes.

    :param str url: URL of resource

    :rtype: bytes
    :return: resource with given URL

    :raise HttpRequestFailed: sth went wrong while making HTTP request
    :raise HttpResponseBadStatusCode: HTTP response had bad status code
    """
    response = _get_request(url)
    return response.content


def get_text(url):
    """ Sends a HTTP request to retrieve a resource that is text.

    :param str url: URL of resource

    :rtype: str
    :return: resource with given URL

    :raise HttpRequestFailed: sth went wrong while making HTTP request
    :raise HttpResponseBadStatusCode: HTTP response had bad status code
    """
    response = _get_request(url)
    return response.text


def get_json(url):
    """ Sends a HTTP request to retrieve a resource that is a JSON object.

    :param str url: URL of resource

    :rtype: [dict] or dict
    :return: resource with given URL

    :raise HttpRequestFailed: sth went wrong while making HTTP request
    :raise HttpResponseBadStatusCode: HTTP response had bad status code
    :raise HttpResponseInvalidJSON: HTTP response was invalid JSON object
    """
    response = _get_request(url)
    try:
        o = response.json()
    except ValueError as e:
        msg = "HTTP Response to '{}' contained invalid JSON object: {}"
        raise HttpResponseInvalidJSON(msg.format(url, e))
    return o


def _get_request(url):
    """ Sends a HTTP request with an appropriate user agent.
    """
    try:
        response = requests.get(url, headers={
            # Change User-Agent to reflect use of this module.
            "user-agent": "python/bvl-api/0.2.0",
        })
    except requests.exceptions.RequestException as e:
        msg = "Could not download resource with URL '{}': {}"
        raise HttpRequestFailed(msg.format(url, e))

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        msg = "Could not download resource with URL '{}': Bad Status Code: {}"
        raise HttpResponseBadStatusCode(msg.format(url, e))

    return response
