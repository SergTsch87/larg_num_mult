import pytest
from ..src.core import multiply_str


def test_single_digit():
    assert multiply_str("3", "4") == "12"


def test_multi_by_digit():
    assert multiply_str("123", "3") == "369"