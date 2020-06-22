#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains a simple test that acts as a placeholder.

from bvlapi.add import add_two_numbers


def test_add_two_numbers():
    """ A test that should pass if setup is correct.
    """
    assert add_two_numbers(3, 7) == 10
