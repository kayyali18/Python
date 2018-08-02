# Simple Game
## Demonstrates iporting modules

import games, random

print ("Welcome to the world's simplest game!\n")

again = None
while again != "n":
    players = []
    num = games.ask_number(question = "How many player? (2-5):\t",
                           low = 2, high =6)

    for i in range (num):
        name = input ("Player name:\t")
        score = random.randrange (100) + 1
        player = games.Player (name, score)
        players.append (player)

    print ("\nHere are the results:\t")
    for player in players:
        print (player)

    again = games.ask_yes_no(question = "\nDo you want to play again? (y/n):\t")

input ("\n\nPress Enter to exit")

