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

`imageapp/implementations/`

`imageapp/implementations/rotateimage.py`

```python
def run(image, angle):
    return {f'rotate{angle}': image.rotate(angle)}
```

`imageapp/filters.py`

```python
from .implementations import rotateimage
from .filterregister import register

@register(name='Rotate Image', types=['RGB'], help='Rotates the input image clockwise according to the angle.')
def rotate(image, angle_degrees):
    return rotateimage.run(image, int(angle_degrees))
```

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

```
$ python main.py --image data/test-image.png
This is an Image App

Avaliable Filters:
1 - Rotate Image

Type the selected filter number: 1   # user input

Selected Filter: Rotate Image

Type the Angle Degrees: 45           # user input
Processing...

Image file processed successfully!
Saving data/test-image-rotate45.png...
```

### How to generate docs


### How to execute test
