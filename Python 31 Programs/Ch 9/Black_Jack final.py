
#Blackjack
## From 1 to 7 players compete against a dealer

import cards, games

# creating a class that inherits the Card class from the cards module
class BJ_Card (cards.Card):
    """A BLackjack Card """
    # constant for Ace Value
    ACE_VALUE = 1

    # create a property
    @property
    def value (self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index (self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

#creating a class that inherits the Deck Class from the module cards
class BJ_Deck (cards.Deck):
    """A Blackjack Deck """
    def populate (self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append (BJ_Card(rank, suit)) # if buggy check add vs append

# creating a class that inherits the Hand Class from the module cards

class BJ_Hand (cards.Hand):
    """ A Blackjack Hand """
    def __init__ (self, name):
        super (BJ_Hand, self).__init__ ()
        self.name = name

    def __str__ (self):
        rep = self.name + ":\t" + super (BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str (self.total) + ")"
        return rep

    # create property for total
    @property
    def total (self):
        # if a card in the hand has value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None

        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
            t += card.value

        # determine if hand contains an Ace
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        # if hand contains Ace and total is low enough, treat Ace as 11
        if contains_ace and t <= 11:
            # add only 10 since we've already added 1 for the Ace
            t += 10

        return t

    def is_busted (self):
        return self.total > 21



# create a class that inherits the BJ_Hand Class created above
class BJ_Player (BJ_Hand):
    """ A Blackjack Player """

    def is_hitting (self):
        response = games.ask_yes_no ("\n" + self.name + ", do you want to hit? (Y/N):\t")
        return response == "y"

    def bust (self):
        print (self.name, "busts!")
        self.lose ()

    def lose (self):
        print (self.name, "loses!")

    def win (self):
        print (self.name, "wins!!!")

    def push (self):
        print (self.name, "pushes.")

# create a class that inherits the BJ_Hand Class created above

class BJ_Dealer (BJ_Hand):
    """ A Blackjack Dealer """
    def is_hitting (self):
        return self.total < 17

    def bust (self):
        print (self.name, "busts!\t Table win!")

    def flip_first_card (self):
        first_card = self.cards [0]
        first_card.flip ()

# create the BJ_Game class

class BJ_Game (object):
    """ A Blackjack Game """
    # contructor method receives a list of names and creates a player for each name
    # also creates a dealer and deck
    def __init__ (self, names):
        self.players = []
        for name in names:
            player = BJ_Player (name)
            self.players.append (player)

        self.dealer = BJ_Dealer ("Dealer")

        self.deck = BJ_Deck ()
        self.deck.populate ()
        self.deck.shuffle ()


    @property
    def still_playing (self):
        sp = []
        for player in self.players:
            if not player.is_busted ():
                sp.append (player)

        return sp

    def __additional_cards (self, player):
        while not player.is_busted () and player.is_hitting ():
            self.deck.deal  ([player])
            print (player)
            if player.is_busted ():
                player.bust ()

    def play (self):
        # deal initial 2 cards to everyone
        self.deck.deal (self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card () # hide dealer's first card
        for player in self.players:
            print (player)
        print (self.dealer)

        # deal additional cards to players
        for player in self.players:
            self.__additional_cards (player)

        self.dealer.flip_first_card () # reveal dealer's first

        if not self.still_playing:
            # since all players have busted, just show dealer's hand
            print (self.dealer)
        else:
            # deal additional cards to dealer
            print (self.dealer)
            self.__additional_cards (self.dealer)

            if self.dealer.is_busted():
                #everyone still playing wins
                for player in self.still_playing:
                    player.win ()
            else:
                # compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win ()
                    elif player.total < self.dealer.total:
                        player.lose ()
                    else:
                        player.push ()

        # remove everyone's cards
        for player in self.players:
            player.clear ()
        self.dealer.clear ()


# main

def main ():
    print ("\t\tWelcome to Blackjack!\n")

    names = []
    number = games.ask_number("How many players? (1-7)\t:", low = 1, high = 8)
    for i in range (number):
        name = input ("Enter player name:\t")
        names.append (name)

    print ()

    game = BJ_Game (names)

    again = None
    while again != "n":
        game.play ()
        again = games.ask_yes_no ("\nDo you want to play again?:\t")


main ()
input ("\n\nPress Enter to exit")

        
                        
                
    

        
    
                
    
