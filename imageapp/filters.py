from .implementations import blurfilter, rgbdecomposition, rotateimage
from .filterregister import register


@register(name='Blur', types=['RGB'], help='Blur Help')
def blur(image, radius, weight):
    return blurfilter.run(image, int(radius), int(weight))


@register(name='RGB Split', types=['RGB'])
def rgb(image):
    return rgbdecomposition.run(image)


@register(name='Rotate Image', types=['RGB'], help='Rotates the input image clockwise according to the angle.')
def rotate(image, angle_degrees):
    return rotateimage.run(image, int(angle_degrees))
