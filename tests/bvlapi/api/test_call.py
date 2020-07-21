#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for making API calls.

from unittest.mock import patch

import pytest

from bvlapi.api.call import call_api
from bvlapi.api.settings import API_BASE_URL
from bvlapi.common.exceptions import ApiCallFailed
from bvlapi.common.exceptions import BvlApiException


def test__api_call__success():
    """ Tests that JSON object is returned successfully when API call succeeds.
    """
    with patch("bvlapi.api.call.get_json") as mock_get:
        mock_get.return_value = {"success": True}
        url = API_BASE_URL + "TeamDetailByGuid?teamGuid=BVBL1328HSE++1"
        d = call_api(url)
        mock_get.assert_called_once_with(url)
        assert d["success"] is True


def test__api_call__failure():
    """ Tests that exception is raised when API call fails.
    """
    with patch("bvlapi.api.call.get_json") as mock_get:

        mock_get.side_effect = BvlApiException("sth went wrong")
        url = API_BASE_URL + "TeamDetailByGuid?teamGuid=BVBL1328HSE++1"
        with pytest.raises(ApiCallFailed):
            _ = call_api(url)
        mock_get.assert_called_once_with(url)
