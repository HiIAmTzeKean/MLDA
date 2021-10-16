from PIL import Image
import numpy

im = Image.open('test.png')
im = im.resize((96, 96))
pixels = list(im.getdata())

final=""
for item in pixels:
    string = "0x"
    for num in item:
        string += "{0:x}".format(num).zfill(2)
    final+=string+ ', '

fileout = open("test.txt", "w")
fileout.write(final[:-2])
fileout.close