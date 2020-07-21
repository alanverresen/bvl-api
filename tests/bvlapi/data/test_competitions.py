#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for retrieving information about competitions.

import json

from unittest.mock import patch

from bvlapi.data.competitions import get_competitions

from tests.files import TEAM_DETAIL_BY_GUID_JSON


def test_get_competitions__empty():
    """ Try to retrieve and parse information about a team's competitions,
        but no information is found.
    """
    with patch("bvlapi.data.competitions.get.get_detail_by_guid") as call_mock:
        call_mock.return_value = json.loads("[]")
        competitions = get_competitions("123")
        assert len(competitions) == 0


def test_get_competitions():
    """ Try to retrieve and parse information about a team's competition.
    """
    with patch("bvlapi.data.competitions.get.get_detail_by_guid") as call_mock:
        call_mock.return_value = json.loads(TEAM_DETAIL_BY_GUID_JSON)
        competitions = get_competitions("123")
        assert len(competitions) == 1
        assert competitions[0].name == "Beker van Vlaanderen Heren Poule K"
        assert len(competitions[0].standings) == 5

        standing_0 = competitions[0].standings[0]
        assert standing_0.rank == 1
        assert standing_0.name == "Kortrijk Spurs HSE B"
        assert standing_0.games_played == 4
        assert standing_0.games_wins == 3
        assert standing_0.games_losses == 1
        assert standing_0.games_draws == 0
        assert standing_0.rank_points == 10
        assert standing_0.points_scored == 281
        assert standing_0.points_conceded == 262
        assert standing_0.comment == ""
        assert standing_0.guid_club == "BVBL1127"
        assert standing_0.guid_team == "BVBL1127HSE++2"

        standing_3 = competitions[0].standings[3]
        assert standing_3.rank == 4
        assert standing_3.name == "BC Cobras Schoten-Brasschaat HSE A"
        assert standing_3.games_played == 4
        assert standing_3.games_wins == 1
        assert standing_3.games_losses == 3
        assert standing_3.games_draws == 0
        assert standing_3.rank_points == 6
        assert standing_3.points_scored == 249
        assert standing_3.points_conceded == 286
        assert standing_3.comment == ""
        assert standing_3.guid_club == "BVBL1277"
        assert standing_3.guid_team == "BVBL1277HSE++1"
