# Movie Chooser 2
# Deomstrates radio buttons

from tkinter import *

# write the Application class with Frame as it's master
class Application (Frame):
    """ A GUI Application for favourite movie type """
    # define constructor method that intialises new Application object
    def __init__ (self, master):
        super (Application, self).__init__(master)
        self.grid ()
        self.create_widgets ()

    # create labels in widgets method that give user instructions
    def  create_widgets (self):
        """ Create widgets for movie type choices """
        # create description label
        Label (self,
               text = "Choose your favourite type of movie"
               ).grid (row = 0, column = 0, sticky = W)

        # create instruction label
        Label (self,
               text = "Select one:\t"
               ).grid (row = 1, column = 0, sticky = W)

        # unlike check boxes, there's no need for radio buttons to each
        # have a status variable. Instead a group can share one object
        # This case will be the StringVar () method from the tkinter module
        # StringVar () allows a string to be stored and retrieved

        # create StringVar () object for buttons to share
        # assign it to the attribute favourite and set it's initial value
        # to None using the object's set () method
        self.favourite = StringVar ()
        self.favourite.set (None)

        # create Comedy radio button
        Radiobutton (self,
                     text = "Comedy",
                     variable = self.favourite, #defines special variable
                     value = "comedy.", # defines value to be stored by special var
                     command = self.update_text
                     ).grid (row =2, column = 0, sticky = W)
        # create Drama radio button
        Radiobutton (self,
                     text = "Drama",
                     variable = self.favourite,
                     value = "drama.",
                     command = self.update_text
                     ).grid (row = 3, column = 0, sticky = W)


        # create Romance radio button
        Radiobutton (self,
                     text = "Romance",
                     variable = self.favourite,
                     value = "romance.",
                     command = self.update_text
                     ).grid (row = 4, column = 0, sticky = W)

        # create text field to display result
        self.results_txt = Text (self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid (row = 5, column = 0, columnspan = 3)

    def update_text(self):
        """ Update text area and display user's favourite movie type """
        message = "Your favourite type of movie is "
        message += self.favourite.get ()
        # delete anything in text box and insert current selection
        self.results_txt.delete (0.0, END)
        self.results_txt.insert (0.0, message)

# main
root = Tk()
root.title ("Movie Chooser 2 ")
app = Application (root)
root.mainloop ()
        

























        
