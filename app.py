import tkinter as tk
from tkinter import *
import pyshorteners

shorthener = pyshorteners.Shortener()
root = Tk()

root.geometry('400x200')

def button_command():
    text = entry1.get()
    text = shorthener.tinyurl.short(text)
    entry2.insert(0, text)
    return None

def button_command_del():
    entry1.delete(0, END)
    entry2.delete(0, END)
    return None

root.title("URL SHORTHENER")

L1 = Label(root, text="URL goes here:")
entry1 = Entry(root, width = 60)
L1.pack()
entry1.pack()


L2 = Label(root, text="Shorthened URL is here:")
entry2 = Entry(root, width = 60)

L2.pack()
entry2.pack()


button = Button(root, text="Submit", command = button_command)
button.pack(side = LEFT, padx = 100)

button2 = Button(root, text="Delete", command = button_command_del)
button2.pack(side = LEFT)


root.mainloop()
