#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains function to call API for information about a team's games.

from bvlapi.api.call import call_api
from bvlapi.api.settings import API_BASE_URL


def get_matches_by_guid(guid):
    """ Calls API to retrieve information about a basketball team's season.

    :param str guid: GUID of basketball team

    :rtype: [dict]
    :return: a list of dictionaries containing information about team's games

    :raise ApiCallFailed: something went wrong while calling API
    """
    url = API_BASE_URL + "TeamMatchesByGuid?teamGuid={}".format(guid)
    return call_api(url)
