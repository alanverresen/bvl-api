#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for retrieving information about matches being played by team.

import json

from datetime import datetime
from unittest.mock import patch

from bvlapi.api.matches import get_matches
from bvlapi.common.settings import TIMEZONE as tz

from tests.files import GAMES_JSON


def test_get_matches__empty():
    """ Try to retrieve and parse information about a team's matches, but
        no information is given.
    """
    with patch("bvlapi.api.matches.get.call_api") as call_mock:
        call_mock.return_value = json.loads("[]")
        matches = get_matches("123")
        assert len(matches) == 0


def test_get_matches():
    """ Try to retrieve and parse information about a team's matches.
    """
    with patch("bvlapi.api.matches.get.call_api") as call_mock:
        call_mock.return_value = json.loads(GAMES_JSON)
        matches = get_matches("123")
        assert len(matches) == 1
        assert matches[0].home_team == "Basket Willebroek HSE C"
        assert matches[0].home_score == 95
        assert matches[0].visiting_team == "BBC Floorcouture Zoersel HSE A"
        assert matches[0].visiting_score == 61
        assert matches[0].datetime == datetime(2019, 10, 5, 18, 15, tzinfo=tz)
        assert matches[0].location == "Sporthal de Schalk"
        assert not matches[0].is_forfait
        assert matches[0].is_bekermatch
