from .imagemanipulator import ImageManipulator
from .inputprocessor import InputProcessor


class Processor:
    """Select the filter, apply, and then save the result.

    This module is responsible for analyzing the user's arguments and deciding
    to apply the filter or display the menu. Then applies the filter on the
    image with the received arguments and saves the result images.

    Args:
        filters: (:obj:`dict` of :obj:`str:`
            :py:mod:`imageapp.filterregister.Filter`) -- List of registered
            filters.
    """

    def __init__(self, filters):
        self.filters = filters
        self.im = ImageManipulator()
        self.ip = InputProcessor()

    def start(self, flag, args_argparse):
        """From the user's arguments, performs the necessary functions.

        Read the image, if necessary, require the
        :py:mod:`imageapp.inputprocessor.menu` to allow the user to choose a
        filter, then apply the filter and save the result.

        Args:
            flag (:obj:`str`): The flag provided by the user.
            args_argparse (:obj:`list` of :obj:`str`): Arguments provided by
                the user.

        """
        file_name = args_argparse[0]
        image = self.im.read_image(file_name)

        if flag == 'image':
            filter, kwargs = self.ip.menu(self.filters, image.mode)
            print('Processing...')
            result = self._apply_filter(filter.function, image, **kwargs)

        elif image.mode in self.filters[flag].types:
            print('Processing...')
            result = self._apply_filter(self.filters[flag].function, image, *args_argparse[1:])

        else:
            print('Image mode not compatible with the chosen filter.')
            exit(1)

        # If needed, some verifications about result struct can be here.

        print('\nImage file processed successfully!')
        self._save_result(result, file_name)

    def _save_result(self, result, file_name):
        """Saves the results applied by the filter.

        For each result, a filename of the result image is generated, and then
        it's written.

        Args:
            result (:obj:`dict` of :obj:`str:` :py:mod:`PIL.Image`):
                Dictionary with result images.
            file_name (:obj:`str`): File name of the original image.
        """
        for complement, image in result.items():
            name = self.im.gen_file_name(file_name, complement)
            print(f'Saving {name}...')
            self.im.write_image(image, name)

    def _apply_filter(self, function, image, *args, **kwargs):
        """Apply a filter to an image.

        It receives the image and filter function with the arguments, applies
        the filter and returns the result images.

        Args:
            function (:obj:`function`): Function that applies the filter.
            image (:py:mod:`PIL.Image`): Image where the filter will be applied.
            *args (:obj:`list` of :obj:`str`): Arguments for the filter.
            **kwargs (:obj:`dict` of :obj:`str:`:obj:`str`): Arguments for the
                filter.

        Returns:
            (:obj:`dict` of :obj:`str:` :py:mod:`PIL.Image`): Dictionary with
            result images.
        """
        return function(image, *args, **kwargs)
