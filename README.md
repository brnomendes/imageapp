[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=brnomendes_imageapp&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=brnomendes_imageapp) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=brnomendes_imageapp&metric=coverage)](https://sonarcloud.io/summary/new_code?id=brnomendes_imageapp)

# Quick Start

### How to execute ImageApp

To run the application you need the [Pillow](https://pillow.readthedocs.io/) library and it's recommended to have Python 3.6+.

To display the help menu with the list of available filters you can run the following command:
```bash
$ python main.py --help
```

To run, for example, the `RGB Decomposition` filter, you need to pass the filter flag and the necessary arguments, in this case only the image that will be used:
```bash
$ python main.py --rgb /paht/to/image.xyz
```

Using the `--image` flag, providing the image as an argument, a menu will be displayed with the available filters according to the [image mode](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes):

```bash
$ python main.py --image /paht/to/image.xyz
This is an Image App

Avaliable Filters:
1 - Blur
2 - RGB Split
3 - Rotate Image

Type the selected filter number:
```


### How to implement new filters

The implementation of a new filter is completed in only two steps. First, you must create a module where you will implement the filter. This module should be located in the `app/implementations/` directory. You can implement the module as you want, with classes or only functions.

The input to your module will be a [Pillow image](https://pillow.readthedocs.io/en/stable/reference/Image.html#module-PIL.Image) and optionally the arguments.

The output (result) must be a dictionary with the key as a string and values as a [Pillow image](https://pillow.readthedocs.io/en/stable/reference/Image.html#module-PIL.Image).

Let's take as an example a filter that rotates an image. The module will be created in `app/implementations/rotateimage.py`. Besides the image it will receive as an argument an angle in degrees:

```python
def run(image, angle):
    return {f'rotate{angle}': image.rotate(angle)}
```

In this case, the filter generates only one image, so the dictionary has only one value. The key to the image is `rotate<angle>`. The key name is important because it will be used as a complement to the result file name. For example, for the `/paht/to/image.xyz` image and `result` complement, the name of the resulting image will be `/paht/to/image-result.xyz`.

Once the filter implementation is complete, it must be registered in `app/filters.py` to be available to users. For this you must create a function that receives as the first argument the image, and optionally other arguments (all as string), then returns the result of implementation. Important point for names:
 - The function name will be used as the flag for the command line.
 - The name of the arguments will be used as the name for command line arguments and for the interactive menu. If you use underline in the argument name, the interactive menu will display it as space.

Then you must decorate the function with the `register` module. The decorator gets three arguments:

 - `name` **-** The name of the filter that will be displayed in the interactive menu.
 - `types` **-** A list of the [image mode](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes) types that the filter supports.
 - `help` (optional) **-** The message that will be displayed in the command line help.

Following is the example of registering the rotate images filter:

```python
from .implementations import rotateimage
from .filterregister import register

@register(name='Rotate Image', types=['RGB'], help='Rotates the input image clockwise according to the angle.')
def rotate(image, angle_degrees):
    return rotateimage.run(image, int(angle_degrees))
```

After the filter is implemented and registered, it's ready to be used by the users, both on the command line and in the interactive menu. The following shows how the rotate images filter is displayed in the command line help:

```
$ python main.py --help
usage: main.py [-h] (--image image | --rotate image angle_degrees)

An app to process images.

optional arguments:
  -h, --help            show this help message and exit
  --image image         Shows the available filters for the input image.
  --rotate image angle_degrees
                        Rotates the input image clockwise according to the
                        angle.
```

And how it's displayed in the interactive menu:

```
$ python main.py --image data/test-image.png
This is an Image App

Avaliable Filters:
1 - Rotate Image

Type the selected filter number: 1   # user input

Selected Filter: Rotate Image

Type the Angle Degrees: 45           # user input (Note: 'angle_degrees' argument chaged to 'Angle Degrees')
Processing...

Image file processed successfully!
Saving data/test-image-rotate45.png...
```

## Development: Docs and Tests

To generate the documentation and run the tests it's recommended to create a virtual environment Python, for example with [virtualenv](https://virtualenv.pypa.io/):

```bash
$ virtualenv venv -p python3
$ source venv/bin/activate
```

Then install the required dependencies with the [pip](https://pypi.org/project/pip/) and the `setup.py` module:

```bash
(venv) $ pip install -e .
```

### How to generate docs

*Dependencies: [sphinx](http://www.sphinx-doc.org/), [recommonmark](https://recommonmark.readthedocs.io/)*

To generate the documentation in html, in the `docs/` directory you run the `Makefile`:

```bash
(venv) docs/ $ make html
```

By default, the documentation will be generated in the `docs/_build/` directory

*Note: The code documentation is based on [Google Style Python Docstrings](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)*

### How to run tests

*Dependencies: [pytest](https://pytest.org/), [numpy](https://www.numpy.org/)*

To run the tests, you should only run `pytest` at the root of the project:

```bash
(venv) $ pytest
```
