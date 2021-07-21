#!/usr/bin/env python
"""Tests for `iketm` package."""
# pylint: disable=redefined-outer-name

import pytest

from iketm.iketm import IkeTM


@pytest.fixture
def iketm():
    return IkeTM()


def test_tasks(iketm):
    try:
        iketm.tasks()
    except RuntimeError as err:
        assert False, f"commands should should never throw: {err}"
