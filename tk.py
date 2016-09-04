"""
This is a tkinter application by Richard Morley that will manipulate an image 
of Homer J. Simpson as a sample of Python coding using Tkinter library and API.
"""

# Import the necessary libraries, Tkinter and PIL (Python Imaging Library).
import tkinter
from tkinter.constants import *
from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk


# Create a class for the application that will display a window with widgets to
# display and manipulate the image as desired.
class App:

    def __init__(self, master, img):
        # Create the initial window frame and populate it with buttons to
        # control the application.
        frame = Frame(master)
        frame.pack()

        self.hi_there = Button (frame, text="Bart!", command=self.bart)
        self.hi_there.pack(side=LEFT)

        self.picb = Button (frame, text="Show Image", command=self.displayPic)
        self.picb.pack(side=LEFT)

        self.invB = Button (frame, text="Invert Image", command=self.invert)
        self.invB.pack(side=LEFT)

        self.button = Button (
                frame, text="Quit", fg="red", command=frame.quit
                )
        self.button.pack(side=LEFT)

        #self.data_input = Entry (frame, command=self.data_input)

    def bart(self):
        print("Doh!")

    def data_input(self):
        #number = self.entry
        #print(number)
        return

    def displayPic(self):
        # Create a canvas and display an image in the window.
        pos = homer.width // 2, homer.height // 2
        w = Canvas(root, width=homer.width, height=homer.height)
        w.create_image(pos, image=photo)
        w.pack()

    def invert(self):
        # Invert the image.
        current = 0
        dim = homer.getbbox()
        dimX = dim[2]
        dimY = dim[3]
        pos = dimX // 2, dimY // 2
        w = Canvas (root, width=dimX, height=dimY)
        for yColumn in range(dimY):
            for xOnRow in range(dimX):
                xy = xOnRow, yColumn
                total = dimX * dimY
                p = homer.getpixel(xy)
                newpixel = p - 255
                new = PhotoImage(homer.putpixel(xy, newpixel))
        w = Canvas(root, width=dimX, height=dimY)
        w.create_image(pos, image=new)
        w.pack() 


homer = Image.open('homer.gif')
root = Tk()

photo = PhotoImage(file='homer.gif')
app = App(root, photo)

root.mainloop()
root.destroy() #destroy the window
