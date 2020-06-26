#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for retrieving information about competitions.

from bvlapi.guid.club import is_club_guid


def test_is_club_guid():
    """
    """
    assert is_club_guid("BVBL1328")


def test_is_club_guid__false():
    """
    """
    assert not is_club_guid("not a guid")
