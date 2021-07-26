from card import Card
from deck import Deck

deck = Deck()
print(deck.count())
print(deck)
deck.shuffle()
print(deck.cards)
hand = deck.deal_hand(7)
print(deck)
print(hand)
