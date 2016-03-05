#!/usr/bin/python


#Aaron Quan 2016
#playing around with Tkinter
from tkinter import *
import os
import subprocess
#import Image

#subprocess.call("image.bmp", shell=True)
'''
app = Application()
app.master.geometry("60x40")
app.master.title('Sample application')
app.mainloop()
'''

root = Tk()

image = PhotoImage(file="image.png")
label = Label(root, image=image)
label.pack()

root.mainloop()