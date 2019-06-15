from random import shuffle
from typing import List, TypeVar, Iterator, Iterable
from operator import attrgetter,or_
from functools import reduce
from itertools import combinations
from card import Card

TCardSet = TypeVar("CardSet")

N = len(Card.AVAILABLE_RANKS)
ROYAL_FLUSH_NUMBER = 1 << N-1 | 1 << N-2 | 1 << N-3 | 1 << N-4 | 1 << N-5
# print(N, ROYAL_FLUSH_NUMBER)

STRAIGHT_MAP = {}


class CardSet:
    def __init__(self, cards: List[Card]) -> None:
        self._cards = cards  # List[Card]

    def draw(self, n):
        out = CardSet(self._cards[-n:])
        del self._cards[-n:]
        return out

    def shuffle(self) -> None:
        shuffle(self._cards)

    def is_royal_flush(self):
        rank_res = reduce(or_, self._get_set_ranks_or())
        suit_res = reduce(or_, self._get_set_suits_or())

        return (rank_res == ROYAL_FLUSH_NUMBER) and ((suit_res & (suit_res - 1)) == 0)

    def is_straight_flush(self):
        rank_res = reduce(or_, self._get_set_ranks_or())
        suit_res = reduce(or_, self._get_set_suits_or())

        return rank_res in STRAIGHT_MAP and ((suit_res & (suit_res - 1)) == 0)

    def is_four_of_kind(self):
        return NotImplemented

    def is_full_house(self):
        return NotImplemented

    def is_flush(self):
        suit_res = reduce(or_, self._get_set_suits_or())
        return (suit_res & (suit_res - 1)) == 0

    def is_straight(self):
        rank_res = reduce(or_, self._get_set_ranks_or())
        return rank_res in STRAIGHT_MAP




    def evaluate(self):
        assert len(self) == Deck.HAND_SIZE
        return self.is_royal_flush()

    # @TODO: rename
    def _get_set_ranks_or(self):
        return map(attrgetter("rank_value"), self)

    # @TODO: rename
    def _get_set_suits_or(self):
        return map(attrgetter("suit_value"), self)

    def get_all_combinations(self):
        for hand in combinations(self, Deck.HAND_SIZE):
            yield CardSet(hand)

    def __len__(self):
        return len(self._cards)

    def __iter__(self) -> Iterator[Card]:
        return self._cards.__iter__()

    def __repr__(self):
        out = ""
        for x in self:
            out += f"{x} "

        return f"Suit<{out.rstrip()}>"


class Deck(CardSet):
    CARDS_IN_DECK = 52
    HAND_SIZE = 5

    def __init__(self) -> None:
        super(Deck, self).__init__(list(Card.generate_all_cards()))


straight_value = 1 << 4 | 1 << 3 | 1 << 2 | 1 << 1 | 1 << 0
for i in range(len(Card.AVAILABLE_RANKS)-(Deck.HAND_SIZE-1)):
    value = straight_value << i
    # print(value, bin(value))
    STRAIGHT_MAP[value] = True

STRAIGHT_MAP[(straight_value >> 1) | (1 << (len(Card.AVAILABLE_RANKS)-1))] = True
