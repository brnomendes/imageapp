from PIL import Image


class ImageManipulator:
    """Performs operations with image files.

    This module is responsible for reading and writing images, in addition
    to generating name of the result image files.
    """

    def read_image(self, file_name):
        """Returns an image according to the file path.

        Args:
            file_name (:obj:`str`): Path of the image to be read.

        Returns:
            :py:mod:`PIL.Image`: Image that was read.
        """
        return Image.open(file_name)

    def write_image(self, image, name):
        """Writes an image to the file.

        Args:
            image (:py:mod:`PIL.Image`): Image that will be saved.
            name (:obj:`str`): Path of the image file to be saved.
        """
        image.save(name)

    def gen_file_name(self, file_name, complement):
        """Add a complement to the file name of an image.

        For example, for the ``/paht/to/image.xyz`` image and ``result``
        complement, the name of the resulting image will be
        ``/paht/to/image-result.xyz``.

        Args:
            file_name (:obj:`str`): Original image file name.
            complement (:obj:`str`): Complement to be added to the file name
                of the image.

        Returns:
            :obj:`str`: File name of the image with the complement.
        """
        name_split = file_name.split(".")
        return f'{".".join(name_split[:-1])}-{complement}.{name_split[-1]}'
