#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for retrieving information about a club's teams.

import json

from unittest.mock import patch

from bvlapi.data.teams.get import get_teams

from tests.files import CLUB_DETAIL_BY_GUID_JSON


def test_get_teams__empty():
    """ Tests that an empty list is returned when club is not found.
    """
    with patch("bvlapi.data.teams.get.get_detail_by_guid") as call_mock:
        call_mock.return_value = []
        teams = get_teams("BVBL1234")
        assert len(teams) == 0


def test_get_teams():
    """ Tests that a list of teams is returned when club is found.
    """
    with patch("bvlapi.data.teams.get.get_detail_by_guid") as call_mock:
        call_mock.return_value = json.loads(CLUB_DETAIL_BY_GUID_JSON)
        teams = get_teams("BVBL1234")
        assert len(teams) == 27
        assert teams[3].name == "Antwerp Giants J18 B"
        assert teams[3].guid == "BVBL1004J18++2"
