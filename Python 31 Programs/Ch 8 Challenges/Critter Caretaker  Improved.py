import random, math

# creating a class

class Critter (object):
    """A virtual pet"""
    total = 0
    crit_names = []

    @staticmethod
    def status ():
        print ("\nYou have", Critter.total, "critters in your farm")
        print ("Their names are in  a list:\t", Critter.crit_names)

    def __init__ (self, name, hunger = 0, boredom = 0):

        hunger = random.randint(0,15)
        boredom = random.randrange (0,16)
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1
        Critter.crit_names.append (self.name)

    # def a "hidden" method only invoked by other methods

    def __pass_time (self):

        self.hunger += 1
        self.boredom += 1

    @property
    def mood (self): # mood method is a property, duh....
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "fine...."
        elif 10 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "F@$%ing ANGRY. Love me... (: <3"
        return m

    def talk (self):
        print ("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time ()

    def play (self, fun = 4):

        print ("How many hours would you like to play with", self.name, "(0-8)")
        fun = int(input("-----\t"))
        print ("Wheeee!!!!!!")
        self.boredom -= fun
        # keep self.boredom in check
        if self.boredom < 0:
            self.boredom = 0
        # call on the hidden propert pass time
        self.__pass_time ()

    def eat (self, eat = 4):

        print ("How many meals would you like to feed", self.name, "(0-8)")
        eat = int(input("-----\t"))
        print ("Yummy yummm yummmm. I love having", eat, "meals")
        self.hunger -= eat
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time ()

    # method to display and keep count of both hunger and boredom attributes
    # make it a __str__ method

    def __str__ (self):

        rep = str(self.name) + "'s hunger and boredom\n"
        rep += "Hunger:\t" + str(self.hunger) + "\n"
        rep += "Boredom:\t" + str(self.boredom) + "\n"

        return rep

def main ():
    # getting critter name

    crit_name = input ("What do you want to name your critter?:\t")
    crit_name2 = input ("What do you want to name your critter?:\t")
    crit_name3 = input ("What do you want to name your critter?:\t")

    #instantiating Critter object with name above
    crit = Critter (crit_name)
    crit2 = Critter (crit_name2)
    crit3 = Critter (crit_name3)

    choice = None
    while choice != "0":
        print \
            ("""
            Critter Caretaker

            0 - Exit
            1 - See how your critter feels
            2 - Feed your critter
            3 - Play with your critter
            4 - Show all critters in farm

            """)
        choice = input ("Choice:\t")

        if choice == "0":
            print ("Good-bye")

        elif choice == "1":
            crit.talk ()
            crit2.talk ()
            crit3.talk ()

        elif choice == "2":
            who = input("Which critter would you like to feed?:\t")
            if who == crit.name:
                crit.eat ()
            elif who == crit2.name:
                crit2.eat ()
            elif who == crit3.name:
                crit3.eat ()
            elif who == "all":
                crit.eat ()
                crit2.eat ()
                crit3.eat ()
            else:
                print ("That critter doesn't exist")

        elif choice == "3":
            who = input ("Which critter would you like to play with?:\t")
            if who == crit.name:
                crit.play ()
            elif who == crit2.name:
                crit2.play ()
            elif who == crit3.name:
                crit3.play ()
            elif who == "all":
                crit.play ()
                crit2.play ()
                crit3.play ()
            else:
                print ("That critter doesn't exist!")
        elif choice == "4":
            Critter.status ()

        elif choice == "5":
            print (crit)
            print (crit2)
            print (crit3)

        else:
            print ("Your choice is invalid")

main ()

input ("Press enter to exit")
            
    

    
            
        
    
