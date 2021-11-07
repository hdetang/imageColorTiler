# imageColorTiler

Divides an image into a specified dimensioned grid. Each tile of the grid is filled of the dominant color in the corresponding region of the image.
You can run the script with the following command :
```
python imageColorTiler.py <path-to-image> <columns> <rows>
```

## Examples

Here is a few examples of what this script can achieve :

### Get the dominant color

Get the most dominant color in your image.
This was the original purpose of this script but I decided to tweak it and make it with a grid system.

```
python imageColorTiler.py ./examples/color/original.jpg 1 1
```
Shot from the Blade Runner 2049 (2017):
![Blade Runner 2049(2017)](./examples/color/original.jpg)
Dominant color :
![Color Blade Runner 2049(2017)](examples/color/color.jpg)

### Slice an image 

Slice an image into several band (e.g. for seeing the color repartion through the image)

```
python imageColorTiler.py ./examples/slice/original.jpg 8 1
```
Shot from the Star Wars: The Last Jedi (2017):
![Star Wars: The Last Jedi(2017)](./examples/slice/original.jpg)
Sliced image :
![Sliced Star Wars: The Last Jedi(2017)](examples/slice/slice.jpg)

### Pixelate  an image

You can simply pixelate an image 
```
python imageColorTiler.py ./examples/pixel/original.jpg 80 100
```
Shot from the movie Skyfall (2012):
![Skfall(2012)](./examples/pixel/original.jpg)
Pixelated image :
![Pixelated Skyfall(2012)](examples/pixel/pixel.jpg)