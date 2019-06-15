from typing import TYPE_CHECKING
from operator import itemgetter, mul
from functools import reduce
import config as cfg

if TYPE_CHECKING:
    from deck import Deck, CardSet

from card import Card


class LookupTablesClass:
    RANK_TABLE = {}
    ROYAL_FLUSH_PRODUCT = 0
    STRAIGHT_TABLE = {}
    FOUR_OF_KIND_TABLE = {}
    FULL_HOUSE_TABLE = {}
    THREE_OF_KIND = {}
    TWO_PAIRS = {}
    ONE_PAIR = {}
    HIGH_CARD = {}

    def __init__(self) -> None:
        self._rank_increment = 0
        # TODO: make correct order
        self.init_royal_flush()
        self.init_straight()
        self.init_four_of_kind()
        self.init_full_house()
        self.init_three_of_kind()
        self.init_two_pairs()
        self.init_one_pair()
        self.init_high_card()

    def init_royal_flush(self):
        # take TJQKA only
        royal_flush_rank = list(Card.AVAILABLE_RANKS.keys())[-cfg.HAND_SIZE:]
        royal_flush_rank_values = itemgetter(*royal_flush_rank)(Card.AVAILABLE_RANKS)
        product = reduce(mul, royal_flush_rank_values, 1)

        self.RANK_TABLE[product] = self.rank_increment()
        self.ROYAL_FLUSH_PRODUCT = product

    def init_straight(self):
        available_rank_keys = list(Card.AVAILABLE_RANKS.keys())
        for i in reversed(range(len(Card.AVAILABLE_RANKS) - (cfg.HAND_SIZE-1))):
            keys = available_rank_keys[i:i+cfg.HAND_SIZE]
            ranks = itemgetter(*keys)(Card.AVAILABLE_RANKS)
            product = reduce(mul, ranks, 1)

            self.STRAIGHT_TABLE[product] = self.rank_increment()
            # print(keys, ranks, product, self.RANK_TABLE[product])

        keys = [available_rank_keys[-1]] + available_rank_keys[:cfg.HAND_SIZE-1]
        ranks = itemgetter(*keys)(Card.AVAILABLE_RANKS)
        product = reduce(mul, ranks, 1)

        self.STRAIGHT_TABLE[product] = self.rank_increment()
        # print(keys, ranks, product, self.RANK_TABLE[product])

    def init_four_of_kind(self):
        for rank1, rank1_value in Card.AVAILABLE_RANKS.items():
            base_product = rank1_value ** len(Card.AVAILABLE_SUITS)

            for rank2, rank2_value in Card.AVAILABLE_RANKS.items():
                if rank1 == rank2:
                    continue

                product = base_product * rank2_value
                assert product not in self.FOUR_OF_KIND_TABLE
                self.FOUR_OF_KIND_TABLE[product] = self.rank_increment()

    def init_full_house(self):
        for rank1, rank1_value in Card.AVAILABLE_RANKS.items():
            base_product = rank1_value ** 3

            for rank2, rank2_value in Card.AVAILABLE_RANKS.items():
                if rank1 == rank2:
                    continue
                product = base_product * rank2_value ** 2
                self.FULL_HOUSE_TABLE[product] = self.rank_increment()

    def init_three_of_kind(self):
        for rank1, rank1_value in Card.AVAILABLE_RANKS.items():
            base_product = rank1_value ** 3
            for rank2, rank2_value in Card.AVAILABLE_RANKS.items():
                if rank1 == rank2:
                    continue
                for rank3, rank3_value in Card.AVAILABLE_RANKS.items():
                    if rank1 == rank3 or rank2 == rank3:
                        continue

                    product = base_product * rank2_value * rank3_value
                    self.THREE_OF_KIND[product] = self.rank_increment()

    def init_two_pairs(self):
        for rank1, rank1_value in Card.AVAILABLE_RANKS.items():
            base_product = rank1_value ** 2
            for rank2, rank2_value in Card.AVAILABLE_RANKS.items():
                if rank1 == rank2:
                    continue
                product1 = rank2_value ** 2
                for rank3, rank3_value in Card.AVAILABLE_RANKS.items():
                    if rank1 == rank3 or rank2 == rank3:
                        continue

                    product = base_product * product1 * rank3_value
                    self.TWO_PAIRS[product] = self.rank_increment()

    def init_one_pair(self):
        for rank1, rank1_value in Card.AVAILABLE_RANKS.items():
            base_product = rank1_value ** 2
            for rank2, rank2_value in Card.AVAILABLE_RANKS.items():
                if rank1 == rank2:
                    continue
                for rank3, rank3_value in Card.AVAILABLE_RANKS.items():
                    if rank1 == rank3 or rank2 == rank3:
                        continue
                    for rank4, rank4_value in Card.AVAILABLE_RANKS.items():
                        if rank1 == rank4 or rank2 == rank4 or rank3 == rank4:
                            continue

                        product = base_product * rank2_value * rank3_value * rank4_value
                        self.ONE_PAIR[product] = self.rank_increment()


    def init_high_card(self):
        pass



    def rank_increment(self):
        out = self._rank_increment
        self._rank_increment += 1
        return out

    @property
    def maximum_rank(self):
        self._rank_increment

    def __contains__(self, item):
        return item in self.RANK_TABLE





LookupTables = LookupTablesClass()
