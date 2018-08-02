# Lazy Buttons
# Demonstrates creating buttons

from tkinter import *

# create a root window
root = Tk ()
root.title ("Lazy Buttons")
root.geometry ("400x550")

# create a frame in the window to hold other widgets

app = Frame (root)
app.grid ()

# to create a Button widget I instanstiate an object of the Button class
# create a button in the frame
bttn1 = Button (app, text = "I do nothing!")
bttn1.grid ()

# create a second button in the frame
bttn2 = Button (app)
bttn2.grid ()
# Since we only create an empty Button Widget
# We need to modify it by using the configure () method
bttn2.configure (text = "Me too, even though I was configured")

# create a third button in the frame
bttn3 = Button (app)
bttn3.grid ()

# to modify bttn3 text I will use a dictionary style reference.
# the key for the option is the name of the option as a string
bttn3 ["text"] = "Same here, even though modified with dictionary-like reference"


# always invoke the root window's event loop to start the GUI
root.mainloop ()
