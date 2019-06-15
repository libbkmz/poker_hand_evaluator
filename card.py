from typing import Iterator


class Card:
    AVAILABLE_SUITS = {
        "c": 1 << 0,  # clubs
        "d": 1 << 1,  # diamonds
        "h": 1 << 2,  # hearts
        "s": 1 << 3,  # spades
    }
    AVAILABLE_RANKS = {
        "2": 1 << 0,
        "3": 1 << 1,
        "4": 1 << 2,
        "5": 1 << 3,
        "6": 1 << 4,
        "7": 1 << 5,
        "8": 1 << 6,
        "9": 1 << 7,
        "T": 1 << 8,
        "J": 1 << 9,
        "Q": 1 << 10,
        "K": 1 << 11,
        "A": 1 << 12,
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
