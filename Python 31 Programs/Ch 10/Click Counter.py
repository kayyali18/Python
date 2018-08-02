# Click Counter
# Demonstrate binding an event with an event handler
from tkinter import *

class Application (Frame):
    """ A GUI app which counts button clicks """
    def __init__ (self, master):
        """ Initialise the frame """
        super (Application, self).__init__(master)
        self.grid ()
        self.bttn_clicks = 0 # the number of button clicks
        self.create_widget ()

    def create_widget (self):
        """ Create button which displays number of clicks """
        self.bttn = Button (self)
        self.bttn ["text"] = "Total Clicks:\t 0"
        self.bttn ["command"] = self.update_count
        self.bttn.grid ()

    def update_count (self):
        """ Increase click count and display new total """
        self.bttn_clicks += 1
        self.bttn.configure (text = "Total Clicks:\t" + str(self.bttn_clicks))

# main
root = Tk ()
root.title ("Click Counter")
root.geometry ("500x300")

app = Application (root)
root.mainloop ()

    
