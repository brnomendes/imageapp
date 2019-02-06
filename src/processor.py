from .imagemanipulator import ImageManipulator
from .inputprocessor import InputProcessor


class Processor:

    def __init__(self, filters):
        self.filters = filters
        self.im = ImageManipulator()
        self.ip = InputProcessor()

    def start(self, flag, args):
        if not isinstance(args, list):
            args = [args]

        file_name = args[0]
        image = self.im.read_image(file_name)

        if flag == 'image':
            choice_flag, kwargs = self.ip.menu(self.filters, image.mode)
            result = self.filters[choice_flag]['function'](image, **kwargs)

        elif image.mode in self.filters[flag]['types']:
            result = self.filters[flag]['function'](image, *args[1:])

        else:
            print('Error')
            exit(1)

        print('\nImage file processed successfully!')
        self._save_result(result, file_name)

    def _save_result(self, result, file_name):
        for complement, image in result.items():
            name = self.im.gen_file_name(file_name, complement)
            print(f'Saving {name}...')
            self.im.write_image(image, name)
