from tkinter import *

def main():
	root = App(Tk())
	root.tk.mainloop()

def hello():
    print ("hello!")

# create a toplevel menu

class App():
	def __init__(self, master=None):
		self.tk = master
		self.menuBar()

	def menuBar(self):
		menubar = Menu(self.tk)
		menubar.add_command(label="Hello!", command=hello())
		menubar.add_command(label="Quit!", command=self.tk.quit)
		self.tk.config(menu=menubar)

main()