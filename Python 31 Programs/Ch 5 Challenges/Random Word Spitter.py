## Chapter 5 Challenges

## Random Word Spitter

print ("This is a random word spitter. Everytime you press Enter, I will\n\
spit a name of a player until all have been spat")
input ("Press Enter to start")

words = ["A7mad Basha+", "3am_3am_3am", "MANASRA", "BLACK SERIES"]
import random
empty = []

while len(words) != 0:
    x = random.choice(words)
    print ("\n",x)
    words.remove(x)
    input("Press Enter to see the next word")

input ("That's all folks!")
input ("Thanks for playing, press Enter to quit")
