## Word Jumble Program
#
# The computer picks a random word and then jumbles it
# The player has to guess the original word

import random

## Create constant variable WORD that is a tuple and contains list of words
# to jumble
#
# Create a sequence of words to choose from

WORDS = ("The Grind",
         "Coffee",
         "Programming",
         "Ramadan",
         "Chelsea")

## Use function random.choice() to grab a random word from WORDS
#
## Pick one word randomly from the sequence

word = random.choice(WORDS)

# create a variable to use later to see if the guess is correct

correct = word

# Use pseudocode to plan, always:
#
## create an empty jumble word
## while the chosen word has letters in it
##      extract a random letter from the chosen word
##      add the random letter to the jumble word


# create a jumbled version of the word

jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word [(position + 1):]

# start the game
print (
"""
            Welcome to Word Jumble!

        Unscramble the letters to make a word.
    (Press the Enter key at the prompt to quit.)
"""
)
print ("The jumble is:\t", jumble)

## Creating the code to get the player's guess

guess = input("\nYour guess:\t")
while guess != correct and guess != "":
    print ("Sorry, that's not it")
    guess = input("Your guess:\t")

if guess == correct:
    print("That's it! You guessed it!\n")

print ("Thanks for playing!")
input ("\nPress Enter key to exit")
    
        
