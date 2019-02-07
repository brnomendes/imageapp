from PIL import ImageDraw


def run(image, x, y, text_to_put, color):
    draw = ImageDraw.Draw(image)

    draw.text((x, y), text_to_put, color)
    return {'text': image}
