# Mad Success

from tkinter import *

class Application (Frame):

    def __init__(self, master):
        """ A GUI Application that creates a story based on user imput """
        super (Application, self).__init__(master)
        self.grid ()
        self.create_widgets ()

    def create_widgets (self):
        """ Create widgets to get story"""
        # create instruction label
        Label (self,
               text = "Fill out the blanks and check the boxes to start ",
               ).grid (row = 0, column = 0, columnspan = 2, sticky = W)

        # create a label and text entry for the name
        Label (self,
               text = "Name: "
               ).grid (row = 1, column = 0, sticky = W)
        # entry box
        self.name_ent = Entry (self)
        self.name_ent.grid (row = 1, column = 1, sticky = W)

        # create label from check buttons
        Label (self,
               text = "Do you have: "
               ).grid (row = 2, column = 0, sticky = W)

        # create Discipline Check button
        self.is_disciplined = BooleanVar ()
        Checkbutton (self,
                     text = "Discipline",
                     variable = self.is_disciplined
                     ).grid (row = 2, column = 1, sticky = W)

        # create Desire Check button
        self.is_desire = BooleanVar ()
        Checkbutton (self,
                     text = "Desire",
                     variable = self.is_desire
                     ).grid (row = 2, column = 2, sticky = W)

        # create Dedication Check button
        self.is_dedicated = BooleanVar ()
        Checkbutton (self,
                     text = "Dedication",
                     variable = self.is_dedicated
                     ).grid (row = 2, column = 3, sticky = W)

        # create a label for qoute by famous person
        Label (self,
               text = "Pick a successful person:"
               ).grid (row = 3, column = 0, sticky = W)

        # create a variable for a single qoute
        self.famous_qoute = StringVar () # assign it to StringVar ()
        self.famous_qoute.set (None)

        # create qoute radio buttons
        famous_people = {"Muhammad Ali":
                         """\n\t\t'If my mind can conceive it,
                    and my heart can believe it - then I can achieve it'
                         - Muhammad Ali.""",
                         "Bill Gates":
                         """\n\t\t'It's fine to celebrate success
                    but it is more important to heed the lessons
                    of failure.' - Bill Gates""",
                         "Me (InshAllah)":
                         """\n\t\t'Going from Zero to Hero, doesn't happen
                    in a day. That's why you have 365 a days a year,
                    to work for it everyday' - Ahmad Kayyali"""}
        column = 1
        for key in famous_people:
            Radiobutton (self,
                         text = key,
                         variable = self.famous_qoute,
                         value = famous_people.get (key)
                         ).grid (row = 3, column = column, sticky = W)
            column += 1

        # create a submit button
        Button (self,
                text = "Submit",
                command = self.tell_story
                ).grid (row = 4, column = 0, sticky = W)
        self.story_text = Text (self, width = 75, height = 10, wrap = WORD)
        self.story_text.grid (row = 5, column = 0, columnspan = 4)

    # create a class to use the values entered to create final product

    def tell_story (self):
        """Fill text box with new text based on user input """
        name = self.name_ent.get ()
        threedee = ""
        if self.is_disciplined.get ():
            threedee += " discipline,"
        if self.is_desire.get ():
            threedee += " desire,"
        if self.is_dedicated.get ():
            threedee += " dedication,"
        famous_qoute = self.famous_qoute.get ()

        # create the text

        text = name
        text += ", if you have a problem - make it a challenge!"
        text += "You have "
        text += threedee + "!\n"
        text += "Nothing, can stop you if you stop at nothing!"
        text += "A successful man once said: "
        text += famous_qoute

        # display the story
        self.story_text.delete (0.0, END)
        self.story_text.insert (0.0, text)

# main
root = Tk ()
root.title ("Mad Success")
app = Application (root)
root.mainloop ()
        
                         
                         





















        

        
        
