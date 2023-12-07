from collections import Counter
from dataclasses import dataclass

from aocd import get_data, submit

cards = "AKQT98765432J"[::-1]


@dataclass
class Hand:
    hand: str
    bid: int
    counts: Counter = None

    def __post_init__(self):
        self.counts = Counter(hand)
        if "J" in self.counts and self.hand != "JJJJJ":
            jacks = self.counts.pop("J")
            most_common_key, _ = self.counts.most_common(1)[0]
            self.counts[most_common_key] += jacks

    def hand_ordering(self):
        return (cards.index(card) for card in self.hand)

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
    submit(result, part="b", day=7)
