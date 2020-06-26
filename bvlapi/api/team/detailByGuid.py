#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains function to call API for information about a team.

from bvlapi.api.call import call_api
from bvlapi.api.settings import API_BASE_URL


def get_detail_by_guid(guid):
    """ Calls API to retrieve information about a basketball team.

    :param str guid: GUID of basketball team

    :rtype: [dict]
    :return: a list of dictionaries containing information about team:
        - contains one dictionary if team exists
        - is empty if team does not exist

    :raise ApiCallFailed: something went wrong while calling API
    """
    url = API_BASE_URL + "TeamDetailByGuid?teamGuid={}".format(guid)
    return call_api(url)
