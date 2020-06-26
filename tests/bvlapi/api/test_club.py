#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for making API calls.

import pytest

from unittest.mock import patch

from bvlapi.api.club.detailByGuid import get_detail_by_guid
from bvlapi.common.exceptions import InvalidGuid


def test_get_detail_by_guid():
    """ Tests that API is correctly called, and a response is returned.
    """
    with patch("bvlapi.api.club.detailByGuid.call_api") as mock_call:
        mock_call.return_value = []
        result = get_detail_by_guid("BVBL1432")
        mock_call.assert_called_with(
            "https://vblcb.wisseq.eu/VBLCB_WebService/data/"
            "OrgDetailByGuid?issguid=BVBL1432")
        assert result == []


def test_get_detail_by_guid__invalid_guid():
    """ Tests that exception is raised when an invalid club GUID is provided.
    """
    with pytest.raises(InvalidGuid):
        get_detail_by_guid("not a guid")
