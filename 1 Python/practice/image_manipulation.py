import colorsys
import math
from PIL import Image


img = Image.open("corgi.jpg") # must be in same folder
width, height = img.size
pixels = img.load()

#filter portion here:
for x in range(width):
  for y in range(height):
    r, g, b = pixels[x, y]

    h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

    # Murder this picture with maths
    t = x * y
    h *= math.sin(x * s) / 10
    s -= math.tan(y * 10000 / (x + 1)) / 7
    v -= (t & x << 5) / (t + 1) 

    r, g, b = colorsys.hsv_to_rgb(h, s, v)

    pixels[x, y] = (int(r * 255), int(g * 255), int(b * 255))
# img.save("corgi.jpg") #you might not need to save it, show should just open image wo saving
img.show()
