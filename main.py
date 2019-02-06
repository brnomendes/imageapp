import argparse


from src.processor import Processor
from src.filters import register


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Processes input images by applying filters.')
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('--image', metavar='image', help='Help')

    for flag in register.filters:
        filter_args = register.filters[flag].args
        group.add_argument(f'--{flag}', metavar=tuple(filter_args), nargs=len(filter_args), help=register.filters[flag].help)

    for flag, args_argparse in vars(parser.parse_args()).items():
        if args_argparse is not None:
            Processor(register.filters).start(flag, args_argparse)
