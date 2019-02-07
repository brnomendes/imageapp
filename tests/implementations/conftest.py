import pytest
import numpy as np
from PIL import Image


@pytest.fixture
def image():
    data = [[[10, 20, 30], [10, 20, 30]], [[10, 20, 30], [10, 20, 30]]]
    array = np.array(data, dtype=np.uint8)

    return Image.fromarray(array, mode='RGB')


@pytest.fixture
def image2():
    data = [[[5, 5, 5], [6, 6, 6]], [[7, 7, 7], [8, 8, 8]]]
    array = np.array(data, dtype=np.uint8)

    return Image.fromarray(array, mode='RGB')


@pytest.fixture
def compare_images():
    def is_equals(image1, image2):
        return np.abs(np.array(image1) - np.array(image2)).sum() == 0
    return is_equals
