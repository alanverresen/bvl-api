#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains functionality used to retrieve information about competitions.

from bvlapi.data.competitions.competition import Competition
from bvlapi.api.team import get_detail_by_guid


def get_competitions(team_guid):
    """ Queries API for list of competitions for team with given GUID.

    :param str team_guid: GUID of team

    :rtype: [Competition]
    :return: list of competitions
    """
    data = get_detail_by_guid(team_guid)
    if len(data) != 1:
        return []
    competitions = []
    for poule in data[0].get("poules", []):
        competitions.append(Competition(poule))
    return competitions
