#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains functionality used to retrieve logo of a club.

from shutil import copy as copy_file

from bvlapi.common.download import download_file
from bvlapi.common.exceptions import FailedToDownloadFile
from bvlapi.common.exceptions import FailedToGetLogo
from bvlapi.common.exceptions import InvalidGuid
from bvlapi.common.exceptions import LogoInvalidFileExtension
from bvlapi.files import NO_LOGO_JPG_FILEPATH
from bvlapi.guid.club import is_club_guid

# A team's logo can be accessed using the following URL. However, not every
# team has an official log, and therefore, an attempt to download their logo
# will result in a 404 response.
LOGO_URL_TEMPLATE = "https://vblcb.wisseq.eu/vbldata/organisatie/{}_Small.jpg"


def get_club_logo(club_guid, filepath):
    """ Downloads logo of a basketball club with a given filename.

    :param str club_guid: GUID of a basketball club
    :param str filepath: filepath of logo image

    :raise InvalidGuid: given GUID is not a valid club GUID
    :raise FailedToDownloadLogo: failed to download an image
    """
    if not is_club_guid(club_guid):
        m = "'{}' is not a valid club GUID."
        raise InvalidGuid(m.format(club_guid))
    if not (filepath.endswith(".jpg") or filepath.endswith(".jpeg")):
        m = "file extension of '{}' should be '.jpg' or '.jpeg'."
        raise LogoInvalidFileExtension(m.format(filepath))
    try:
        download_file(filepath, LOGO_URL_TEMPLATE.format(club_guid))
    except FailedToDownloadFile:
        use_empty_logo(club_guid, filepath)


def use_empty_logo(club_guid, filepath):
    """ Attempts to provide an empty image as a club logo.

    :param str club_guid: GUID of a basketball club
    :param str filepath: filepath of logo image
    """
    try:
        copy_file(NO_LOGO_JPG_FILEPATH, filepath)
    except Exception as e:
        m = "Completely failed to provide logo for club with GUID '{}': {}"
        raise FailedToGetLogo(m.format(club_guid, e))
