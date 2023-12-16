import itertools
import re

from aocd import get_data, submit

data = get_data()

directions, mapping = data.split('\n\n')

map = {}

for line in mapping.splitlines():
    match = re.match(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", line)
    source, left, right = (match.group(i) for i in range(1, 4))
    map[source] = (left, right)

count = 0

choices = itertools.cycle(directions)

current = "AAA"

while current != "ZZZ":
    left, right = map[current]
    current = left if next(choices) == "L" else right
    count += 1

submit(count)