#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains function to call API for information about a club.

from bvlapi.api.call import call_api
from bvlapi.api.settings import API_BASE_URL


def get_detail_by_guid(guid):
    """ Calls API to retrieve information about a basketball club.

    :param str guid: GUID of basketball club

    :rtype: [dict]
    :return: a list of dictionaries containing information about club:
        - contains one dictionary if club exists
        - is empty if club does not exist

    :raise ApiCallFailed: something went wrong while calling API
    """
    url = API_BASE_URL + "OrgDetailByGuid?issguid={}".format(guid)
    return call_api(url)
