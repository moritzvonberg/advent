"""This code is meant to illustrate that you can detect all instances of numbers adjacent to symbols
without backtracking and is not a complete implementation."""

from itertools import pairwise
import re
from typing import NamedTuple

from aocd import get_data, submit

data = get_data()

schematic = data.splitlines()
width = len(schematic[0])


class NumberRange(NamedTuple):
    num: int
    search_bounds: range

def get_symbols_and_nums(schematic):
    for line in schematic:
        symbols = [
            range(match_.start() - 1, match_.end() + 1)
            for match_ in re.finditer(r"[%+!*]+", line)
            ]
        nums = [
            NumberRange(int(match_.group()), range(match_.start() - 1, match_.end() + 1))
            for match_ in re.finditer(r"\d+", line)
            ]
        yield symbols, nums

def check_overlap_and_pop(symbol_range, num_range: list) -> int:
    # find num ranges with overlap, then
    res = 0
    overlapping_nums = []
    for overlapping_num in overlapping_nums:
        res += overlapping_num.num
        num_range.remove(overlapping_num)
    return res

answer = 0

for (prev_symb, prev_nums), (curr_symb, curr_nums) in pairwise(get_symbols_and_nums(schematic)):
    answer += check_overlap_and_pop(curr_symb, prev_nums)
    answer += check_overlap_and_pop(prev_symb, curr_nums)

print(answer)





