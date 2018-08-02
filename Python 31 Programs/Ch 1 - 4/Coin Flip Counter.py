##Coin flip counter program

##Algorithm

##import random
##Set value for coin to range (1,2)
##Create heads and tails value set at 0
## Create flip counter
##While count is < 100
##Flip coin
## Count if heads or tails
## Repeat

print("Welcome to the Coin Flip Counter Program")
input("This program will flip a coin 100 times and give you \n\
back the results. Press enter to check it out:")

import random


heads = 0
tails = 0
flip_counter = 0

while flip_counter < 100:
    coin = random.randint(1,2)
    if coin == 1:
        heads += 1
    elif coin == 2:
        tails += 1
    flip_counter += 1

print("Total amount of heads vs tails in 100 tries is:\n\t",
      heads, "heads\n\t", tails,"tails.")

input ("\nPress Enter to exit")
