from card import Card

class Deck ():
    
    def __init__(self, cards, shuffled_cards) -> None:
        self.cards = []
        self.shuffled_cards = []

    def fill_deck(self):
        value_counter = 1
        color_counter = 1
        for i in range(1,53):
            
            x = Card("","")          
        
            x.value, color_counter = x.set_value(value_counter, color_counter)
            value_counter += 1
            x.color = x.set_color(color_counter)
            self.cards.append(x)

    def __repr__(self, cards) -> str:
        rep = cards
        return rep
    
    def printdeck(self):
        for i in range(len(self.cards)):
            print(f'{self.cards[i]}')
