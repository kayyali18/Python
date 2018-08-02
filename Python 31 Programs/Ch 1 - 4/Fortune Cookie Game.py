##Fortune Cookie Program

##Algorithm

##Import random module
##Set range from 1-5
##Ask user to press Enter to start

##if elif statements tied to each number
##Tell player to not really believe this crap

import random

print("This is a fortune cookie game, everytime you play it you get\n\
a different fortune.")

input("Press Enter to get your fortune:\t")

fortune = random.randint(1,5)

if fortune == 1:
    print("Every problem arises from within oneself, Confucious say.")
elif fortune == 2:
    print("Searching for love, is like searching for yourself. When you\n\
find yourself, you find love.")
elif fortune == 3:
    print("Hey sugar, how you get so flyyyyyy?")
elif fortune == 4:
    print("I'm at the grind, grindin out code. Period.")
elif fortune == 5:
    print("Keep keepin' on brother")
else:
    print("Error")

input("Press enter to exit")
