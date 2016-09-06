"""
This is a new applicaiton I am wiring to manipulate an image.
By Richard Morley
"""

from PIL import Image

class Convert:
    """
    The Convert class is used to filter an image so only red, green or blue is
    left in the saved image.
    """

    def __init__(self, original_image):

        self.pic = original_image

    def get_pic(self):
        return self.pic

    def convert_image_to_red(self):
        # Open the image to be altered.
        imageSize = list(self.pic.getbbox())
        dimX = imageSize[2]
        dimY = imageSize[3]
        for x in range(dimX):
            for y in range(dimY):
                xy = x, y
                pix = self.pic.getpixel(xy)
                # Remove the green and blue hues from each pixel.
                new_pixel = (pix[0],0,0)
                # Place the altered pixel back into the picture object.
                self.pic.putpixel(xy, new_pixel)
        # Save the altered image.
        self.pic.save('saved.jpg')
    
    def convert_image_to_green(self):
        # Open the image to be altered.
        imageSize = list(self.pic.getbbox())
        dimX = imageSize[2]
        dimY = imageSize[3]
        for x in range(dimX):
            for y in range(dimY):
                xy = x, y
                pix = self.pic.getpixel(xy)
                # Remove the red and blue hues from each pixel.
                new_pixel = (0,pix[1],0)
                # Place the altered pixel back into the picture object.
                self.pic.putpixel(xy, new_pixel)
        # Save the altered image.
        self.pic.save('saved.jpg')

    def convert_image_to_blue(self):
        # Open the image to be altered.
        imageSize = list(self.pic.getbbox())
        dimX = imageSize[2]
        dimY = imageSize[3]
        for x in range(dimX):
            for y in range(dimY):
                xy = x, y
                pix = self.pic.getpixel(xy)
                # Remove the red and green hues from each pixel.
                new_pixel = (0,0,pix[2])
                # Place the altered pixel back into the picture object.
                self.pic.putpixel(xy, new_pixel)
        # Save the altered image.
        self.pic.save('saved.jpg')
