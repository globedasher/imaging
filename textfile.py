#This is a test of altering a text file with my python script

infile = open("text.txt", "r")
outfile = open("conv.txt", "w")
aline = infile.readline()

while aline:
    items = aline.split()
    dataline = items[1] + "," + items [0]
    outfile.write(dataline + "\n")
    aline = infile.readline()

infile.close()
outfile.close()
