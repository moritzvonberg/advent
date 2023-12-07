from collections import Counter
from dataclasses import dataclass

from aocd import get_data, submit

result = 0

data = get_data()


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
        if max(self.counts.values()) != max(other.counts.values()):
            return max(self.counts.values()) < max(other.counts.values())
        elif sorted(self.counts.values()) != sorted(other.counts.values()):
            return sorted(self.counts.values(), reverse=True) < sorted(
                other.counts.values(), reverse=True
            )
        else:
            return tuple(self.hand_ordering()) < tuple(other.hand_ordering())


hands: list[Hand] = []

for line in data.splitlines():
    hand, bid = line.split()
    hands.append(Hand(hand, int(bid)))

hands.sort()

for i, hand in enumerate(hands):
    result += (i + 1) * hand.bid

if result:
    submit(result, part="b", day=7)
