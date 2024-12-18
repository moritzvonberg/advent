from aocd import data, submit
from itertools import pairwise

lines = data.splitlines()
reports = []
for line in lines:
    reports.append([int(s) for s in line.split()])


def is_safe(report):
    ordered = sorted(report)
    for prev, next_ in pairwise(report):
        if not 1 <= abs(prev - next_) <= 3:
            return 0
    return 1 if ordered == report or ordered[::-1] == report else 0


submit(sum(map(is_safe, reports)))
