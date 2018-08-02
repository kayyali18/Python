##Number guesser program

##Algorithm
##Welcome user, ask to think of number from 1-100
##import random module
##Create input variable correct
##Make var pc_guess = random.randint(1,100)
##Create var min and max for min and max range in pc_guess
##Create count variable outside while loop
##Create user input variable correct
##While variable correct != str('correct')
##  if correct == str('higher'):
##      make min = pc guess + 1
##  else if correct == 'lower':
##      max = pc guess - 1
## Print how many tries it took pc to guess user
##Press enter to exit.

import random
print('Welcome, think of a number from 1 - 100 and I"ll try to guess it')
pc_guess = random.randint(1,100)
input("If you are ready press Enter")
print("My first guess is:\t", pc_guess)
correct = input("Is the number 'lower', 'higher', or 'correct':\t")
min = 1
max = 100
count = 1
while correct != "correct":
    if correct == 'higher':
        min = pc_guess + 1
    elif correct == 'lower':
        max = pc_guess - 1
    elif correct != 'higher' or 'lower':
        print("Learn how to type dumb dumb. Try Again!")
    pc_guess = random.randint(min,max)
    print(pc_guess)
    correct = input("Is the number 'lower', 'higher', or 'correct':")
    count += 1
print("You tried to be tricky and pick", pc_guess, ".\n I guessed it \
in only",count, "tries")
input("Press Enter to continue")
input("Who's your daddy?")
input("I'm your daddy")
