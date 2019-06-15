from unittest import TestCase
from functools import reduce
from card import Card


class TestCard(TestCase):
    def test_static_fields1(self):
        self.assertTrue(Card.AVAILABLE_SUITS)
        self.assertTrue(Card.AVAILABLE_RANKS)

        self.assertTrue(Card.REVERSE_SUITS)
        self.assertTrue(Card.REVERSE_RANKS)

    def test_static_fields2(self):
        self.assertEqual(
            Card.AVAILABLE_SUITS,
            {v: k for k, v in Card.REVERSE_SUITS.items()}
        )

        self.assertEqual(
            Card.AVAILABLE_RANKS,
            {v: k for k, v in Card.REVERSE_RANKS.items()}
        )

    def test_card_generations(self):
        all_cards = list(Card.generate_all_cards())
        self.assertEqual(
            reduce(lambda acc, x: x.suit_value + acc, all_cards, 0),
            13*1+13*2+13*4+13*8
        )
        self.assertEqual(
            reduce(lambda acc, x: x.rank_value + acc, all_cards, 0),
            ((1 << 13) - 1) * 4
        )
