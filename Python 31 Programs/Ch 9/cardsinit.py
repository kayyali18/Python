# making classes for a game with playing  cards

class Card (object):
    """A playing card"""
    # create CONSTANTS
    RANKS  = ["A", "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♣", "♦", "♥", "♠" ]

    # initialisation method
    def __init__ (self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__ (self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    #def a method to flipp the cards
    def flip (self):
        self.is_face_up = not self.is_face_up

# create a class for a hand of playing cards

def Hand (object):
    """A hand of playing cards"""
    # constructor method

    def __init__ (self):
        self.cards = [] #set cards to empty list

    def __str__ (self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<empty>"
        return rep

    # create a method to clear the hand

    def clear (self):
        self.cards = []

    # define a method to add cards to hand i.e. the list
    def add (self, card):
        self.cards.append (card)

    def give (self, card, other_hand):
        self.cards.remove (card)
        other_hand.add (card)

# create a class for a deck of cards

def Deck (Hand):
    """A deck of playing cards"""
    ## a method to populate the deck using the Hand class and RANK AND SUITS 
    def populate (self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add (Card(rank, suit))

    # a method to shuffle the deck

    def shuffle (self):
        import random
        random.shuffle (self.cards)

    # a method to deal

    def deal (self, hands, per_hand = 1):
        for rounds in range (per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards [0]
                    self.give (top_card, hand)
                else:
                    print ("Can't continue deal. Out of cards!")


if __name__ == "__main__":
    print ("This is a module with classes for playing cards")
    input ("\n\nPress Enter to exit")
    
        
