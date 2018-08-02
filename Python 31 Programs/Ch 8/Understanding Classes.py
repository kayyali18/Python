## Simple Critter

class Critter (object): # class header
    """A Virtual pet"""  # docstring (documents the class) 
    def talk (self):   # method
        print ("Hi, I am an instance of class Critter.")


# main
crit = Critter () # creating an object of the class Critter ()

crit.talk () # is like saying Critter.talk () but we're referring to
                # the object of the class instead of the class itself

                
# Constructors are methods that are automatically invoked after a new object
 # is created. I'll often use one after setting up a class


# Constructor Critter
# Demonstrating Constructors

class Critter (object):
    def __init__ (self): # constructor method, initialisation method
        print ("\nA new critter has been born")

    def talk (self):
        print ("\nHi! I am an instance of class Critter")

# main

crit = Critter ()
crit2 = Critter ()

crit.talk ()
crit2.talk ()


# Attribute Creator Program


class Critter (object):
    """A virtual pet"""

    def __init__ (self, name, age):
        print ("\nA new critter has been born")
        self.name = name
        self.age = age

    def __str__ (self): # special method to print something if object is called
        rep = "Critter object \n"
        rep += "name:\t" + self.name + "\n"

        return rep

    def talk (self):
        print ("\nHi, my name is", self.name, "and I am", self.age, "days old")


# main

crit = Critter ("Poochie", 3) # object 1
crit.talk ()

crit2 = Critter ("Alex", 4) # object 2
crit2.talk ()

crit3 = Critter ("Basha", 22) # object 3
crit3.talk ()


print ("Print crit")
print (crit)

print ("\nDirectly accessing crit3.name:\t")
print (crit3.name)
print ("Directly accessing crit3.age:\t")
print (crit3.age)


# Classy Critter
# Demonstrates class attributes and static methods

class Critter (object):
    """ A virtual pet"""
    total = 0 # a class attribute tied to the class rather than object

    @staticmethod # notice method has no self parameter
                    # are invoked through the class no the object
                        # meaning no self parameter is required
                            # because self calls to object
    def status ():
        print ("The total number of critters is:\t", Critter.total)

    def __init__ (self, name):
        print ("\nA critter has been born")
        self.name = name
        Critter.total += 1

        
# main

print ("Accessing the class attribute Critter.total:\t", end = " ")
print (Critter.total)

print ("\nCreating critter")
crit = Critter ("critter 1")
crit2 = Critter ("critter 2")
crit3 = Critter ("critter 3")

Critter.status () # invoking the class attribute
                    #everytime the initialisation method is invoked i.e. everytime
                        # an object is instanstiated
                            #name and total is updated
                                # total is a class attribute so it remains in the class
                                     #not the object

print ("Accessing the class attribute through an object:\t", end = " ")
print (crit.total)


# Saving Private Critter Program
# No Sergeant here
# Demonstrates private variables and methods

class Private (object):
    """A virtual pet"""
    def __init___ (self, name, mood):
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

crit = Critter (name = "7amada", mood = "happy")
crit.talk ()
crit.public_method ()


    


        
        














































        
