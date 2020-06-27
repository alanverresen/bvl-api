#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains function used to make an API call.

from bvlapi.common.exceptions import ApiCallFailed
from bvlapi.common.exceptions import BvlApiException
from bvlapi.common.http import get_json


def call_api(url):
    """ Sends GET request to API, and returns the JSON response.

    :param str url: URL used to consume API

    :rtype: dict or [dict]
    :return: result of API call as a dictionary

    :raise ApiCallFailed: something went wrong while calling API
    """
    try:
        return get_json(url)
    except BvlApiException as e:
        m = "Exceptional situation occurred while using BVL API: {}"
        raise ApiCallFailed(m.format(e))
