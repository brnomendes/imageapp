import argparse


from .processor import Processor
from .filters import register


class ImageApp:
    """Application entry point.

    This module is responsible for starting the argparse and obtaining the user
    arguments for executing the application.
    """

    def start(self):
        """Create argparse and start :py:mod:`imageapp.processor.Processor`.

        The argparse is started with the --image argument, which displays to
        the user a menu with the filters available for the input image.

        For each filter registered in :py:mod:`imageapp.filters`, a new argument
        is added to argparse.
        """
        parser = argparse.ArgumentParser(
            description='An app to process images.')

        group = parser.add_mutually_exclusive_group(required=True)

        group.add_argument('--image', metavar='image',
                           help='Shows the available filters for the input image.')

        for flag in register.filters:
            filter_args = register.filters[flag].args
            group.add_argument(f'--{flag}', metavar=tuple(filter_args),
                               nargs=len(filter_args),
                               help=register.filters[flag].help)

        for flag, args_argparse in vars(parser.parse_args()).items():
            if args_argparse:
                if not isinstance(args_argparse, list):
                    args_argparse = [args_argparse]
                Processor(register.filters).start(flag, args_argparse)
