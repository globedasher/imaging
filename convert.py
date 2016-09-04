"""
This is a new applicaiton I am wiring to manipulate an image.
By Richard Morley
"""

from PIL import Image

class Convert():

    def convert_image_to_blue():
        # Open the image to be altered.
        pic = Image.open('original.jpg')
        imageSize = list(pic.getbbox())
        dimX = imageSize[2]
        dimY = imageSize[3]
        for x in range(dimX):
            for y in range(dimY):
                xy = x, y
                pix = pic.getpixel(xy)
                # Remove the red and green hues from each pixel.
                #new_pixel = (pix[0],0,0)
                new_pixel = (0,pix[1],0)
                #new_pixel = (0,0,pix[2])
                # Place the altered pixel back into the picture object.
                pic.putpixel(xy, new_pixel)
        # Save the altered image.
        pic.save('saved.jpg')

Convert.convert_image_to_blue()
