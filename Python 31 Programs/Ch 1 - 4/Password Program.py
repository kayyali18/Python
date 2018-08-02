##Granted or Denied Program

## A program that asks for password if password is correct
##access is granted, else access is denied.
import sys
from tkinter import *

class Application (Frame):
    """ GUI Application to reveal a morale booster for me """
    def __init__(self, master):
        """ Initialise the frame """
        super (Application, self).__init__(master)
        self.grid ()
        self.create_widgets ()

    def create_widgets (self):
        """ Create button, text, and entry widgets """
        self.inst_lbl = Label (self, text = "Please enter your password")
        self.inst_lbl.grid (row = 0, column = 0, columnspan = 2, sticky = W)

        # create label for password
        self.pw_lbl = Label (self, text = "Password:\t")
        self.pw_lbl.grid (row = 1, column = 0, sticky = W)

        # create an entry widget to accept password
        self.pw_ent = Entry (self)
        self.pw_ent.grid (row = 1, column = 1, sticky = W)

        # create a submit button
        self.submit_bttn = Button (self, text = "Submit", command = self.reveal)
        self.submit_bttn.grid (row = 2, column = 0, sticky = W)

        # create a text widget to display message
        self.secret_txt = Text (self, width = 40, height = 20, wrap = WORD)
        self.secret_txt.grid (row = 3, column = 0, columnspan = 2, sticky = W)

    def reveal (self):
        """ Display message based on password """
        contents = self.pw_ent.get ()
        if contents == "Qwerty607":
            message = """ This is for those times you need Peace of Mind Remember
how you were before. You were focused, alert, responsable-\n\
and very comitted. It was easier to be happy, it was better just being. \n\
Thank God, you atleast have the decency to know that it was better before. \n\
For once, it would be nice to do what's better. In the words of the Late Muhammad Ali,\n\
'If my mind can conceive it, and my heart can believe it - then I can achieve it.'\n\
I know I can conceive it, and I my heart can definitely believe it. So I'm going to \n\
achieve it. InshAllah."""
        else:
            message = "Stop trying to hack into my shit!"

        self.secret_txt.delete (0.0, END)
        self.secret_txt.insert (0.0, message)

# main
root = Tk ()
root.title ("Do Not Open!")
root.geometry ("350x400")

app = Application (root)

root.mainloop ()


        












##
##password = input ("Please enter your password:\t")
##
##total = 0
##
##while password != "Qwerty607":
##    print ("\aAcces Denied")
##    password = input ("Please enter your password:\t")
##    total += 1
##    if total == 5:
##        print ("\nStop trying to hack into my shit!")
##        input ()
##        sys.exit()
##    
##
##print ("\a")
##input ("Press Enter to hear that again")
##print ("\a Access Granted")
##input ("This is for those times you need Peace of Mind")
##print ("Remember how you were before. You were focused, alert, responsable-\n\
##and very comitted. It was easier to be happy, it was better just being. \n\
##Thank God, you atleast have the decency to know that it was better before. \n\
##For once, it would be nice to do what's better. In the words of the Late Muhammad Ali,\n\
##'If my mind can conceive it, and my heart can believe it - then I can achieve it.'\n\
##I know I can conceive it, and I my heart can definitely believe it. So I'm going to \n\
##achieve it. InshAllah.")
##
##input("Press enter to exit")
