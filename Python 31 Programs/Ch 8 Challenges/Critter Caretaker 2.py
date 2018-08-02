## Critter Caretake Program
# A virtual pet to care for
import random, math


class Critter (object):
    """A Virtual Pet"""
    def __init__ (self, name, hunger = random.randrange(0,16),
                  boredom = random.randint (0,15)):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        print (hunger)
        print (boredom)

    # def a private method that affects hunger and boredom as time passed
    # should only be invoked by other method because time passes only if
    # eat, play, or talk is called.

    def __pass_time (self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood (self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "PISSED OFF!"
        return m

    # talk method, announces critter's mood and invokes __pass_time method

    def talk (self):
        print ("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time () ## to invoke a method of an object use ()

    # play method reduces critter boredom by amount passed to the fun parameter
    # if no value passed, fun's value is 4. Boredom level is kept in check
    # not allowed to go below 0
    ## finally method invokes __pass_time ()

    def play (self, fun = 4):
        print("How many hours would you like to play with" ,self.name, "?(0-8)")
        fun = int(input("-----\t"))
        print ("Wheeee!")
        self.boredom -= fun
        # make sure self.boredom doesn't go below zero
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time ()

    def eat (self, eat = 4):
        print("How many meals would you like to feed" ,self.name, "?(0-8)")
        eat = int(input("------\t"))
        print ("Brruppp. Thank youuuu hehe.")
        self.hunger -= eat
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time ()

    # method to display and keep track of hunger and boredom
    def __str__ (self):
        rep = "Critter hunger and boredom\n"
        rep += "Hunger:\t" + str(self.hunger) + "\n"
        rep += "Boredom: " + str(self.boredom) + "\n"

        return rep
    



def main ():
    # getting critter name
    crit_name = input ("What do you want to name your critter?:\t")
    # instantiating Critter object with name above
    crit = Critter (crit_name)

    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter's feelings
        2 - Feed your critter
        3 - Play with your critter
        """)

        choice = input ("Choice:\t")
        print ()

        # exit
        if choice == "0":
            print ("Good-bye")

        # listen to your critter
        elif choice == "1":
            crit.talk ()

        # feed your critter
        elif choice == "2":
            crit.eat ()

        # play with your critter
        elif choice == "3":
            crit.play ()

        # see hunger and boredom
        elif choice == "4":
            print (crit)

        # some unknown choice
        else:
            print ("Your choice is invalid")

main ()
            

input ("Press Enter key to exit")
