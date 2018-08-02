## Guess My Number Game GUI

from tkinter import *
import random

# put the random number as a global variable so it doesnt change
# with every function call

number = random.randint (1,100)

class Application (Frame):
    """ A GUI Game where a user has to guess a number picked by computer """
    def __init__ (self, master):
        super (Application, self).__init__(master)
        self.grid ()
        self.number_guess = 0
        self.num_guesses = 0
        self.create_widgets ()
        

    def create_widgets (self):
        """ Create widgets to get user input for guess """
        # create a label for guess
        Label (self,
               text = "Your Guess: ",
               ).grid (row = 1, column = 0, sticky = W)
        self.guess_ent = Entry (self)
        self.guess_ent.grid (row = 1, column = 1, sticky = W)

        # create a click counter button
        self.bttn = Button (self)
        self.bttn ['text'] = "Total Guesses:\t 0"
        self.bttn.grid (row  = 3, column = 3, sticky =W)


        # create a submit button
        Button (self,
                text = "Submit",
                command = self.give_answer # everytime it is clicked. This method runs
                ).grid (row = 3, column = 0, sticky = W)

        # create text box with prompt displayed when initialised
        prompt = """\tWelcome to the Number Guessing Game
I'm going to pick a random number from 1 and 100\n\
I need you to guess it, in the least amount of tries."""
        self.answer_txt = Text (self, width = 75, height = 10, wrap = WORD)
        self.answer_txt.grid (row = 4, column = 0, columnspan = 4)
        self.answer_txt.insert (0.0, prompt)
        

    # def a method to update count
    # I was able to make this method work by putting it in the give_answer method
    # which is run everytime the submit button is clicked
    # as such the update_count method is run everytime the submit button is clicked
    # allowing the self.bttn (Button) to update for every click
    def update_count (self):
        """ Increase click count and display new total"""
        guess = self.guess_ent.get ()
        if guess != None: # if guess entry box is not empty value run:
            self.num_guesses += 1
            self.bttn.configure (text = "Total Guesses:\t" + str(self.num_guesses))

    def game (self, number, guess, number_guess):
        if guess > number:
            reply = "You're too high, guess lower"
        elif guess < number:
            reply = "You're too low, guess higher!"
        elif guess == number:
            reply = "You guessed it and it only took you:\n" + str(number_guess)
            reply += " tries"
        last_guess = "Your last guess was:\t" + str(guess)
        return reply, last_guess

    # create def to give_answer

    def give_answer (self):
        """ Fill text box with reply to guess """
        guess = int(self.guess_ent.get ())
        self.update_count ()
        self.number_guess += 1 # put it in initialisation method
        # update it everytime give_answer method is run
        # in turn it relays as a parameter to the game method
        number_guess = self.number_guess
        global number #global so it doesn't change everytime although I
        # could probably make the random num a method instead. For another day!

        game = self.game (number, guess, number_guess)
        self.answer_txt.delete (0.0, END)
        self.answer_txt.insert (0.0, game)

root = Tk ()
root.title ("Guess My Number")
app = Application (root)
root.mainloop ()
        
        
        
        
        
        
