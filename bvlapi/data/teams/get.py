#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains functionality to retrieve a list of team's for a given club.

from bvlapi.api.club.detailByGuid import get_detail_by_guid

from bvlapi.data.teams.team import Team


def get_teams(club_guid):
    """ Returns a list of club's teams.

    :param str club_guid: GUID of team

    :rtype: []
    :return: a list of objects containing information about a club's teams
    """
    o = get_detail_by_guid(club_guid)
    if len(o) == 0:
        return []
    teams = []
    for team_info in o[0]["teams"]:
        teams.append(Team(team_info))
    return teams
