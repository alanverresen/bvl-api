#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains class used to hold information about one's standing in competition.

from bvlapi.data.parse import use_fallback_value


class CompetitionStanding:
    """ Used to hold information about one's standing in a competition.

    :ivar int rank: rank of team within competition
    :ivar str name: name of team
    :ivar str guid_team: GUID of team
    :ivar str guid_club: GUID of club
    :ivar int rank_points: amount of points that determine a team's standing
    :ivar int games_played: amount of games played by team
    :ivar int games_wins: amount of games won by team
    :ivar int games_losses: amount of games lost by team
    :ivar int games_draws: amount of games played by team that ended in a draw
    :ivar int points_scored: amount of points scored by team
    :ivar int points_conceded: amount of points conceded by team
    :ivar str comment: an optional comment
    """

    def __init__(self, r):
        """ Initializes a new instance based on given information.

        :param dict r: contains information about current standing
        """
        self.rank = parse_rank(r)
        self.name = parse_name(r)
        self.guid_team = parse_team_guid(r)
        self.guid_club = parse_club_guid(r)
        self.games_played = parse_games_played(r)
        self.games_wins = parse_games_wins(r)
        self.games_losses = parse_games_losses(r)
        self.games_draws = parse_games_draws(r)
        self.rank_points = parse_rank_points(r)
        self.points_scored = parse_points_scored(r)
        self.points_conceded = parse_goals_conceded(r)
        self.comment = parse_comment(r)


@use_fallback_value(0)
def parse_rank(r):
    """ Used to parse the rank of one's standing.
    """
    return int(r.get("rangNr", 0))


@use_fallback_value("???")
def parse_name(r):
    """ Used to parse the name of a team.
    """
    return str(r.get("naam", ""))


@use_fallback_value("BVBL0000XXX++1")
def parse_team_guid(r):
    """ Used to parse GUID of team.
    """
    return str(r.get("guid", "BVBL0000XXX  1")).replace(" ", "+")


@use_fallback_value("BVBL0000")
def parse_club_guid(r):
    """ Used to parse GUID of club.
    """
    return parse_team_guid(r)[:-6]


@use_fallback_value(0)
def parse_games_played(r):
    """ Used to parse the amount of games played by a team.
    """
    return int(r.get("wedAant", 0))


@use_fallback_value(0)
def parse_games_wins(r):
    """ Used to parse the amount of games won by a team.
    """
    return int(r.get("wedWinst", 0))


@use_fallback_value(0)
def parse_games_losses(r):
    """ Used to parse the amount of games lost by a team.
    """
    return int(r.get("wedVerloren", 0))


@use_fallback_value(0)
def parse_games_draws(r):
    """ Used to parse the amount of games that ended in a draw.
    """
    return int(r.get("wedGelijk", 0))


@use_fallback_value(0)
def parse_rank_points(r):
    """ Used to parse the amount of points collected based on one's W/L/D.
    """
    return int(r.get("wedPunt", 0))


@use_fallback_value(0)
def parse_points_scored(r):
    """ Used to parse the amount of points scored by a team.
    """
    return int(r.get("ptVoor", 0))


@use_fallback_value(0)
def parse_goals_conceded(r):
    """ Used to parse the amount of points conceded by a team.
    """
    return int(r.get("ptTegen", 0))


@use_fallback_value("???")
def parse_comment(r):
    """ Used to parse the extra comment.
    """
    return str(r.get("opmerk", ""))
