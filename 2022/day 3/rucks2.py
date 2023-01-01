rucks = []

from functools import reduce

with open("2022/day 3/input.txt") as infile:
    rucks = [x.strip() for x in infile.readlines()]

def content_prio(char: str) -> int:
    if not char.isalpha():
        return 0
    if char.islower():
        return ord(char) - ord("a") + 1
    else:
        return ord(char) - ord("A") + 27

ruck_iterators = [iter(rucks)] * 3
ruck_groups = zip(*ruck_iterators)
res = 0

for group in ruck_groups:
    intersect = reduce(lambda s1, s2: set(s1) & set(s2), group)
    if not len(intersect) == 1:
        raise ValueError("more than one common value in group")
    res += content_prio(intersect.pop())


print(res)
pass