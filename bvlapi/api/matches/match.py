#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains functionality to retrieve information about calendar.

from bvlapi.common.settings import TIMEZONE

from datetime import datetime

from bvlapi.common.parse import use_fallback_value
from bvlapi.common.settings import DEFAULT_DATE
from bvlapi.common.settings import DEFAULT_TIME


class MatchInformation:
    """ Used to represent and organize information about a basketball match.
    """

    def __init__(self, d):
        """ Initializes a new instance based on information from dictionary
            containing data retrieved from API.
        """
        self.datetime = parse_datetime(d)
        self.location = parse_location(d)
        self.home_team = parse_home(d)
        self.home_score = parse_home_score(d)
        self.visiting_team = parse_visitor(d)
        self.visiting_score = parse_visitor_score(d)
        self.is_forfait = parse_is_forfeit(d)
        self.is_bekermatch = parse_is_bekermatch(d)


def parse_datetime(d):
    """ Used to parse date and time of match.
    """
    yyyy, mm, dd = parse_date(d.get("datumString", ""))
    hrs, mns = parse_time(d.get("beginTijd", ""))
    return datetime(yyyy, mm, dd, hrs, mns, tzinfo=TIMEZONE)


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
