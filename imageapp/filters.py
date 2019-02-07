from .implementations import blurfilter, rgbdecomposition, puttext
from .filterregister import register


@register(name='Blur', types=['RGB'], help='Blur Help')
def blur(image, radius, weight):
    return blurfilter.run(image, int(radius), int(weight))


@register(name='RGB Split', types=['RGB'])
def rgb(image):
    return rgbdecomposition.run(image)


@register(name='Put Text', types=['RGB'])
def text(image, x, y, text, color):
    return puttext.run(image, int(x), int(y), text, color)
