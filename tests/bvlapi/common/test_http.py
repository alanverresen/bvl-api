#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for making HTTP requests to retrieve resources.

import unittest.mock as mock

import pytest
from requests.exceptions import HTTPError
from requests.exceptions import RequestException

from bvlapi.common.exceptions import HttpRequestFailed
from bvlapi.common.exceptions import HttpResponseBadStatusCode
from bvlapi.common.exceptions import HttpResponseInvalidJSON
from bvlapi.common.http import get_bytes
from bvlapi.common.http import get_json
from bvlapi.common.http import get_text


class ResponseStub:
    """ A stub object used to replace the Response returned by requests.get().
    """

    def __init__(self, *, bad_status=False, bad_json=False, text=None,
                 json=None, byte=None):
        """ Initializes a new instance.
        """
        self.bad_status = bad_status
        self.bad_json = bad_json
        if text:
            self.text = text
        if json:
            self._json = json
        if byte:
            self.content = byte

    def json(self):
        """ Raises an exception if JSON object is bad.
        """
        if self.bad_json:
            raise ValueError
        return self._json

    def raise_for_status(self):
        """ Raises an exception when response has a "bad" status code.
        """
        if self.bad_status:
            raise HTTPError()


def test__bytes__successful_request():
    """ Tests that a string of bytes is correctly retrieved.
    """
    with mock.patch("bvlapi.common.http.requests.get") as mock_get:
        mock_get.return_value = ResponseStub(byte=b"success!")
        d = get_bytes("<this is a fake URL>")
        assert d == b"success!"


def test__bytes__request_failed():
    """ Tests that exception is raised when request fails (e.g. times out).
    """
    with mock.patch("bvlapi.common.http.requests.get") as mock_get:
        mock_get.side_effect = RequestException("sth went wrong")
        with pytest.raises(HttpRequestFailed):
            _ = get_bytes("<this is a fake URL>")


def test__bytes__bad_status_code():
    """ Tests that exception is raised when response has bad status code.
    """
    with mock.patch("bvlapi.common.http.requests.get") as mock_get:
        mock_get.return_value = ResponseStub(bad_status=True, byte=b"fail!")
        with pytest.raises(HttpResponseBadStatusCode):
            _ = get_bytes("<this is a fake URL>")


def test__text__successful_request():
    """ Tests that a string of bytes is correctly retrieved.
    """
    with mock.patch("bvlapi.common.http.requests.get") as mock_get:
        mock_get.return_value = ResponseStub(text="success!")
        d = get_text("<this is a fake URL>")
        assert d == "success!"


def test__text__request_failed():
    """ Tests that exception is raised when request fails (e.g. times out).
    """
    with mock.patch("bvlapi.common.http.requests.get") as mock_get:
        mock_get.side_effect = RequestException("sth went wrong")
        with pytest.raises(HttpRequestFailed):
            _ = get_text("<this is a fake URL>")


def test__text__bad_status_code():
    """ Tests that exception is raised when response has bad status code.
    """
    with mock.patch("bvlapi.common.http.requests.get") as mock_get:
        mock_get.return_value = ResponseStub(bad_status=True, text="fail!")
        with pytest.raises(HttpResponseBadStatusCode):
            _ = get_text("<this is a fake URL>")


def test__json__successful_request():
    """ Tests that a string of bytes is correctly retrieved.
    """
    with mock.patch("bvlapi.common.http.requests.get") as mock_get:
        mock_get.return_value = ResponseStub(json=[{"success": True}])
        d = get_json("<this is a fake URL>")
        assert d[0]["success"]


def test__json__request_failed():
    """ Tests that exception is raised when request fails (e.g. times out).
    """
    with mock.patch("bvlapi.common.http.requests.get") as mock_get:
        mock_get.side_effect = RequestException("sth went wrong")
        with pytest.raises(HttpRequestFailed):
            _ = get_json("<this is a fake URL>")


def test__json__bad_status_code():
    """ Tests that exception is raised when response has bad status code.
    """
    with mock.patch("bvlapi.common.http.requests.get") as mock_get:
        mock_get.return_value = ResponseStub(bad_status=True)
        with pytest.raises(HttpResponseBadStatusCode):
            _ = get_json("<this is a fake URL>")


def test__json__invalid_content():
    """ Tests that exception is raised when response contains invalid JSON.
    """
    with mock.patch("bvlapi.common.http.requests.get") as mock_get:
        mock_get.return_value = ResponseStub(bad_json=True)
        with pytest.raises(HttpResponseInvalidJSON):
            _ = get_json("<this is a fake URL>")
