#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def is_club_guid(guid):
    """
    """
    return re.match(r"^BVBL[0-9]{4}$", guid)
