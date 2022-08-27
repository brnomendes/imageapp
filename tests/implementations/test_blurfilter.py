import numpy as np
import pytest

from PIL import Image
from app.implementations import blurfilter


@pytest.fixture
def image2_radius1_weight1():
    data = [[[6, 6, 6], [6, 6, 6]], [[6, 6, 6], [6, 6, 6]]]
    return Image.fromarray(np.array(data, dtype=np.uint8), mode='RGB')


def test_convolution_radius1_weight1(image2, image2_radius1_weight1, compare_images):
    result_image = blurfilter.convolution(image2.copy(), image2, 1, 1)

    assert compare_images(result_image, image2_radius1_weight1)


def test_convolution_radius5_weight5(image2, compare_images):
    result_image = blurfilter.convolution(image2.copy(), image2, 5, 5)

    data = [[[5, 5, 5], [6, 6, 6]], [[6, 6, 6], [7, 7, 7]]]
    image_blur = Image.fromarray(np.array(data, dtype=np.uint8), mode='RGB')

    assert compare_images(result_image, image_blur)


def test_pixel_exists():
    assert blurfilter._pixel_exists(0, 4, 5, 5) is True


def test_pixel_exists_negative():
    assert blurfilter._pixel_exists(-1, 4, 5, 5) is False
    assert blurfilter._pixel_exists(4, -1, 5, 5) is False


def test_pixel_exists_overflow():
    assert blurfilter._pixel_exists(0, 4, 4, 4) is False
    assert blurfilter._pixel_exists(4, 0, 4, 4) is False


def test_blurfilter(image2, image2_radius1_weight1, compare_images):
    result = blurfilter.run(image2, 1, 1)
    assert 'blur-radius1-weight1' in result
    assert compare_images(result['blur-radius1-weight1'], image2_radius1_weight1)
