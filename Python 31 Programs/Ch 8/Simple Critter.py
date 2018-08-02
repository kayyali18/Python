# Simple Critter
# Demonstrates a basic class and object

class Critter (object):
    """A Virtual pet"""

    def __init__ (self, name):
        print ("A new critter has been born")
        self.name = name

    def __str__ (self):
        rep = "Critter object \n"
        rep += "name:\t" + self.name + "\n"

        return rep

    def talk (self):
        print ("Hi! I'm", self.name, "\n")

# main

crit1 = Critter ("Poochie")
crit1.talk ()

crit2 = Critter ("Randyyyyy")
crit2.talk ()

print ("Printing crit1:\n" , crit1)
print ("Directly accessing crit1.name:\n", crit1.name)
