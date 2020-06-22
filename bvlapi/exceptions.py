#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file contains all exceptions raised by this package.


class BvlApiException(Exception):
    """ Base class of all exceptions raised by this package.
    """
    pass


class ApiCallFailed(BvlApiException):
    """ Raised when something goes wrong when calling API.
    """
    pass
