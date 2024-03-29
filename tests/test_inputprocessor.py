from unittest import mock

import pytest

from app.filterregister import Filter
from app.inputprocessor import InputProcessor


@pytest.fixture
def input_processor():
    return InputProcessor()


def test_get_filter_args(input_processor):
    filter = Filter(None, None, None, None)
    filter.args = ["image", "x", "y", "z"]

    with mock.patch("builtins.input", side_effect=["ab", "02", 5]):
        kwargs = input_processor._get_filter_args(filter)
        assert kwargs == {"x": "ab", "y": "02", "z": 5}


def test_choice_a_filter(input_processor):
    f1 = Filter(None, "F1", None, None)
    f2 = Filter(None, "F2", None, None)

    possibles = [f1, f2]

    with mock.patch("builtins.input", side_effect=[1, 2]):
        filter = input_processor._choice_a_filter(possibles)
        assert filter.name == "F1"

        filter = input_processor._choice_a_filter(possibles)
        assert filter.name == "F2"
