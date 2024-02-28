from card import Card
from random import shuffle

class Deck ():
    
    cards = []
    
    def __init__(self) -> None:
        pass

    def fill_deck(self):
        value_counter = 1
        color_counter = 1
        for i in range(1,53):
            
            x = Card("","")          
        
            x.value, color_counter = x.set_value(value_counter, color_counter)
            value_counter += 1
            x.color = x.set_color(color_counter)
            self.cards.append(x)
        return self.cards

    def __repr__(self) -> str:
        rep = self.cards
        return rep
    
    def print_deck(self):
        for i in range(len(self.cards)):
            print(f'{self.cards[i]}')

    def shuffle_deck(self):
        shuffle(self.cards)
        return self.cards