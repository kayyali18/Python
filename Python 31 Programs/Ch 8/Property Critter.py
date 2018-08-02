## Property Critter

# Demonstrates properties

class Critter (object):
    """A virtual pet"""
    def __init__ (self, name):
        print ("\nA new critter has been born!")
        self.__name = name

    @property
    def name (self):
        return self.__name

    @name.setter
    def name (self, new_name):
        if new_name == "":
            print ("\nA critter's name can't be the empty string")
        else:
            self.__name = new_name
            print ("\nName change successful!")
    def talk (self):
        print ("\nHi, I'm", self.name)

# main

crit = Critter ("Mr. Jamal")
crit.talk ()

print ("\nMy critter's name is :", end = " ")
print (crit.name)

print ("\nAttempting to change the critter's name to 7amooda....")
crit.name = "7amooda"

print ("\nMy critter's name is now....")
print (crit.name)

print ("\nAttemptin to change critter's name to empty string")
crit.name = ""

print ("\n My critter's name is still....")
print (crit.name)
