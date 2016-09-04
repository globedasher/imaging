#building something from scratch
#importing modules for use in the application
import tkinter
from PIL import Image, ImageTk

#import the image and get dimensions
img = Image.open("homer.jpg")
imageSize = list(img.getbbox())
dimX = imageSize[2]
dimY = imageSize[3]


#iterate through the image data and invert to chosen color
def invert(color, invertCh):
    current = 0
    for yColumn in range(dimY):
        for xOnRow in range(dimX):
            xy = xOnRow, yColumn
            total = dimX * dimY #for "mount.jpg" = 7053161 pixels
            current = current + 1
            percent = int((current / total) * 100)
            #per = int(percent)
            print("\b" * 6,)
            print(str(percent) + "%",)
            p = img.getpixel(xy)
            print(p)

            #remove all but the chosen color
            if color == "Red":
                newpixel = (p[0],0,0)
            elif color == "Green":
                newpixel = (0,p[1],0)
            elif color == "Blue":
                newpixel == (0,0,p[2])
            else:
                print("Invalid input.(2)")

            #write new pixel to new image file
            img.putpixel(xy, newpixel)

#create a function that prints the progress
def printProgress(progress):
    out = (str(progress) + "%")
    bs = "\b" * 4
    print(bs)
    print(out)

#save the file and append the file name
def save(color, invertCh):
    #save the resulting image
    if invertCh == "y":
        img.save(color + "Inv.jpg")
    else:
        img.save(color + "Reg.jpg")

#user choice for app use
def setup():
    """Primary config of user choices"""
    invertCh = input("Invert? (y/n) ")
    invertLs = ["y", "n"]
    color = input("Which color? Red, Green, Blue? ")
    color = color.title()
    colorList = ["Red", "Green", "Blue"]
    if color in colorList:
        invert(color, invertCh)
    else:
        print("Invalid input.(1)")

def main():
    setup()

main()
