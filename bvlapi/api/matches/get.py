#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains functionality to retrieve information about calendar.

from bvlapi.api.matches.match import MatchInformation
from bvlapi.common.call import call_api
from bvlapi.common.settings import API_BASE_URL


def get_matches(team_guid):
    """ Queries API for list of matches by team with given GUID.

    :param str team_guid: GUID of team

    :return: list of matches played/to be played by team in chronological order
    :rtype: [MatchInformation]
    """
    data = call_api(API_BASE_URL + "TeamMatchesByGuid?teamGuid=" + team_guid)
    matches = []
    for match in data:
        matches.append(MatchInformation(match))
    return list(sorted(matches, key=lambda m: m.datetime))