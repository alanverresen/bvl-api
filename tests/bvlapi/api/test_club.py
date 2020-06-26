#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for making API calls.

from unittest.mock import patch

from bvlapi.api.club.detailByGuid import get_detail_by_guid


def test_get_detail_by_guid():
    """ Tests that API is correctly called, and a response is returned.
    """
    with patch("bvlapi.api.club.detailByGuid.call_api") as mock_call:
        mock_call.return_value = []
        result = get_detail_by_guid("<club_guid>")
        mock_call.assert_called_with(
            "https://vblcb.wisseq.eu/VBLCB_WebService/data/"
            "OrgDetailByGuid?issguid=<club_guid>")
        assert result == []
