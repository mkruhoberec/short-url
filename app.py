import tkinter as tk
from tkinter import *
import pyshorteners

shorthener = pyshorteners.Shortener()
root = Tk()
text = Text(root)
root.geometry('400x200')

def button_command():
    text = entry1.get()
    text = shorthener.tinyurl.short(text)
    entry2.insert(0, text)
    return None

def button_command_del():
    entry1.delete(0, END)
    entry2.delete(0,END)
    return None

root.title("URL SHORTHENER")

text.insert(INSERT, "Insert URL here:")
entry1 = Entry(root, width = 60)
entry1.pack()

text.insert(INSERT, "Shortened URL here:")
entry2 = Entry(root, width = 60)
entry2.pack()

button = Button(root, text="Submit", command = button_command)
button.pack()

button2 = Button(root, text="Delete", command = button_command_del)
button2.pack()


text.pack()

root.mainloop()
