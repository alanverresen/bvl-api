#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for making API calls.

from unittest.mock import patch

from bvlapi.api.team.detailByGuid import get_detail_by_guid
from bvlapi.api.team.matchesByGuid import get_matches_by_guid


def test_get_detail_by_guid():
    """ Tests that API is correctly called, and a response is returned.
    """
    with patch("bvlapi.api.team.detailByGuid.call_api") as mock_call:
        mock_call.return_value = []
        result = get_detail_by_guid("<team_guid>")
        mock_call.assert_called_with(
            "https://vblcb.wisseq.eu/VBLCB_WebService/data/"
            "TeamDetailByGuid?teamGuid=<team_guid>")
        assert result == []


def test_get_matches_by_guid():
    """
    """
    with patch("bvlapi.api.team.matchesByGuid.call_api") as mock_call:
        mock_call.return_value = []
        result = get_matches_by_guid("<team_guid>")
        mock_call.assert_called_with(
            "https://vblcb.wisseq.eu/VBLCB_WebService/data/"
            "TeamMatchesByGuid?teamGuid=<team_guid>")
        assert result == []
