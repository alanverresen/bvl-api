#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for retrieving club logos.

from os.path import isfile
from os.path import join as path_join
from tempfile import TemporaryDirectory
from unittest.mock import patch

import pytest

from bvlapi.common.exceptions import FailedToDownloadFile
from bvlapi.common.exceptions import FailedToGetLogo
from bvlapi.common.exceptions import InvalidGuid
from bvlapi.common.exceptions import LogoInvalidFileExtension
from bvlapi.data.logos.get import get_club_logo


def test__get_club_logo__success__logo_found():
    """ Test that a logo can be successfully downloaded.
    """
    with patch("bvlapi.data.logos.get.download_file") as mock_dl_file:
        get_club_logo("BVBL1234", "/path/to/file.jpg")
        mock_dl_file.assert_called_once_with(
            "/path/to/file.jpg",
            "https://vblcb.wisseq.eu/vbldata/organisatie/BVBL1234_Small.jpg")


def test__get_club_logo__success__no_logo_found():
    """ Test that an 'no logo' image is provided if no logo was found.
    """
    with patch("bvlapi.data.logos.get.download_file") as mock_dl_file, \
            TemporaryDirectory() as temp_dir:
        mock_dl_file.side_effect = FailedToDownloadFile("oops")
        filepath = path_join(temp_dir, "myLogo.jpg")
        get_club_logo("BVBL1234", filepath)
        assert isfile(filepath)


def test__get_club_logo__invalid_guid():
    """ Test that an exception is raised when given GUID is invalid.
    """
    with pytest.raises(InvalidGuid):
        get_club_logo("invalid guid", "/path/to/file.jpg")


def test__get_club_logo__invalid_file_extension():
    """ Test that an exception is raised when the file extension is not valid.
    """
    with pytest.raises(LogoInvalidFileExtension):
        get_club_logo("BVBL1234", "/path/to/file.png")


def test__get_club_logo__complete_failure():
    """ Test that an exception is raised when providing a logo completely fails
        in every way:
            - try to download logo -> download fails, no logo
            - try to use empty logo -> sth went wrong
    """
    with patch("bvlapi.data.logos.get.download_file") as mock_dl_file, \
            patch("bvlapi.data.logos.get.copy_file") as mock_copy_file:
        mock_dl_file.side_effect = FailedToDownloadFile("oops!")
        mock_copy_file.side_effect = Exception("oops again!")
        with pytest.raises(FailedToGetLogo):
            get_club_logo("BVBL1234", "/path/to/file.jpg")
