import pytest
import numpy as np
from PIL import Image

from imageapp.implementations import rotateimage


def test_rotateimage(image2, compare_images):
    result = rotateimage.run(image2, 45)

    data = [[[6, 6, 6], [8, 8, 8]], [[7, 7, 7], [8, 8, 8]]]
    image_rotate = Image.fromarray(np.array(data, dtype=np.uint8), mode='RGB')

    assert 'rotate45' in result
    assert compare_images(result['rotate45'], image_rotate)
