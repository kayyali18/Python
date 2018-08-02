# Simple GUI
# Demonstrates creating a window

from tkinter import *

# create a root window
root = Tk ()

# modify the window

root.title ("Simple GUI") # sets the name of the title
root.geometry ("300x200") # sets the size in pixels

# kick off the window's event loop
root.mainloop ()
