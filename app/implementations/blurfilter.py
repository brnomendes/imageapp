def run(image, radius, weight):
    image = convolution(image.copy(), image, radius, weight)

    return {f"blur-radius{radius}-weight{weight}": image}


def convolution(image, original_image, radius, weight):
    width, height = image.size

    for x in range(width):
        for y in range(height):
            pixel = list(image.getpixel((x, y)))
            for c, _ in enumerate(image.getbands()):
                pixel_sum = 0
                count = 0
                for j in range(-radius, radius + 1):
                    for k in range(-radius, radius + 1):
                        if _pixel_exists(x + j, y + k, width, height):
                            value = original_image.getpixel((x + j, y + k))[c]
                            if j == 0 and k == 0:
                                pixel_sum += (value * weight)
                                count = count + weight
                            else:
                                pixel_sum += value
                                count = count + 1
                pixel[c] = int(pixel_sum / count)
            image.putpixel((x, y), tuple(pixel))

    return image


def _pixel_exists(x, y, width, height):
    if x < 0 or y < 0:
        return False
    elif x >= width or y >= height:
        return False
    else:
        return True
