#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains class used to hold information about a basketball team.

from bvlapi.data.parse import use_fallback_value


class Team:
    """ Class used to hold data that was retrieved about a team.
    """

    def __init__(self, o):
        """ Initializes a new instance based on given information.
        """
        self.guid = parse_team_guid(o)
        self.name = parse_team_name(o)


@use_fallback_value("???")
def parse_team_guid(o):
    """ Used to parse GUID of a team.
    """
    return o.get("guid", "x").replace(" ", "+")


@use_fallback_value("???")
def parse_team_name(o):
    """ Used to parse name of a team.
    """
    return o.get("naam", "r")
