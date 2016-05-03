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
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="New", command=self.canvas)
		filemenu.add_command(label="Open", command=hello)
		filemenu.add_command(label="Save", command=hello)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.tk.quit)
		menubar.add_cascade(label="File", menu=filemenu)
		self.tk.config(menu=menubar)
	def canvas(self):
		canvas = Canvas(self.tk, bg='#333399')
		canvas.create_bitmap(100,100)
		canvas.pack()

main()