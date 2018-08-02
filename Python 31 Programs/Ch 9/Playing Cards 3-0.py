## Playing Cards
# Demonstrates combining objects

class Card (object):
    """ A Playing Card """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♣", "♦", "♥", "♠"]

    # constructor method to assign rank and suit
    def __init__ (self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    ## string representation of object method
    def __str__ (self):
        rep = self.rank + self.suit
        return rep



# creating a hand class for objects. It is a coolection of Card objects

class Hand (object):
    """ A Hand of Playing Cards """
    # initialisation method
    def __init__ (self):
        self.cards = []


    ## string representation of object method
    def __str__ (self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t "
        else:
            rep = "<empty>"
        return rep


    # method to clear the cards
    def clear (self):
        self.cards = []


    # method to add cards
    def add (self, card):
        self.cards.append (card)


    # method to give player a card from Deck
    def give (self, card, other_hand):
        self.cards.remove (card)
        other_hand.add (card)


# creating a class that inherits the Hand Class
# Hand is a base class because Deck is based on it
# Deck is a derived class because it derives part of it's definition from Hand
class Deck (Hand):
    """A deck of playing cards"""

    # no need for contructor method, already derived from Hand
    
    # define a method to populate the deck
    def populate (self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add (Card(rank,suit))

    # define a method to shuffle the deck
    def shuffle (self):
        import random
        random.shuffle (self.cards)

    # define a method to deal the cards
    def deal (self, hands, per_hand = 1):
        for rounds in range (per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards [0]
                    self.give (top_card, hand)
                else:
                    print ("Can't continue to deal. Out of cards!")


class Unprintable_Card (Card):
    """ A Card that won't reveal it's rank or suit when printed """
    ## Class inherits the __str__ method from the Class Card
    ## Overrides it
    def __str__ (self):
        return "<unprintable>"

class Positionable_Card (Card):
    """ A Card that can be face up or face down """
    ## Invoking the __str__ in Card Class but adjusting it
    def __init__ (self, rank, suit, face_up = True):
        # invokeds the method __str__ of superclass (Card)
        ## first arugment of super says, I want to invoke the superclass of
        ## that argument
        ### the second argument passes to the newly instanstiated PositionableCard
        ### object so that code in the Card class can get at the object to add the
        #### rank and suit attributes
        super(Positionable_Card, self).__init__ (rank, suit)
        self.is_face_up = face_up

    ## This method overrides a method inherited from the superclass
        ## and invokes this one instead
    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__ ()
        else:
            rep = "XX"
        return rep

    #extend the definition of this class without overriding the superclass
    # this method flips over the value of an objects face_up attribute
    ## changes it to opposite... if True = False and if False = True
    def flip (self):
        self.is_face_up = not self.is_face_up

# main
card1 = Card("A", "♣")
card2 = Unprintable_Card ("A", "♦")
card3 = Positionable_Card ("A", "♥")

# print the card object
print ("\nPrinting the card object")
print (card1)

# print an Unprintable_Card object
print ("\nPrinting an Unprintable_Card object")
print (card2)

# printing a Positionable_Card object
print ("\nPrinting a Positianable_Card object")
print (card3)

# invoking the flip () method of Positiniable_Card object
print ("\nFlipping the Positionable_Card object")
card3.flip ()
print ("\nPrinting the flipped card")
print (card3)

input ("\n\nPress Enter to exit")
        
        
        


    

               
        
