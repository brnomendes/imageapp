import sys
from setuptools.command.test import test as TestCommand
from setuptools import setup, find_packages


class PyTest(TestCommand):
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ""

    def run_tests(self):
        import shlex
        import pytest

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


setup(
    name='imageapp',
    version=1.0,
    description='An app to process images.',
    author='Bruno Mendes',
    author_email='brunoms.50@gmail.com',
    python_requires='>=3.6.0',
    packages=find_packages(),
    install_requires=['Pillow', 'pytest'],
    include_package_data=True,
    license='MIT',
)
