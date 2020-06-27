#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for downloading resources.

import os
import tempfile
import unittest.mock as mock

import pytest

from bvlapi.common.download import download_file
from bvlapi.common.exceptions import BvlApiException
from bvlapi.common.exceptions import FailedToDownloadFile


class BadFileObjectStub:
    """ Stub class used to act as a file that causes an Exception when being
        written to.
    """

    def write(self, s):
        """ Raises an exception.
        """
        raise Exception


def test__download_file__success_file_created():
    """ Tests that file is created after resource is downloaded.
    """
    with mock.patch("bvlapi.common.download.get_bytes") as mock_get_bytes, \
            tempfile.TemporaryDirectory() as temp_dir:
        mock_get_bytes.return_value = b"hi there!"
        filepath = os.path.join(temp_dir, "temp_file.txt")
        download_file(filepath, "<url>")
        assert os.path.isfile(filepath)


def test__download_file__success_file_written():
    """ Tests that bytes are written to file after being dl'ed.
    """
    with mock.patch("bvlapi.common.download.get_bytes") as mock_get_bytes, \
            tempfile.TemporaryDirectory() as temp_dir:
        mock_get_bytes.return_value = b"hi there!"
        fpath = os.path.join(temp_dir, "temp_file.txt")
        download_file(fpath, "<url>")
        with open(fpath, "rb") as f:
            r = f.read()
        assert r == b"hi there!"


def test__download_file__download_failed():
    """ Tests that exception is raised when downloading resource fails.
    """
    with mock.patch("bvlapi.common.download.get_bytes") as mock_get_bytes:
        mock_get_bytes.side_effect = BvlApiException("sth went wrong")
        with pytest.raises(FailedToDownloadFile):
            download_file("<filepath>", "<url>")


def test__download_file__writing_to_file_failed():
    """ Tests that exception is raised when writing bytes to file fails.
    """
    with mock.patch("bvlapi.common.download.get_bytes") as mock_get_bytes, \
            mock.patch("bvlapi.common.download.open") as mock_open:
        mock_get_bytes.return_value = b"hi there!"
        mock_open.return_value = BadFileObjectStub()
        with pytest.raises(FailedToDownloadFile):
            download_file("<filepath>", "<url>")
