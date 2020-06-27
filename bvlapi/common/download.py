#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains functionality used to download and store a file locally.

from bvlapi.common.http import get_bytes

from bvlapi.common.exceptions import FailedToDownloadFile
from bvlapi.common.exceptions import BvlApiException


def download_file(filepath, url):
    """ Downloads resource with a given URL and stores it as a file.
    """
    try:
        o = get_bytes(url)
    except BvlApiException as e:
        msg = "Could not download resource at '{}' to '{}': {}"
        raise FailedToDownloadFile(msg.format(url, filepath, e))
    try:
        with open(filepath, "wb") as f:
            f.write(o)
    except Exception as e:
        msg = "Could not write resource at '{}' to '{}': {}"
        raise FailedToDownloadFile(msg.format(url, filepath, e))
