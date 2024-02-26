import deck
import card

x = card.Card("","")
x.color = x.get_color
x.value = x.get_value
x.__repr__()
print(x)
new_deck = deck.Deck([],[])
new_deck.fill_deck()
'''test = new_deck.make_readable(new_deck.cards)
print(test)'''
print(new_deck.cards)


