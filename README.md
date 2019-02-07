# ImageApp  (ESSS Final Task)


### How to implement new filters

`imageapp/implementations/`

`imageapp/implementations/puttext.py`

```python
from PIL import ImageDraw


def run(image, x, y, text_to_put, color):
    draw = ImageDraw.Draw(image)

    draw.text((x, y), text_to_put, color)
    return {'text': image}
```

`imageapp/filters.py`

```python
from .implementations import puttext
from .filterregister import register

@register(name='Put Text', types=['RGB'], help='Put text in position x,y in the image')
def text(image, x, y, text_to_put, color):
    return puttext.run(image, int(x), int(y), text_to_put, color)
```

```
$ python main.py --help
usage: main.py [-h] (--image image | --text image x y text_to_put color)

An app to process images.

optional arguments:
  -h, --help            show this help message and exit
  --image image         Help
  --text image x y text_to_put color
                        Put text in position x,y in the image
```

```
$ python main.py --image data/test-image.png 
This is an Image App

Avaliable Filters:
1 - Put Text

Type the selected filter number: 1 # User Input

Selected Filter: Put Text

Type the X: 5                      # User Input
Type the Y: 5                      # User Input
Type the Text To Put: Hello        # User Input
Type the Color: black              # User Input
Processing...

Image file processed successfully!
Saving data/test-image-text.png...
```
