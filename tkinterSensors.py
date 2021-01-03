'''
2020/05/XX
This is a python test of sensors updating every second
'''

from tkinter import *
from psutil import *
from time import strftime

root = Tk()
root.title("Sensors")

root.attributes('-type', 'dialog')

def fTime():
    s = strftime('%I:%M:%S %p')
    lTime.config(text = s)
    lTime.after(1000, fTime)

def fTemp():
    return

def fMem():
    return

lTime = Label(root, fg = 'white', bg = 'black')
lTime.pack()

fTime()

root.mainloop()
