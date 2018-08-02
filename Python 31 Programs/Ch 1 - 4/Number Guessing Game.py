##This is my first true attempt to write a program from scratch with no help
##The only help I had was how to write the algorithm for the game
##I changed it a little bit to suit my needs but nonetheless
##The following is written solely by me

##Number Guessing Game
##importing random module
import random

print("\tWelcome to the Number Guessing Game")
print("I'm going to pick a random number from 1 and 100\n\
I need you to guess it, in the least amount of tries.")


#Set number variable to random integer every time it's called
number = random.randint(1,100)

#Player guess is input and must be integer
player_guess = int(input("\nPick a number:\t"))

#Set number of guesses variable outside of loop
number_guess = 1

#While loop that runs as long as number is not guessed correctly
while player_guess != number:
    if player_guess > number:
        print("You're too high, guess lower")
    else:
        print("You're too low, guess higher")
    player_guess = int(input("Guess again:\t"))
    number_guess += 1

print("\aCongratulations you guessed correctly and it only took you:\t",\
      number_guess,"guesses!")
input("Press Enter key to exit")
