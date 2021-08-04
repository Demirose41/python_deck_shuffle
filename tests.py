import unittest
from deck import *
from card import *

class CardTests(unittest.TestCase):
    def setUp(self):
        self.test_card = Card(5,'hearts')

    def test_init(self):
        """Should make a card with a given value and suit"""
        self.assertEqual(self.test_card.suit, 'hearts')
        self.assertEqual(self.test_card.value, 5)
    
    def test_repr(self):
        """repr should return a string of the form 'VALUE of SUIT"""
        self.assertCountEqual(repr(self.test_card), '5 of hearst')

class DeckTests(unittest.TestCase):
    def setUp(self):
        self.test_deck = Deck()
    def test_init(self):
        """deck should have a cards attribute that is in the form of a list that has 52 entries"""
        self.assertTrue(isinstance(self.test_deck.cards, list))
        self.assertEqual(len(self.test_deck.cards),52)
    def test_repr(self):
        """repr should return Deck of LEN_OF_CARDS cards"""
        self.assertEqual(repr(self.test_deck), 'Deck of 52 cards')
    def test_count(self):
        """count should return the count of the number of cards remaining in the deck"""
        self.assertEqual(self.test_deck.count(),52)
        self.test_deck.cards.pop()
        self.assertEqual(self.test_deck.count(),51)
    def test_deal_sufficient_cards(self):
        """takes in a num value and checks that there are enough cards remaining in the deck to satisfy the request to deal said cards"""
        cards = self.test_deck._deal(10)
        self.assertEqual(len(cards),10)
        self.assertEqual(self.test_deck.count(),42)
    def test_deal_insufficient_cards(self):
        """deal should deal the number of cards left in the deck"""
        cards = self.test_deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.test_deck.count(),0)
    def test_deal_no_cards(self):
        """_deal should throw a ValueError if the deck is empty"""
        self.test_deck._deal(self.test_deck.count())
        with self.assertRaises(ValueError):
            self.test_deck._deal(1)
    def test_deal_card(self):
        """deal_card should deal  single card from the deck"""
        card = self.test_deck.cards[-1]
        dealt_card = self.test_deck.deal_card()
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.test_deck.count(),51)
    def test_deal_hand(self):
        """deal_hand should deal the number of cards passed"""
        cards = self.test_deck.deal_hand(20)
        self.assertEqual(len(cards),20)
        self.assertEqual(self.test_deck.count(), 32)

    def test_shuffle_full_deck(self):
        """Cards should shuffle the deck if the deck is full"""
        cards = self.test_deck.cards[:]
        self.test_deck.shuffle()
        self.assertNotEqual(cards, self.test_deck.cards)
    def test_shuffle_not_full_deck(self):
        self.test_deck._deal(1)
        with self.assertRaises(ValueError):
            self.test_deck.shuffle()

if __name__ == '__main__':
    unittest.main()