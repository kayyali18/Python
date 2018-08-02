# Saving Private Critter Program
# No Sergeant here
# Demonstrates private variables and methods

class Private (object):
    """A virtual pet"""
    def __init__ (self, name, mood):
        print ("\nA new private has been born")
        self.name = name    #public attribute
        self.__mood = mood  #private attribute

    def talk (self):
        print ("\nI'm private", self.name)
        print ("Right now I feel", self.__mood, "\n")

    def __private_method (self):
        print ("This is a private method")

    def public_method (self):
        print ("This is a public method")
        self.__private_method ()
        print ("^ That is a private method accesed by an object (self) through\
                \n a public method")


# main

crit = Private (name = "7amada", mood = "happy")
crit.talk ()
crit.public_method ()

input ("Press Enter to exit")
