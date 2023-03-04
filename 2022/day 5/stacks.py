from aocd import get_data
from aocd import submit

import re

lines = get_data(day=5).splitlines(keepends=False)
bottom_of_stacks_index = None
bottom_of_stacks = None
moves = None
for i, line in enumerate(lines):
    if line.startswith(" 1"):
        bottom_of_stacks = lines[i - 1]
        bottom_of_stacks_index = i - 1
    if line.startswith("move"):
        moves = lines[i:]
        break

offsets = []
stacks = []

move_parser = re.compile(r"move (\d+) from (\d) to (\d)")

for i, char in enumerate(bottom_of_stacks):
    if char.isalpha():
        offsets.append(i)
        stacks.append([char])

for line in lines[bottom_of_stacks_index - 1::-1]:
    for i, offset in enumerate(offsets):
        if line[offset].isalpha():
            stacks[i].append(line[offset])

for move in moves:
    print(f"doing {move}")
    count, source, destination = move_parser.findall(move)[0]
    for item in range(int(count)):
        stacks[int(destination) - 1].append(stacks[int(source) - 1].pop())

print(stacks)
result = "".join([stack[-1] for stack in stacks])

submit(result, part="a", day=5, year=2022)