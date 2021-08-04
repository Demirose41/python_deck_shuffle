import unittest
from deck import *
from card import *

class CardTests(unittest.TestCase):
    def setUp(self):
        self.test_card = Card(5,'hearts')
    def test_card_init(self):
        """Should make a card with a given value and suit"""
        self.assertEqual(
            self.test_card.suit, 'hearts'
        )
        self.assertEqual(self.test_card.value, 5)



if __name__ == '__main__':
    unittest.main()