#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains paths of files used by this package.

import os


def _build_filepath(filename):
    """ Used to construct filepath of local file.
    """
    this_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(this_dir, filename)


# filepath of file containing empty logo
NO_LOGO_JPG_FILEPATH = _build_filepath("no_logo.jpg")
