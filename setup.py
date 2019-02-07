from setuptools import setup, find_packages

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
