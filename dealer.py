
from random import shuffle
from deck import Deck

class Dealer ():
    pot = 0
    centercard_1 = ""
    centercard_2 = ""
    centercard_3 = ""
    centercard_4 = ""
    centercard_5 = ""
    small_blind = 2
    big_blind = small_blind * 2
    deck = Deck()
    deck.cards = deck.fill_deck()

    def __init__(self):#, pot, centercard_1, centercard_2, centercard_3, centercard_4, centercard_5 , big_blind, small_blind, shuffled_deck, deck):
        pass

    def get_deck(self):
        return self.deck.cards
        

   

        
        

        