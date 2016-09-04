#my first tkinter app

import tkinter
from tkinter.constants import *
from tkinter import *
from PIL import Image, ImageTk


class App:

    def __init__(self, master, img):

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

        self.data_input = Entry (
                frame, command=self.data_input
                )

    def bart(self):
        print("Doh!")

    def data_input(self):
        #number = self.entry
        #print(number)
        return

    def displayPic(self):
        pos = photo.width() // 2, photo.height() // 2
        w = Canvas (root, width=photo.width(), height=photo.height())
        w.create_image(pos, image=photo)
        w.pack()
        return w

    def invert(self):
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
        #newIm = Image(new)
        #newDim = new.getbbox()
        #print(newDim)
        w = Canvas (root, width=dimX, height=dimY)
        w.create_image(pos, image=new)
        w.pack() 


homer = Image.open('homer.jpg')
root = Tk()

photo = PhotoImage('homer.jpg')
app = App(root, photo)

root.mainloop()
root.destroy() #destroy the window
