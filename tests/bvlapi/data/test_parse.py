#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for making API calls.

from bvlapi.data.parse import use_fallback_value


@use_fallback_value(7)
def parse_int_value(value):
    """ Parses string that is expected to be an integer.
    """
    return int(value)


def test_decorator__expected_value():
    """ Tests that decorator returns proper value when parsing succeeds.
    """
    assert parse_int_value("123") == 123


def test_decorator__bad_value():
    """ Tests that decorator returns fallback value when parsing fails.
    """
    assert parse_int_value("N/A") == 7
