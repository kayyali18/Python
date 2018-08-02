##Craps Roller
### This is how random number statements can be written

import random

##Generate random num. 1-6

dice1 = random.randint(1,6)
dice2 = random.randrange(6) + 1

total = dice1 + dice2

print("You rolled a ", dice1, "and a ", dice2, "for a total of " ,total)

input("\n\n \tPress enter to exit the craps game")

