# Hangman Game
#
# The classic game of Hangman. The computer picks a random word
# and the player has to guess it, one letter at a time. If the player
# can't guess the word in time, the little stick figure gets hanged

# imports random module

import random

# constants
HANGMAN = (
    """
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

# constant no. 2

MAX_WRONG = len(HANGMAN) - 1

# constant no. 3

WORDS = ("THE GRIND", "HANGMAN", "WHEEL OF FORTUNE",
         "AEROPOSTALE", "PYTHON", "CASABLANCA",
         "ALASKA", "SILLY GOOSE", "OVERUSED")

# initialise variables

word = random.choice(WORDS) # the word to be guessed

so_far = "-" * len(word) # one dash for each letter in word to be guessed

wrong = 0 # counter to keep track of number of wrong guesses

used = [] # list to keep track of letters already guessed


print("Welcome to Hangman. Good luck!")

while wrong < MAX_WRONG and so_far != word:
    print (HANGMAN[wrong])
    print ("\nYou've used the following letters:\n", used)
    print ("\nSo far, you have guessed:\t", so_far)

    guess = input("Enter your guess:\t")
    guess = guess.upper()

    while guess in used:
        print ("You already guessed the letter:\t", guess)
        guess = input("Guess again:\t")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print ("The letter, ", guess, "is in the word")

        # create a new so_far to include guess
        new = ""


        for i in range(len(word)):
            if guess == word [i]:
                new += guess
            else:
                new += so_far [i]
        so_far = new

    else:
        print ("\nSorry,", guess, "isn't in word")
        wrong += 1

if wrong == MAX_WRONG:
    print (HANGMAN[WRONG])
    print ("I would tell you, that you've been hanged. \n\
But you're dead, so.......RIP?")

else:
    print("\nYou guessed it!")

print("\nThe word was", word)

input ("\n\nPress Enter key to exit")




    


























