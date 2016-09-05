"""
This is a new applicaiton I am wiring to manipulate an image.
By Richard Morley
"""

import tkinter
from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk


class App:
    """
    Create a class for the application that will display a window with widgets
    to display and manipulate the image as desired.
    """

    def __init__(self, master, picture):
        # Create the initial window frame and populate it with buttons to
        # control the application.
        frame = Frame(master)
        frame.pack()

        self.hi_there = Button (frame, text="Bart!", command=self.bart)
        self.hi_there.pack(side=LEFT)

        self.picb = Button (frame, text="Show Image", command=self.displayPic)
        self.picb.pack(side=LEFT)

        # Convert to Red button
        self.invB = Button (frame, text="Convert to Red", 
                command=img.convert_image_to_red)
        self.invB.pack(side=LEFT)
        
        # Convert to Green button
        self.invB = Button (frame, text="Convert to Green", 
                command=img.convert_image_to_green)
        self.invB.pack(side=LEFT)
        
        # Convert to Blue button
        self.invB = Button (frame, text="Convert to Blue", 
                command=img.convert_image_to_blue)
        self.invB.pack(side=LEFT)

        self.button = Button (
                frame, text="Quit", fg="red", command=frame.quit
                )
        self.button.pack(side=LEFT)

    def bart(self):
        print("Doh!")

    def data_input(self):
        #number = self.entry
        #print(number)
        return

    def displayPic(self):
        # Create a canvas and display an image in the window.
        pos = img.pic.width // 2, img.pic.height // 2
        w = Canvas(root, width=img.pic.width, height=img.pic.height)
        w.create_image(pos, image=photo)
        w.pack()


class Convert:
    """
    The Convert class is used to filter an image so only red, green or blue is
    left in the saved image.
    """

    def __init__(self, original_picture):
        self.pic = original_picture

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


# Open the original picture.
img = Convert(Image.open('original.jpg'))
# Create the tkinter window.
root = Tk()
# Create an ImageTk.PhotoImage of the original photo.
photo = ImageTk.PhotoImage(img.pic)
app = App(root, photo)
root.mainloop()
root.destroy() #destroy the window
