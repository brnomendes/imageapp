from .imagemanipulator import ImageManipulator
from .inputprocessor import InputProcessor


class Processor:

    def __init__(self, filters):
        self.filters = filters
        self.im = ImageManipulator()
        self.ip = InputProcessor()

    def start(self, flag, args_argparse):
        if not isinstance(args_argparse, list):
            args_argparse = [args_argparse]

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

        # Some verifications about result struct can be here

        print('\nImage file processed successfully!')
        self._save_result(result, file_name)

    def _save_result(self, result, file_name):
        for complement, image in result.items():
            name = self.im.gen_file_name(file_name, complement)
            print(f'Saving {name}...')
            self.im.write_image(image, name)

    def _apply_filter(self, function, image, *args, **kwargs):
        """ If needed some pre-processing in image """
        return function(image, *args, **kwargs)
