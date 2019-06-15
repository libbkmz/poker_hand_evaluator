import random
import time
from unittest import TestCase, skip
from functools import reduce
from math import factorial as fac

from card import Card
from deck import Deck, CardSet


def _binomial(n, k):
    try:
        res = fac(n) // fac(k) // fac(n - k)
    except ValueError:
        res = -1
    return res


try:
    from scipy.special import binom  # n, k
except ImportError:
    binom = _binomial


class TestEvaluation(TestCase):
    # def setUp(self) -> None:
    #     super().setUp()
    #
    #     random.seed(time.time())
    #     random.seed(1)
    #
    #     self.deck = Deck()
    #     self.deck.shuffle()

    def test_card_rank_comparison_1(self):
        a, b = Card("c", "2"), Card("s", "3")

        self.assertTrue(a < b)
        self.assertFalse(a > b)
        self.assertFalse(a == b)

        # @TODO: implement
        # self.assertFalse(a >= b)
        # self.assertFalse(a <= b)

    def test_card_rank_comparison_2(self):
        a, b = Card("c", "2"), Card("s", "2")

        self.assertFalse(a < b)
        self.assertFalse(a > b)
        self.assertTrue(a == b)

    def test_hand_1(self):
        d1 = Deck()

        self.assertTrue(d1.draw(Deck.HAND_SIZE).evaluate())
        self.assertFalse(d1.draw(Deck.HAND_SIZE).evaluate())

    @skip
    def test_all_royal_flush(self):
        count = 0
        hand: CardSet
        for hand in Deck().get_all_combinations():
            if hand.is_royal_flush():
                count += 1

        self.assertEqual(
            count,
            len(Card.AVAI1LABLE_SUITS)
        )

    @skip
    def test_all_straight_flush(self):
        count = 0
        hand: CardSet
        for hand in Deck().get_all_combinations():
            if hand.is_straight_flush():
                count += 1

        self.assertEqual(
            count,
            (len(Card.AVAILABLE_RANKS)-(Deck.HAND_SIZE-1))*len(Card.AVAILABLE_SUITS)
        )

    @skip
    def test_flush(self):
        count = 0
        hand: CardSet

        for hand in Deck().get_all_combinations():
            if hand.is_flush():
                count += 1

        self.assertEqual(
            count,
            # C(13, 5) * 4 = 1287*4 = 5148
            binom(len(Card.AVAILABLE_RANKS), Deck.HAND_SIZE) * len(Card.AVAILABLE_SUITS)
        )

    def test_straight(self):
        count = 0
        hand: CardSet

        for hand in Deck().get_all_combinations():
            if hand.is_straight():
                count += 1

        self.assertEqual(
            count,
            (len(Card.AVAILABLE_RANKS) - (Deck.HAND_SIZE - 1) + 1) * (len(Card.AVAILABLE_SUITS) ** Deck.HAND_SIZE)
        )
