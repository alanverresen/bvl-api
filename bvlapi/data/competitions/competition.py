#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains class used to hold information about a competition.

from bvlapi.data.competitions.standing import CompetitionStanding
from bvlapi.data.parse import use_fallback_value


class Competition:
    """ Used to hold information about a basketball competition.

    :ivar str name: name of competition
    :ivar [CompetitionStanding] standings: standings of competition
    """
    def __init__(self, d):
        """ Initializes a new instance based on given information.

        :param dict d: contains information about competition
        """
        self.name = _parse_competition_name(d)      # name of competition
        self.standings = _parse_standings(d)        # competition standings


@use_fallback_value("???")
def _parse_competition_name(d):
    """ Used to parse the name of a competition.
    """
    return d.get("naam", "Competitie Onbekend")


@use_fallback_value([])
def _parse_standings(d):
    """ Used to parse the standings of a competition.
    """
    standings = []
    for o in d.get("teams", []):
        info = CompetitionStanding(o)
        standings.append(info)
    return standings
