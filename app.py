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
# for card in deck.cards:   
#     print(card)
#load player 1 and player 2 in function (board)
#add player class
#look up poker rule hierarchy 
#add subclass for player that is NPC player with a random function 
#1start with just comparing initial hands 
#2add turns,matches,and sets
#3add chips and betting functionality 
