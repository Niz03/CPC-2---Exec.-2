# Improt tkinter for GUI, time, and OS
from tkinter import *
import time
import os

root = Tk()

# Code to display GIF
frameCnt = 1
frames = [PhotoImage(file='majima-melon.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

# Code for text on the right
text = Label(
    root,
    font = ("Arial", 25, "bold"),
    foreground = "white",
    background = "black",
    text = "Nizar C. Arjoun \n Davao City, Febuary 26"
)

text.pack(side=RIGHT)

# Code to handle GIF frames
def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)

# Location of GIF
label = Label(root)
label.pack(side=LEFT)
root.after(0, update, 0)

# Main loop
root.mainloop()
