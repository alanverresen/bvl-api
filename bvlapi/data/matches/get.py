#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains function used to retrieve information about a team's matches.

from bvlapi.data.matches.match import MatchInformation
from bvlapi.api.team import get_matches_by_guid


def get_matches(team_guid):
    """ Queries API for information about a team's games this season.

    :param str team_guid: GUID of team

    :return: list of matches played/to be played by team in chronological order
    :rtype: [MatchInformation]
    """
    matches = []
    for match in get_matches_by_guid(team_guid):
        matches.append(MatchInformation(match))
    return list(sorted(matches, key=lambda m: m.datetime))
