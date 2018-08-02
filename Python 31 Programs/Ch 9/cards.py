# Final Cards Module
## Basic classes for a game with playing cards

class Card (object):
    """A playing card"""
    # create CONSTANTS
    RANKS  = ["A", "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♣", "♦", "♥", "♠" ]

    # create a constructor method
    def __init__ (self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    # define a string representaion of object
    def __str__ (self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    ## def a method to flip the cards
    def flip (self):
        self.is_face_up = not self.is_face_up


#define a class for the hand
class Hand (object):
    """ A Hand of Playing Cards """
    def __init__ (self):
        self.cards = []

    ## string rep of object
    def __str__ (self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<empty>"
        return rep

    # define a method to clear the current hand

    def clear (self):
        self.cards = []

    # a method to add cards to hand

    def add (self, card):
        self.cards.append (card)

    # def a method to give the cards from one hand to the other
    def give (self, card, other_hand):
        self.cards.remove (card)
        other_hand.add (card)


class Deck (Hand):
    """ A Deck of Playing Cards """
    # a method to populate the deck
    def populate (self):
        for suit in Cards.SUITS:
            for rank in Cards.RANKS:
                self.add (Cards(rank, suit))

    # method to shuffle the cards
    def shuffle (self):
        import random
        random.shuffle (self.cards)

    # method to deal the cards
    def deal (self, hands, per_hand = 1):
        for rounds in range (per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards [0]
                    self.give (top_card, hand)
                else:
                    print ("Can't continue to deal. Out of cards!")

## function to only allow this module to be used if imported

if __name__ == "__main__":
    print ("This is a module with classes for playing cards")
    input ("\n\nPress Enter to exit")

