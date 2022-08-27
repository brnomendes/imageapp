import pytest

from app.filterregister import Filter, FilterRegister


@pytest.fixture
def filter_register():
    return FilterRegister()


@pytest.fixture
def register(filter_register):
    return filter_register.get_register()


@pytest.fixture
def filters(register):
    @register(name="Filter", types=["RGB"], help="Some Help")
    def sample_filter(image, x, y, z):
        pass

    return register.filters


def test_register_filter(filters):
    assert len(filters) == 1
    assert "sample_filter" in filters
    assert isinstance(filters["sample_filter"], Filter)


def test_register_filter_flag(filters):
    assert filters["sample_filter"].flag == "sample_filter"


def test_register_filter_name(filters):
    assert filters["sample_filter"].name == "Filter"


def test_register_filter_types(filters):
    assert filters["sample_filter"].types == ["RGB"]


def test_register_filter_help(filters):
    assert filters["sample_filter"].help == "Some Help"


def test_register_filter_args(filters):
    assert filters["sample_filter"].args == ["image", "x", "y", "z"]
