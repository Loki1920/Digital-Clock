from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Digital Clock")

def time():
    string = strftime("%I:%M:%S %p")
    label.config(text = string)
    label.after(1000, time)

label = Label(root, font = "ds-digital 100", background = "dark blue", foreground = "red")
label.pack(anchor = "center")

time()

mainloop()