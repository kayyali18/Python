# Classy Critter
# Demonstrates class attributes and static methods

class Critter (object):
    """A virtual pet"""
    total = 0

    @staticmethod
    def status ():
        print ("\nThe total number of critters is:\t", Critter.total)

    def __init__ (self, name):
        print ("A critter has been born!")
        self.name = name
        Critter.total += 1

# main
print ("Accessing the class attribute Critter.total:|t", end = " ")
print (Critter.total)

Critter.status ()

print ("\nCreating critters")
crit1 = Critter ("Manuel")
crit2 = Critter ("Johnathan")
crit3 = Critter ("Tom")

Critter.status ()

print ("\nAccesssin the class attribute through an object:\t", end = " ")
print (crit1.total)

input ("\nPress Enter key to exit")
