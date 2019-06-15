from typing import Iterator

PRIME_NUMBERS = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
]


class Card:
    AVAILABLE_SUITS = {
        "c": 1 << 0,  # clubs
        "d": 1 << 1,  # diamonds
        "h": 1 << 2,  # hearts
        "s": 1 << 3,  # spades
    }
    # assume Ordered Dict
    AVAILABLE_RANKS = {
        "2": PRIME_NUMBERS[0],
        "3": PRIME_NUMBERS[1],
        "4": PRIME_NUMBERS[2],
        "5": PRIME_NUMBERS[3],
        "6": PRIME_NUMBERS[4],
        "7": PRIME_NUMBERS[5],
        "8": PRIME_NUMBERS[6],
        "9": PRIME_NUMBERS[7],
        "T": PRIME_NUMBERS[8],
        "J": PRIME_NUMBERS[9],
        "Q": PRIME_NUMBERS[10],
        "K": PRIME_NUMBERS[11],
        "A": PRIME_NUMBERS[12],
    }

    REVERSE_SUITS = None  # type: dict
    REVERSE_RANKS = None  # type: dict

    def __init__(self, suit: str, rank: str) -> None:
        self.suit_value = self.AVAILABLE_SUITS[suit]
        self.rank_value = self.AVAILABLE_RANKS[rank]

    @classmethod
    def generate_all_cards(cls):
        for suit, suit_value in cls.AVAILABLE_SUITS.items():
            for rank, rank_value in cls.AVAILABLE_RANKS.items():
                yield cls(suit, rank)

    def __repr__(self):
        return f"{self.REVERSE_SUITS[self.suit_value].lower()}{self.REVERSE_RANKS[self.rank_value].upper()}"

    def __lt__(self, other):
        if isinstance(other, Card):
            return self.rank_value.__lt__(other.rank_value)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank_value.__eq__(other.rank_value)
        else:
            return NotImplemented


Card.REVERSE_SUITS = {v: k for k, v in Card.AVAILABLE_SUITS.items()}
Card.REVERSE_RANKS = {v: k for k, v in Card.AVAILABLE_RANKS.items()}
