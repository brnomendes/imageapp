import pytest
from imageapp.imagemanipulator import ImageManipulator


@pytest.fixture
def img_manipulator():
    return ImageManipulator()


def test_gen_file_name(img_manipulator):
    assert img_manipulator.gen_file_name('/x/y/test.gen.jpg', 'cpl') == '/x/y/test.gen-cpl.jpg'
