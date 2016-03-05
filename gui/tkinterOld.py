#!/usr/bin/env
import Tkinter as tk
from Tkinter import *
def main():
	app = App2(Tk())
	app.master.title('Sample application')
	app.mainloop()

class App1(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid()
		self.createWidgets()
	def createWidgets(self):
		self.quitButton = tk.Button(self, text='Quit', command=self.quit)
		self.quitButton.grid()
class App2():
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        self.button = tk.Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = tk.Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!"

main()