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
                rep += str(card) + " "
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


# main

def main ():
    card1 = Card(rank = "A", suit = "♣")
    print ("\nPrinting a Card object:\t")
    print (card1)

    card2 = Card(rank = "2", suit = "♣")
    card3 = Card(rank = "3", suit = "♣")
    card4 = Card(rank = "4", suit = "♣")
    card5 = Card(rank = "5", suit = "♣")
    print ("\nPrinting the rest of the objects individually:\t")
    print (card1)
    print (card2)
    print (card3)
    print (card4)
    print (card5)
    
    # creating a Hand object and assigning it to my_hand
    my_hand = Hand ()
    print ("\nPrinting my hand before I add any cards:\t")
    print (my_hand)

    my_hand.add (card1)
    my_hand.add (card2)
    my_hand.add (card3)
    my_hand.add (card4)
    my_hand.add (card5)
    print ("\nPrinting my hand after adding 5 cards:\t")
    print (my_hand)

    # create another Hand object and using the .give () method
    ## transfer the first two cards from my_hand to your_hand
    your_hand = Hand ()
    my_hand.give (card1, your_hand)
    my_hand.give (card2, your_hand)
    print ("Your hand:\t")
    print (your_hand)
    print ("My hand:\t")
    print (my_hand)

    my_hand.clear ()
    print ("My hand after clearing it:\t")
    print (my_hand)
    print ("Your hand:\t", your_hand)
    

main ()
        

    
               
        
