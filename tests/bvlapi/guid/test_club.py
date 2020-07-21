#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for validating club GUIDs.

from bvlapi.guid.club import is_club_guid


def test_is_club_guid():
    """ Test that a valid club GUID is recognized.
    """
    assert is_club_guid("BVBL1328")


def test_is_club_guid__false():
    """ Test that an invalid club GUID is recognized.
    """
    assert not is_club_guid("not a guid")
