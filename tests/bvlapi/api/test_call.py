#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for making API calls.

from unittest.mock import patch

import pytest

from bvlapi.api.call import call_api
from bvlapi.common.exceptions import ApiCallFailed
from bvlapi.common.exceptions import BvlApiException


def test__api_call_success():
    """ Tests that JSON object is returned successfully.
    """
    with patch("bvlapi.api.call.get_json") as mock_get:
        mock_get.return_value = {"success": True}
        d = call_api("<this is a URL>")
        assert d["success"]


def test__api_call_failure():
    """ Tests that exception is raised when API call fails.
    """
    with patch("bvlapi.api.call.get_json") as mock_get:
        mock_get.side_effect = BvlApiException("sth went wrong")
        with pytest.raises(ApiCallFailed):
            _ = call_api("<this is a URL>")
