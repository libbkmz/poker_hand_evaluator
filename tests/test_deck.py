from unittest import TestCase
from functools import reduce
from card import Card
from deck import Deck, CardSet


class TestDeck(TestCase):
    def test_deck_size(self):
        deck = Deck()
        self.assertEqual(len(deck), deck.CARDS_IN_DECK)

    def test_draw_del(self):
        HAND_SIZE = 2
        deck = Deck()

        self.assertEqual(len(deck), Deck.CARDS_IN_DECK)
        hand = deck.draw(HAND_SIZE)

        self.assertEqual(len(deck), Deck.CARDS_IN_DECK-HAND_SIZE)
        self.assertEqual(len(hand), HAND_SIZE)

    def test_deck_unpack(self):
        deck = Deck()
        a, b = deck.draw(2)
