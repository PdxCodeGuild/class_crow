from PIL import Image

img = Image.open('/home/jpchato/class_crow/Code/jesse_pena/labs/cedar.PNG')

width, height = img.size
pixels = img.load()

print(pixels)

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        pixels[i, j] = (r,g,b)

img.show()