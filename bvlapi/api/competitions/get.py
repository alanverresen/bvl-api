#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains functionality to retrieve information about competitions.

from bvlapi.api.competitions.competition import Competition
from bvlapi.common.call import call_api
from bvlapi.common.settings import API_BASE_URL


def get_competitions(team_guid):
    """ Queries API for list of competitions for team with given GUID.

    :param str team_guid: GUID of team

    :return: list of competitions
    :rtype: [Competition]
    """
    data = call_api(API_BASE_URL + "TeamDetailByGuid?teamGuid=" + team_guid)
    if len(data) != 1:
        return []
    competitions = []
    for poule in data[0].get("poules", []):
        competitions.append(Competition(poule))
    return competitions
