#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for validating team GUIDs.

from bvlapi.guid.team import is_team_guid


def test_is_team_guid():
    """ Test that a valid team GUID is recognized.
    """
    assert is_team_guid("BVBL1328HSE++1")


def test_is_team_guid__false():
    """ Test that an invalid team GUID is recognized.
    """
    assert not is_team_guid("not a guid")
