from PIL import Image


class ImageManipulator:

    def read_image(self, file_name):
        return Image.open(file_name)

    def write_image(self, image, name):
        image.save(name)

    def gen_file_name(self, file_name, complement):
        name_split = file_name.split('.')
        return f'{".".join(name_split[:-1])}-{complement}.{name_split[-1]}'
