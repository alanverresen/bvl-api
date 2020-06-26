#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for retrieving information about competitions.

from bvlapi.guid.team import is_team_guid


def test_is_team_guid():
    """
    """
    assert is_team_guid("BVBL1328HSE++1")


def test_is_team_guid__false():
    """
    """
    assert not is_team_guid("not a guid")
