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



# main

deck1 = Deck ()


print ("Created a new deck")
print ("Deck:\t")
print (deck1)

deck1.populate ()
print ("\nPopulated the deck")
print ("Deck:\t")
print (deck1)

deck1.shuffle ()
print ("\nShuffled the deck:\t")
print (deck1)

# create two Hand objects and assing them to list hands []
my_hand = Hand ()
your_hand = Hand ()
hands = [my_hand, your_hand]
# deal each hand five cards
deck1.deal(hands, per_hand = 5)

print ("\nDealt 5 cards to my hand and your hand")
print ("\nMy hand:\t")
print (my_hand)
print ("\nYour hand:\t")
print (your_hand)
print ("Deck:\t")
print (deck1)


# clearing the deck

deck1.clear ()
print ("\nCleared the deck")
print ("Deck:\t", deck1)

input ("\n\nPress Enter to exit")


    

               
        
