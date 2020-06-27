#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains all exceptions raised by this package.


class BvlApiException(Exception):
    """ Base class of all exceptions raised by this package.
    """
    pass


class ApiCallFailed(BvlApiException):
    """ Raised when something goes wrong when calling API.
    """
    pass


class InvalidGuid(BvlApiException):
    """ Raised when an invalid GUID is given.
    """
    pass


class HttpRequestFailed(BvlApiException):
    """ Raised when an attempt to download a file failed.
    """
    pass


class HttpResponseBadStatusCode(BvlApiException):
    """ Raised when HTTP response has a bad status code.
    """
    pass


class HttpResponseInvalidJSON(BvlApiException):
    """ Raised when HTTP response's body is an invalid JSON response.
    """
    pass
