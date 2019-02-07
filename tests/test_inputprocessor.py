import pytest
from unittest import mock

from imageapp.inputprocessor import InputProcessor
from imageapp.filterregister import Filter


@pytest.fixture
def input_processor():
    return InputProcessor()


def test_get_filter_args(input_processor):
    filter = Filter(None, None, None, None)
    filter.args = ['image', 'x', 'y', 'z']

    with mock.patch('builtins.input', side_effect=['01', '02', 5]):
        kwargs = input_processor._get_filter_args(filter)
        assert kwargs == {'x': '01', 'y': '02', 'z': 5}


def test_choice_a_filter(input_processor):
    f1 = Filter(None, 'F1', None, None)
    f2 = Filter(None, 'F2', None, None)

    possibles = [f1, f2]

    with mock.patch('builtins.input', side_effect=[2]):
        index = input_processor._choice_a_filter(possibles)
        assert possibles[index].name == 'F2'
