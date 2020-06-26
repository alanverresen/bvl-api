#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for making API calls.

import pytest

from unittest.mock import patch

from bvlapi.api.team.detailByGuid import get_detail_by_guid
from bvlapi.api.team.matchesByGuid import get_matches_by_guid
from bvlapi.common.exceptions import InvalidGuid


def test_get_detail_by_guid():
    """ Tests that API is correctly called, and a response is returned.
    """
    with patch("bvlapi.api.team.detailByGuid.call_api") as mock_call:
        mock_call.return_value = []
        result = get_detail_by_guid("BVBL1328HSE++1")
        mock_call.assert_called_with(
            "https://vblcb.wisseq.eu/VBLCB_WebService/data/"
            "TeamDetailByGuid?teamGuid=BVBL1328HSE++1")
        assert result == []


def test_get_detail_by_guid__invalid_guid():
    """ Tests that API is correctly called, and a response is returned.
    """
    with pytest.raises(InvalidGuid):
        _ = get_detail_by_guid("not a guid")


def test_get_matches_by_guid():
    """ Tests that exception is raised when an invalid team GUID is provided.
    """
    with patch("bvlapi.api.team.matchesByGuid.call_api") as mock_call:
        mock_call.return_value = []
        result = get_matches_by_guid("BVBL1328HSE++1")
        mock_call.assert_called_with(
            "https://vblcb.wisseq.eu/VBLCB_WebService/data/"
            "TeamMatchesByGuid?teamGuid=BVBL1328HSE++1")
        assert result == []


def test_get_matches_by_guid__invalid_guid():
    """ Tests that exception is raised when an invalid team GUID is provided.
    """
    with pytest.raises(InvalidGuid):
        _ = get_matches_by_guid("not a guid")
