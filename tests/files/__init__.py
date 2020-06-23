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


# source file of page containing hourly track chart (2020-02-18)
DETAIL_JSON = read_file("detail.json")

# example of an img (2020-02-17)
GAMES_JSON = read_file("games.json")
