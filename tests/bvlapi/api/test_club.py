#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for making API calls to retrieve information about club.

import pytest

from unittest.mock import patch

from bvlapi.api.club.detailByGuid import get_detail_by_guid
from bvlapi.api.settings import API_BASE_URL
from bvlapi.common.exceptions import InvalidGuid


def test__get_detail_by_guid():
    """ Tests that API is correctly called, and a response is returned.
    """
    with patch("bvlapi.api.club.detailByGuid.call_api") as mock_call:
        mock_call.return_value = []
        result = get_detail_by_guid("BVBL1432")
        mock_call.assert_called_with(
            API_BASE_URL + "OrgDetailByGuid?issguid=BVBL1432")
        assert result == []


def test__get_detail_by_guid__invalid_guid():
    """ Tests that exception is raised when an invalid club GUID is provided.
    """
    with patch("bvlapi.api.club.detailByGuid.call_api") as mock_call:
        with pytest.raises(InvalidGuid):
            get_detail_by_guid("<NOT A CLUB GUID>")
        mock_call.assert_not_called()
