# Quick Start


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
