import functools
import itertools
import math
from operator import attrgetter, or_
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
    indices_on_destination: list[int]


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
                indices_on_destination=[index - loop_start for index in steps_on_destination if index >= loop_start]
            )
        visited_coordinates[(current, count % direction_period)] = count
    

# at this point after attempting a brute force approach, I checked all the cycles contained only one step that arrived at the destination per cycle

def normalize_loop(loop: Loop) -> Loop:
    return Loop(start=loop.start + loop.indices_on_destination[0], period=loop.period, indices_on_destination=[0])


def combined_loop(loop1: Loop, loop2: Loop) -> Loop:
    initial_relative_offset = loop1.start - loop2.start
    minimum_shift_between_loops = math.gcd(loop1.period, loop2.period)
    if initial_relative_offset and not initial_relative_offset % minimum_shift_between_loops == 0:
        return ValueError("Loops never overlap!")
     

def extended_gcd(a: int, b: int) -> tuple[int, int, int]

count = 0

starting_locations = [key for key in mapping.keys() if key.endswith("A")]

loops = [determine_loop(start, directions) for start in starting_locations]





submit(result, day=8, year=2023, part="b")