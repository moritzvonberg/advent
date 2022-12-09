from collections import deque
import bisect
with open("2022/day 1/input.txt") as infile:
    elves = infile.read().split('\n\n')

max_elves = deque((0,0,0), 3)
for elf in elves:
    elf_calories = sum((int(x) for x in elf.split('\n') if x != ""))
    if any(elf_calories > x for x in max_elves):
        max_elves.popleft()
        max_elves.insert(bisect.bisect(max_elves, elf_calories), elf_calories)

        

print(max_elves)
print(sum(max_elves))
