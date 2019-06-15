from unittest import TestCase
from functools import reduce
from card import Card
import config as cfg
from deck import Deck, CardSet


class TestDeck(TestCase):
    def test_deck_size(self):
        deck = Deck()
        self.assertEqual(len(deck), cfg.CARDS_IN_DECK)

    def test_draw_del(self):
        _HAND_SIZE = 2
        deck = Deck()

        self.assertEqual(len(deck), cfg.CARDS_IN_DECK)
        hand = deck.draw(_HAND_SIZE)

        self.assertEqual(len(deck), cfg.CARDS_IN_DECK-_HAND_SIZE)
        self.assertEqual(len(hand), _HAND_SIZE)

    def test_deck_unpack(self):
        deck = Deck()
        a, b = deck.draw(2)
