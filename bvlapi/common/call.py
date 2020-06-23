#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file contains functionality used to make an API call.

import json
import requests

from bvlapi.common.exceptions import ApiCallFailed


def call_api(url):
    """ Sends GET request to REST API, and returns the JSON response.

    :param str url: URL used to consume API

    :rtype: result of API call
    :rtype: dictionary

    :raise ApiCallFailed: something went wrong while calling API
    """
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        m = "Exceptional situation occurred while using BVL API: {}"
        raise ApiCallFailed(m.format(e))
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        m = "Exceptional situation occurred while using BVL API: {}"
        raise ApiCallFailed(m.format(e))
    try:
        return json.loads(response.text)
    except Exception:
        m = "Exceptional situation occurred while using BVL API: {}"
        r = "Unable to convert response content to JSON."
        raise ApiCallFailed(m.format(r))