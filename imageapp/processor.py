from .imagemanipulator import ImageManipulator
from .inputprocessor import InputProcessor


class Processor:
    """Select the filter, apply, and then save the result.

    Args:
        filters: (dict of :py:mod:`str`
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
        :py:mod:`imageapp.inputprocessor.menu` to allow the user to choose the
        filter, apply the filter and save the result.

        Args:
            flag (:py:mod:`str`): The flag provided by the user.
            args_argparse (:py:mod:`list` of :py:mod:`str`): Arguments provided
                by the user.

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
            print('Error')
            exit(1)

        # If needed, some verifications about result struct can be here.

        print('\nImage file processed successfully!')
        self._save_result(result, file_name)

    def _save_result(self, result, file_name):
        for complement, image in result.items():
            name = self.im.gen_file_name(file_name, complement)
            print(f'Saving {name}...')
            self.im.write_image(image, name)

    def _apply_filter(self, function, image, *args, **kwargs):
        return function(image, *args, **kwargs)
