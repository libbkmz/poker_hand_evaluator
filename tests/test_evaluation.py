import random
import time
from unittest import TestCase, skip
from functools import reduce
from math import factorial as fac

import config as cfg
from card import Card
from deck import Deck, CardSet
from lookups import LookupTables


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


# +Royal Flush
# +Straight Flush
# +Four of a kind
# +Full House
# +Flush
# +Straight
# +Three of a kind
# Two Pair
# One Pair
# High Card
# https://www.cut-the-knot.org/Probability/PokerSampleSpaces.shtml
# http://people.math.sfu.ca/~alspach/comp18/

SUITS_NUM = len(Card.AVAILABLE_SUITS)
RANKS_NUM = len(Card.AVAILABLE_RANKS)
HAND_SIZE = cfg.HAND_SIZE
CARDS_IN_DECK = cfg.CARDS_IN_DECK

ROYAL_FLUSH_COUNT = SUITS_NUM
STRAIGHT_FLUSH_COUNT = (RANKS_NUM-(HAND_SIZE-1))*SUITS_NUM
FOUR_OF_KIND_COUNT = RANKS_NUM*(CARDS_IN_DECK-SUITS_NUM)
FULL_HOUSE_COUNT = binom(SUITS_NUM, 3) * RANKS_NUM * binom(4, 2) * (RANKS_NUM-1)
# C(13, 5) * 4 = 1287*4 = 5148
FLUSH_COUNT = binom(RANKS_NUM, HAND_SIZE) * SUITS_NUM
STRAIGHT_COUNT = (RANKS_NUM - (HAND_SIZE - 1) + 1) * (SUITS_NUM ** HAND_SIZE)

THREE_OF_KIND_COUNT = RANKS_NUM * binom(SUITS_NUM, 3)
THREE_OF_KIND_COUNT *= CARDS_IN_DECK - SUITS_NUM
THREE_OF_KIND_COUNT *= CARDS_IN_DECK - SUITS_NUM*2
THREE_OF_KIND_COUNT //= 2

TWO_PAIRS_COUNT = binom(RANKS_NUM, 2) * ((SUITS_NUM-1)*2)**2 * (CARDS_IN_DECK-(SUITS_NUM*2))

PAIR_COUNT = RANKS_NUM * ((SUITS_NUM-1)*2) * binom(RANKS_NUM-1, 3) * SUITS_NUM**3

class TestEvaluation(TestCase):
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

        self.assertTrue(d1.draw(cfg.HAND_SIZE).evaluate())
        self.assertFalse(d1.draw(cfg.HAND_SIZE).evaluate())

    # @skip
    def test_all_royal_flush(self):
        count = 0
        hand: CardSet
        for hand in Deck().get_all_combinations():
            if hand.is_royal_flush():
                count += 1

        self.assertEqual(
            count,
            ROYAL_FLUSH_COUNT
        )

    # @skip
    def test_all_straight_flush(self):
        count = 0
        hand: CardSet
        for hand in Deck().get_all_combinations():
            if hand.is_straight_flush():
                count += 1

        self.assertEqual(
            count,
            STRAIGHT_FLUSH_COUNT + ROYAL_FLUSH_COUNT
        )

    def test_full_house(self):
        count = 0
        hand: CardSet
        for hand in Deck().get_all_combinations():
            if hand.is_full_house():
                count += 1

        self.assertEqual(
            count,
            FULL_HOUSE_COUNT
        )

    def test_four_of_kind(self):
        count = 0
        hand: CardSet
        for hand in Deck().get_all_combinations():
            if hand.is_four_of_kind():
                count += 1

        self.assertEqual(
            count,
            FOUR_OF_KIND_COUNT
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
            FLUSH_COUNT
        )

    # @skip
    def test_straight(self):
        count = 0
        hand: CardSet

        for hand in Deck().get_all_combinations():
            if hand.is_straight():
                count += 1

        self.assertEqual(
            count,
            STRAIGHT_COUNT
        )

    def test_three_of_kind(self):
        count = 0
        hand: CardSet

        for hand in Deck().get_all_combinations():
            if hand.is_three_of_kind():

                count += 1

        self.assertEqual(
            count,
            THREE_OF_KIND_COUNT
        )

    def test_two_pairs(self):
        count = 0
        hand: CardSet

        for hand in Deck().get_all_combinations():
            if hand.is_two_pairs():
                count += 1

        self.assertEqual(
            count,
            TWO_PAIRS_COUNT
        )

    def test_one_pairs(self):
        count = 0
        hand: CardSet

        for hand in Deck().get_all_combinations():
            if hand.is_pair():
                count += 1

        self.assertEqual(
            count,
            PAIR_COUNT,
        )