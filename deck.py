from card import Card

class Deck ():
    
    def __init__(self, cards, shuffled_cards) -> None:
        self.cards = []
        self.shuffled_cards = []

    def fill_deck(self):
        
        for i in range(1,53):
            x = Card("","")
            x = Card.__repr__(x)
            self.cards.append(x)

    def __repr__(self, cards) -> str:
        rep = cards
        return rep
    
