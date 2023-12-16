import bisect
import itertools
from operator import attrgetter
import re
from typing import NamedTuple

from aocd import get_data, submit

data = get_data(day=8, year=2023)

directions, instructions = data.split('\n\n')

mapping: dict[str, tuple[str, str]] = {}

for line in instructions.splitlines():
    match = re.match(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", line)
    source, left, right = (match.group(i) for i in range(1, 4))
    mapping[source] = (left, right)


class Loop(NamedTuple):
    start: int
    period: int
    indicies_on_destination: list[int]
    indices_on_destination_pre_loop: set[int]


def determine_loop(start, directions) -> Loop:
    print(f"finding loop from {start}")
    count = 0
    current = start
    choice = itertools.cycle(directions)
    visited_coordinates = {}
    visited_coordinates[(start, count)] = 0
    direction_period = len(directions)
    
    steps_on_destination = []
    while True:
        count += 1
        if current.endswith("Z"):
            steps_on_destination.append(count)
        current = mapping[current][0] if next(choice) == "L" else mapping[current][1]
        if (current, count % direction_period) in visited_coordinates:
            loop_start = visited_coordinates[(current, count % direction_period)]
            loop_end = count
            
            print(f"found first loop {loop_start=} and {loop_end=}")
            return Loop(
                start=loop_start,
                period=loop_end - loop_start,
                indicies_on_destination=[index - loop_start for index in steps_on_destination if index >= loop_start],
                indices_on_destination_pre_loop=set(index for index in steps_on_destination if index < loop_start),
                )
        visited_coordinates[(current, count % direction_period)] = count
    

class Searcher:
    def __init__(self, loop: Loop) -> None:
        self.loop_count = 0
        self.loop = loop
        self.considering = loop.indices_on_destination_pre_loop
        self.next_considering = None

    def __and__(self, other: "Searcher") -> set[int]:
        return self.considering & other.considering
    
    @property
    def index(self):
        return self.loop.start + self.loop_count * self.loop.period
    
    def generate_until(self, threshold: int):
        while not self.index >= threshold:
            self.loop_count += 1
            if self.index > threshold:
                to_add = [self.loop.start + num * self.loop_count for num in self.loop.indicies_on_destination]
                bisect_point = bisect.bisect(to_add, threshold)
                self.considering |= set(to_add[:bisect_point])
                self.next_considering = set(to_add[bisect_point:])
            else:    
                self.considering |= set(self.loop.start + num * self.loop_count for num in self.loop.indicies_on_destination)

    def discard_below_threshold(self):
        self.considering = self.next_considering


count = 0

starting_locations = [key for key in mapping.keys() if key.endswith("A")]

searchers = [Searcher(determine_loop(start, directions)) for start in starting_locations]

threshold = 0
increment = 100_000

result = 0
while True:
    threshold += increment
    for searcher in searchers:
        searcher.generate_until(threshold)
    
    if (overlaps := set.intersection(*(searcher.considering for searcher in searchers))):
        all_on_destination = overlaps
        break

    for searcher in searchers:
        searcher.discard_below_threshold()
    if threshold % increment * 10000 == 0:
        print(f"searched until {threshold}")

result = min(overlaps)


submit(result, day=8, year=2023, part="b")