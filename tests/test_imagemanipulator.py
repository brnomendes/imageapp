import pytest

from app.imagemanipulator import ImageManipulator


@pytest.fixture
def img_manipulator():
    return ImageManipulator()


def test_gen_file_name(img_manipulator):
    file_name = "/x/y/test.gen.jpg"
    complement = "filter"
    assert img_manipulator.gen_file_name(file_name, complement) == "/x/y/test.gen-filter.jpg"
