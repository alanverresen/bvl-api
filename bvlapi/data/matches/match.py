#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains class used to hold information about a basketball match.

from datetime import datetime

from bvlapi.data.parse import use_fallback_value
from bvlapi.data.settings import DEFAULT_DATE
from bvlapi.data.settings import DEFAULT_TIME
from bvlapi.data.settings import TIMEZONE


class MatchInformation:
    """ Used to represent and organize information about a basketball match.

    :ivar datetime datetime: date and time of match
    :ivar str location: name of location where match is played
    :ivar str home_team: name of home team
    :ivar int home_score: score of home team
    :ivar str home_guid_team: GUID of home team
    :ivar str home_guid_club: GUID of home team's club
    :ivar str visiting_team: name of visiting team
    :ivar int visiting_score: score of visiting team
    :ivar str visiting_guid_team: GUID of visiting team
    :ivar str visiting_guid_club: GUID of visiting team's club
    :ivar bool is_forfeit: did one of the team's forfeit the game?
    :ivar bool is_bekermatch: is a cup match?
    """

    def __init__(self, d):
        """ Initializes a new instance based on information from dictionary
            containing data retrieved from API.
        """
        self.datetime = parse_datetime(d)
        self.location = parse_location(d)
        self.home_team = parse_home(d)
        self.home_score = parse_home_score(d)
        self.home_guid_club = parse_home_guid_club(d)
        self.home_guid_team = parse_home_guid_team(d)
        self.visiting_team = parse_visitor(d)
        self.visiting_score = parse_visitor_score(d)
        self.visiting_guid_club = parse_visitor_guid_club(d)
        self.visiting_guid_team = parse_visitor_guid_team(d)
        self.is_forfeit = parse_is_forfeit(d)
        self.is_bekermatch = parse_is_bekermatch(d)


def parse_datetime(d):
    """ Used to parse date and time of match.
    """
    yyyy, mm, dd = parse_date(d.get("datumString", ""))
    hrs, mns = parse_time(d.get("beginTijd", ""))
    return TIMEZONE.localize(datetime(yyyy, mm, dd, hrs, mns))


@use_fallback_value(DEFAULT_DATE)
def parse_date(string_value):
    """ Used to parse date on which match is played.
    """
    dd, mm, yyyy = string_value.split("-")
    return int(yyyy), int(mm), int(dd)


@use_fallback_value(DEFAULT_TIME)
def parse_time(string_value):
    """ Used to parse time at which match is played.
    """
    hrs, mns = string_value.split(".")
    return int(hrs), int(mns)


@use_fallback_value("???")
def parse_location(d):
    """ Used to parse name of location where match is played.
    """
    return str(d.get("accNaam", ""))


@use_fallback_value("???")
def parse_home(d):
    """ Used to parse name of home team.
    """
    return str(d.get("tTNaam", ""))


@use_fallback_value("???")
def parse_visitor(d):
    """ Used to parse name of visiting team.
    """
    return str(d.get("tUNaam", ""))


@use_fallback_value(0)
def parse_home_score(d):
    """ Used to parse score of home team.
    """
    string_value = d.get("uitslag", "  0-  0")
    (h, _) = string_value.replace(" ", "").split("-")
    return int(h)


@use_fallback_value(0)
def parse_visitor_score(d):
    """ Used to parse score of visiting team.
    """
    string_value = d.get("uitslag", "  0-  0")
    (_, v) = string_value.replace(" ", "").split("-")
    return int(v)


@use_fallback_value(False)
def parse_is_forfeit(d):
    """ Used to parse whether or not one of the teams forfeited the match.
    """
    return bool("FOR" in d.get("uitslag", ""))


@use_fallback_value(False)
def parse_is_bekermatch(d):
    """ Used to parse whether or not a match is a cup match.
    """
    return bool("beker" in d.get("pouleNaam", "").lower())


@use_fallback_value("BVBL0000XXX++1")
def parse_home_guid_team(d):
    """ Used to parse GUID of team.
    """
    return str(d.get("tTGUID", "BVBL0000XXX  1")).replace(" ", "+")


@use_fallback_value("BVBL0000")
def parse_home_guid_club(d):
    """ Used to parse GUID of club.
    """
    return parse_home_guid_team(d)[:-6]


@use_fallback_value("BVBL0000XXX++1")
def parse_visitor_guid_team(d):
    """ Used to parse GUID of team.
    """
    return str(d.get("tUGUID", "BVBL0000XXX  1")).replace(" ", "+")


@use_fallback_value("BVBL0000")
def parse_visitor_guid_club(d):
    """ Used to parse GUID of club.
    """
    return parse_visitor_guid_team(d)[:-6]
