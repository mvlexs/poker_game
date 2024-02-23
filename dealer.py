
from random import shuffle


class Dealer ():
    pot = 0
    centercard_1 = ""
    centercard_2 = ""
    centercard_3 = ""
    centercard_4 = ""
    centercard_5 = ""
    small_blind = 2
    big_blind = small_blind * 2
    deck = ["♤A","♤2","♤3","♤4","♤5","♤6","♤7","♤8","♤9","♤10","♤J","♤Q","♤K"]
    shuffled_deck = list

    def __init__(self, pot, centercard_1, centercard_2, centercard_3, centercard_4, centercard_5 , big_blind, small_blind, shuffled_deck, deck):
        self.deck = deck
        self.shuffled_deck = shuffled_deck

    def shuffle_cards(self):
        self.shuffled_deck = shuffle(self.deck)
        return self.shuffled_deck

        
        

        