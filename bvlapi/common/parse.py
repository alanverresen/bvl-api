#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file contains functionality used to parse values.

import functools


def use_fallback_value(fallback_value):
    """ Parameterized function decorator that acts as a safety net for any
        value parsing activities. If any uncaught exception is raised during
        parsing, the fallback value is returned by the function.
    """
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            try:
                return_value = function(*args, **kwargs)
            except Exception:
                return_value = fallback_value
            return return_value
        return wrapper
    return decorator
