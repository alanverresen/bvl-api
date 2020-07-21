#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for retrieving information about matches being played by team.

import json

from datetime import datetime
from unittest.mock import patch

from bvlapi.data.matches import get_matches
from bvlapi.data.settings import TIMEZONE as tz

from tests.files import TEAM_MATCHES_BY_GUID


def test_get_matches__empty():
    """ Try to retrieve and parse information about a team's matches, but
        no information is given.
    """
    with patch("bvlapi.data.matches.get.get_matches_by_guid") as call_mock:
        call_mock.return_value = json.loads("[]")
        matches = get_matches("123")
        assert len(matches) == 0


def test_get_matches():
    """ Try to retrieve and parse information about a team's matches.
    """
    with patch("bvlapi.data.matches.get.get_matches_by_guid") as call_mock:
        call_mock.return_value = json.loads(TEAM_MATCHES_BY_GUID)
        matches = get_matches("123")
        assert len(matches) == 1

        match = matches[0]
        assert match.home_team == "Basket Willebroek HSE C"
        assert match.home_score == 95
        assert match.home_guid_team == "BVBL1173HSE++3"
        assert match.home_guid_club == "BVBL1173"
        assert match.visiting_team == "BBC Floorcouture Zoersel HSE A"
        assert match.visiting_score == 61
        assert match.visiting_guid_team == "BVBL1328HSE++1"
        assert match.visiting_guid_club == "BVBL1328"
        assert match.datetime == tz.localize(datetime(2019, 10, 5, 18, 15))
        assert match.location == "Sporthal de Schalk"
        assert not match.is_forfeit
        assert match.is_bekermatch
