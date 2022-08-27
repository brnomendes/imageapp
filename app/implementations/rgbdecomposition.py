def run(image):
    result = {}

    for channel, color in enumerate(["red", "green", "blue"]):
        image_color = _image_with_one_chanel(image.copy(), channel)
        result[color] = image_color

    return result


def _image_with_one_chanel(image, chanel_index):
    width, height = image.size

    for x in range(width):
        for y in range(height):
            pixel = list(image.getpixel((x, y)))
            for c, _ in enumerate(image.getbands()):
                if c != chanel_index:
                    pixel[c] = 0
            image.putpixel((x, y), tuple(pixel))

    return image
