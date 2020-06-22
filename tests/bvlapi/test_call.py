#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for making API calls.

import pytest

from unittest.mock import patch
from requests.exceptions import HTTPError
from requests.exceptions import RequestException

from bvlapi.call import call_api
from bvlapi.exceptions import ApiCallFailed


class ResponseStub:
    """ A stub object used to replace the Response returned by requests.get().
    """

    def __init__(self, text="", bad_status=False):
        """ Initializes a new instance.

        :param str text: content of HTTP response (JSON string)
        :param bool bad_status: should exception for bad status code be raised?
        """
        self.text = text
        self.bad_status = bad_status

    def raise_for_status(self):
        """ Raises an exception when response has a "bad" status code.
        """
        if self.bad_status:
            raise HTTPError()


def test__successful_request():
    """ Executes test where a successful request.
    """
    with patch("bvlapi.call.requests.get") as mock_get:
        mock_get.return_value = ResponseStub(text="{ \"success\": true }")
        d = call_api("my://url")
        assert d["success"] is True


def test__request_failed():
    """ Tests that exception is raised when request fails (e.g. times out).
    """
    with patch("bvlapi.call.requests.get") as mock_get:
        mock_get.side_effect = RequestException("sth went wrong")
        with pytest.raises(ApiCallFailed):
            _ = call_api("my://url")


def test__bad_status_code():
    """ Tests that exception is raised when response has bad status code.
    """
    with patch("bvlapi.call.requests.get") as mock_get:
        mock_get.return_value = ResponseStub(bad_status=True)
        with pytest.raises(ApiCallFailed):
            _ = call_api("my://url")


def test__bad_json():
    """ Tests that exception is raised when response is malformed JSON object.
    """
    with patch("bvlapi.call.requests.get") as mock_get:
        mock_get.return_value = ResponseStub(text="{ \"bad JSON")
        with pytest.raises(ApiCallFailed):
            _ = call_api("my://url")
