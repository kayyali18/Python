# Lazy Buttons 2
# Deomstrates using a class with tkinter
from tkinter import *

# create a Class based on Frame
# instead of instanstiating a Frame object I end up instanstiating an Application
# object to hold all the buttons. This works since an Application object is just
# a specialised type of Frame object.
class Application (Frame):
    """A GUI Application with three buttons """
    def __init__ (self, master):
        """ Initialise the frame """
        super (Application, self).__init__(master)
        self.grid ()
        self.create_widgets ()

    # define a method that creates the three buttons
    def create_widgets (self):
        """ Create three buttons that do nothing """
        # create first button
        self.bttn1 = Button (self, text = "I do nothing!")
        self.bttn1.grid ()

        # create a second button
        self.bttn2 = Button (self)
        self.bttn2.grid ()
        self.bttn2.configure (text = "Me too")

        # create a third button
        self.bttn3 = Button (self)
        self.bttn3.grid ()
        self.bttn3 ["text"] = "Same here!"
        
# main to create root window and give it title and proper size

root = Tk ()
root.title ("Lazy Buttons 2")
root.geometry ("500x500")

# instanstiate an Application object with root as it's master
app = Application (root)

root.mainloop ()
