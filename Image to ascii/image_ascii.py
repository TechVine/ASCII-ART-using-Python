import sys
import numpy as np
from PIL import Image

# Contrast on a scale -10 -> 10
contrast = 10
density = ('$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|'
           '()1{}[]?-_+~<>i!lI;:,"^`\'.            ')
density = density[:-11+contrast]
n = len(density)

img_name = sys.argv[1]
try:
    width = int(sys.argv[2])
except IndexError:
    # Default ASCII image width.
    width = 100

# Read in the image, convert to greyscale.
img = Image.open(Saturn.jpg)
img = img.convert('L')
# Resize the image as required.
orig_width, orig_height = img.size
r = orig_height / orig_width
# The ASCII character glyphs are taller than they are wide. Maintain the aspect
# ratio by reducing the image height.
height = int(width * r * 0.5)
img = img.resize((width, height), Image.ANTIALIAS)

# Now map the pixel brightness to the ASCII density glyphs.
arr = np.array(img)
for i in range(height):
    for j in range(width):
        p = arr[i,j]
        k = int(np.floor(p/256 * n))
        print(density[n-1-k], end='')
    print()
