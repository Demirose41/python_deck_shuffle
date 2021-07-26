from card import Card

class Deck :
    def __init__(self):    
        suits = ['Hearts','Diamonds','Clubs','Spades']
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']  
        self.cards = [ Card(value,suit) for suit in suits for value in values]
    def __repr__(self):
        return f'Deck of {self.count()} cards'

    def count(self):
        return len(self.cards)



deck = Deck()
print(deck.count())
print(deck)


