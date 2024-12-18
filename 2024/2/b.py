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
    return ordered == report or ordered[::-1] == report


def is_safe_tolerant(report):

    intervals = []
    asc = 0
    desc = 0
    for prev, next_ in pairwise(report):
        interval_in_range = 1 <= abs(prev - next_) <= 3
        is_ascending = prev < next_

        if is_ascending:
            asc += 1
        else:
            desc += 1
        intervals.append((interval_in_range, is_ascending))
    if min(asc, desc) > 1:
        return False

    expect_ascending = asc >= desc
    for i, (in_range, is_ascending) in enumerate(intervals):
        if not in_range or is_ascending != expect_ascending:
            return is_safe(report[:i] + report[i + 1 :]) or is_safe(
                report[: i + 1] + report[i + 2 :]
            )
    return is_safe(report)


submit(sum(map(is_safe_tolerant, reports)))
