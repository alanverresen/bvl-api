#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for making API calls to retrieve info about team.

import pytest

from unittest.mock import patch

from bvlapi.api.team.detailByGuid import get_detail_by_guid
from bvlapi.api.team.matchesByGuid import get_matches_by_guid
from bvlapi.api.settings import API_BASE_URL
from bvlapi.common.exceptions import InvalidGuid


def test__get_detail_by_guid():
    """ Tests that API is correctly called, and a response is returned.
    """
    with patch("bvlapi.api.team.detailByGuid.call_api") as mock_call:
        mock_call.return_value = []
        result = get_detail_by_guid("BVBL1328HSE++1")
        mock_call.assert_called_with(
            API_BASE_URL + "TeamDetailByGuid?teamGuid=BVBL1328HSE++1")
        assert result == []


def test__get_detail_by_guid__invalid_guid():
    """ Tests that exception is raised when an invalid team GUID is provided.
    """
    with patch("bvlapi.api.team.matchesByGuid.call_api") as mock_call:
        with pytest.raises(InvalidGuid):
            _ = get_detail_by_guid("<NOT A TEAM GUID>")
        mock_call.assert_not_called()


def test__get_matches_by_guid():
    """ Tests that API is correctly called, and a response is returned.
    """
    with patch("bvlapi.api.team.matchesByGuid.call_api") as mock_call:
        mock_call.return_value = []
        result = get_matches_by_guid("BVBL1328HSE++1")
        mock_call.assert_called_with(
            API_BASE_URL + "TeamMatchesByGuid?teamGuid=BVBL1328HSE++1")
        assert result == []


def test__get_matches_by_guid__invalid_guid():
    """ Tests that exception is raised when an invalid team GUID is provided.
    """
    with patch("bvlapi.api.team.matchesByGuid.call_api") as mock_call:
        with pytest.raises(InvalidGuid):
            _ = get_matches_by_guid("<NOT A TEAM GUID>")
        mock_call.assert_not_called()
