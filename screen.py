# Adriel Freud

from tkinter import *
import pyscreenshot as Image
import random

def main():
	global root

	root = Tk()
	root.title("Screenshooter")

	Label(root, text="Nome", fg="black", bg="white", font="Arial 11").place(x=5, y=30)
	
	global name_Entry
	name_Entry = Entry(root, fg="black", bg="white")
	name_Entry.place(x=50, y=30)

	Button(root, text="Shoot", fg="black", bg="white", command=screenshot).place(x=45, y=100)
	Button(root, text="Config", fg="black", bg="white", command=config).place(x=115, y=100)


	root["bg"] = "white"
	root.geometry("230x150")
	root.mainloop()


def generate_string():
	nome = "screnn_%s.png"%random.randint(1, 10000)
	return nome

def save_config():
	global data
	data = (int(X1.get()), int(X2.get()), int(Y1.get()), int(Y2.get()))
	win.destroy()

def config():
	global win

	win = Tk()
	win.title("Config")

	Label(win, text="X1", fg="black", bg="white", font="Arial 11").place(x=5,y=30)
	global X1
	X1 = Entry(win, fg="black", bg="white", width=7)
	X1.place(x=50, y=30)

	Label(win, text="X2", fg="black", bg="white", font="Arial 11").place(x=5,y=50)
	global X2
	X2 = Entry(win, fg="black", bg="white", width=7)
	X2.place(x=50, y=50)

	Label(win, text="Y1", fg="black", bg="white", font="Arial 11").place(x=5,y=70)
	global Y1
	Y1 = Entry(win, fg="black", bg="white", width=7)
	Y1.place(x=50, y=70)

	Label(win, text="Y2", fg="black", bg="white", font="Arial 11").place(x=5,y=90)
	global Y2
	Y2 = Entry(win, fg="black", bg="white", width=7)
	Y2.place(x=50, y=90)

	Button(win, text="SAVE", fg="black", bg="white", font="Arial 11", command=save_config).place(x=45, y=130)

	win["bg"] = "white"
	win.geometry("150x170")
	win.mainloop()

def screenshot():
	global img 
	img = Image.grab(bbox=data)
	if(name_Entry.get()):
		img.save(name_Entry.get())
	else:
		img.save(generate_string())

	img.close()

main()