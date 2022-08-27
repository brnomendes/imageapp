from PIL import Image
from app.implementations import rgbdecomposition


def test_image_with_one_chanel(image, compare_images):
    image_result = rgbdecomposition._image_with_one_chanel(image, 0)
    image_with_one_chanel = Image.new('RGB', (2, 2), color=(10, 0, 0))

    assert compare_images(image_result, image_with_one_chanel)


def test_rgbdecomposition(image, compare_images):
    result = rgbdecomposition.run(image)
    for complement, image_result in result.items():
        if complement == 'red':
            color = (10, 0, 0)
        elif complement == 'green':
            color = (0, 20, 0)
        elif complement == 'blue':
            color = (0, 0, 30)

        image_with_one_chanel = Image.new('RGB', (2, 2), color=color)
        assert compare_images(image_result, image_with_one_chanel)
