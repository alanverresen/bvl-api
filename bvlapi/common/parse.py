#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains functionality used to parse values in a more robust way.

import functools


def use_fallback_value(fallback_value):
    """ Parameterized function decorator that acts as a safety net when
        parsing values. If any exception is raised while parsing a value,
        the exception is caught and the fallback value is returned by the
        decorated function.
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
