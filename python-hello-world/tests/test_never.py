"""This module is an example of skipping an entire module of pytest tests"""
import pytest

pytest.skip("Skipping this module for some reason", allow_module_level=True)


def test1():
    assert False
