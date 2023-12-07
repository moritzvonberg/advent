from collections import Counter
from dataclasses import dataclass

from aocd import get_data, submit


CARDS = "AKQJT98765432"[::-1]


@dataclass
class Hand:
    hand: str
    bid: int
    counts: Counter = None

    def __post_init__(self):
        self.counts = Counter(hand)

    def hand_ordering(self):
        return (CARDS.index(card) for card in self.hand)

    def __lt__(self, other: "Hand"):
        own_counts = self.counts.values()
        other_counts = other.counts.values()

        if max(own_counts) != max(other_counts):
            return max(own_counts) < max(other_counts)

        elif sorted(own_counts) != sorted(other_counts):
            return sorted(own_counts, reverse=True) < sorted(other_counts, reverse=True)

        else:
            return tuple(self.hand_ordering()) < tuple(other.hand_ordering())


data = get_data()
hands: list[Hand] = []

for line in data.splitlines():
    hand, bid = line.split()
    hands.append(Hand(hand, int(bid)))

hands.sort()

result = 0
for i, hand in enumerate(hands):
    result += (i + 1) * hand.bid

if result:
    submit(result, part="a", day=7)
