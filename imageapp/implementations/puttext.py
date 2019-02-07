from PIL import ImageDraw


def run(image, x, y, text, color):
    draw = ImageDraw.Draw(image)

    draw.text((x, y), text, color)
    return {'text': image}
