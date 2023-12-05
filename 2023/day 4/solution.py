from dataclasses import dataclass
from enum import Enum
from itertools import pairwise
import re
from typing import NamedTuple

from aocd import get_data, submit

data = get_data()

lines = data.splitlines()
mults = [1 for _ in lines]
score = 0
for i, line in enumerate(lines):
    _, stuff = line.split(": ")
    winning, own = stuff.split(" | ")
    winning = set(int(v) for v in winning.strip().split())
    own = set(int(v) for v in own.strip().split())
    own_winning = len(winning & own)

    if own_winning:
        for mult_index in range(i + 1, min(i + 1 + own_winning, len(mults))):
            mults[mult_index] += mults[i]
        score += 2 ** (own_winning - 1)
submit(score, part="a", day=4, year=2023)
submit(sum(mults), part="b", day=4, year=2023)