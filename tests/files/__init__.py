#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Used to easily access file contents from tests.

import os


def read_file(filename):
    """ Stores content from a file in this directory in variable.
    """
    this_dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(this_dir, filename)
    with open(filepath, "r") as f:
        s = f.read()
    return s


def read_bytes(filename):
    """ Stores content from a file in this directory in variable.
    """
    this_dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(this_dir, filename)
    with open(filepath, "rb") as f:
        s = f.read()
    return s


# Contains representative example of API response when trying to retrieve
# information about a club.
CLUB_DETAIL_BY_GUID_JSON = read_file("clubDetailByGuid.json")


# Contains representative example of API response when trying to retrieve
# information about team and its competitions.
TEAM_DETAIL_BY_GUID_JSON = read_file("teamDetailByGuid.json")

# Contains representative example of API response when trying to retrieve
# information about team's games.
TEAM_MATCHES_BY_GUID = read_file("teamMatchesByGuid.json")

# Expected result when a team's logo is not found.
LOGO_NOT_FOUND_JPG = read_bytes("logo_not_found.jpg")
