from tkinter import *

def main():
	root = Tk()
	root.geometry("400x400")
	app = App(root)
	root.mainloop()

def hello():
    print ("hello!")

# create a toplevel menu

class App():
	def __init__(self, master=None):
		self.tk = master
		self.createCanvas()
		self.menuBar()
		self.events()
		self.buttons()

	def menuBar(self):
		menubar = Menu(self.tk)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="New", command=self.createCanvas)
		filemenu.add_command(label="Open", command=hello)
		filemenu.add_command(label="Save", command=hello)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.tk.quit)
		menubar.add_cascade(label="File", menu=filemenu)
		self.tk.config(menu=menubar)
	def buttons(self):
		f = Frame(self.tk, bg='#123456')
		closeButton = Button(f, text="Close")
		closeButton.pack(side=RIGHT, padx=5, pady=5)
		okButton = Button(f, text="OK")
		okButton.pack(side=RIGHT)
		f.place(x=0, y=0)

	def createCanvas(self):
		c = Canvas(self.tk, width=300, height=300, bg='#111111')
		c.pack()
		self.canvas = c
	def events(self):
		self.tk.bind_class('Canvas','<Button-1>', self.click)
	def click(self, event):
		self.canvas.create_rectangle(event.x, event.y, event.x, event.y, outline='green')
		print ("Clicked: "+str(event.x)+":"+str(event.y))

main()