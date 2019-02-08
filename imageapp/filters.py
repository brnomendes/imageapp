from .implementations import blurfilter, rgbdecomposition, rotateimage
from .filterregister import register


@register(name='Blur', types=['RGB'])
def blur(image, radius, weight):
    """This filter applies a blur to an image.

    Args:
        image (:py:mod:`PIL.Image`): Image to be applied filter.
        radius (:obj:`str`): Radius to the convolution window.
        weight (:obj:`str`): Weight of the central pixel for the convolution.
    """
    return blurfilter.run(image, int(radius), int(weight))


@register(name='RGB Split', types=['RGB'])
def rgb(image):
    """Decomposes an RGB image into three images, each with values on only
    one channel.

    Args:
        image (:py:mod:`PIL.Image`): Image to be applied filter.
    """
    return rgbdecomposition.run(image)


@register(name='Rotate Image', types=['RGB'], help='Rotates the input image clockwise according to the angle.')
def rotate(image, angle_degrees):
    """Rotates the input image clockwise according to the angle.

    Args:
        image (:py:mod:`PIL.Image`): Image to be applied filter.
        angle_degrees (:obj:`str`): Angle in degrees for rotation.
    """
    return rotateimage.run(image, int(angle_degrees))
