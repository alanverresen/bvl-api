#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains functionality to check validity of a GUID.

import re


def is_team_guid(guid):
    """ Checks that a given GUID is a valid team GUID.

    :param str guid: a GUID

    :rtype: bool
    :return: is GUID a valid team GUID?
    """
    return re.match(r"^BVBL[0-9]{4}...\+\+[0-9]$", guid)
