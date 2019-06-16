from random import shuffle
from typing import List, TypeVar, Iterator, Iterable
from operator import attrgetter, or_, mul
from functools import reduce
from itertools import combinations
from card import Card
import config as cfg
from lookups import LookupTables

TCardSet = TypeVar("CardSet")


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
        rank_res = self.get_rank_product()
        suit_res = reduce(or_, self.get_all_suits())

        return (rank_res == LookupTables.ROYAL_FLUSH_PRODUCT) and ((suit_res & (suit_res - 1)) == 0)

    def is_straight_flush(self):
        rank_res = self.get_rank_product()
        suit_res = reduce(or_, self.get_all_suits())

        return (rank_res in LookupTables.STRAIGHT_TABLE) and ((suit_res & (suit_res - 1)) == 0)

    def is_four_of_kind(self):
        rank_res = self.get_rank_product()
        return rank_res in LookupTables.FOUR_OF_KIND_TABLE

    def is_full_house(self):
        rank_res = self.get_rank_product()
        return rank_res in LookupTables.FULL_HOUSE_TABLE

    def is_flush(self):
        suit_res = reduce(or_, self.get_all_suits())
        return (suit_res & (suit_res - 1)) == 0

    def is_straight(self):
        rank_res = self.get_rank_product()
        return rank_res in LookupTables.STRAIGHT_TABLE

    def is_three_of_kind(self):
        rank_res = self.get_rank_product()
        return rank_res in LookupTables.THREE_OF_KIND

    def is_two_pairs(self):
        rank_res = self.get_rank_product()
        return rank_res in LookupTables.TWO_PAIRS

    def is_pair(self):
        rank_res = self.get_rank_product()
        return rank_res in LookupTables.ONE_PAIR

    def evaluate(self):
        assert len(self) == cfg.HAND_SIZE
        return self.is_royal_flush()

    def get_rank_product(self):
        return reduce(mul, self.get_all_ranks(), 1)

    def get_all_ranks(self):
        return map(attrgetter("rank_value"), self)

    def get_all_suits(self):
        return map(attrgetter("suit_value"), self)

    def get_all_combinations(self):
        for hand in combinations(self, cfg.HAND_SIZE):
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
    def __init__(self) -> None:
        super(Deck, self).__init__(list(Card.generate_all_cards()))
