count = 0
lines = []
with open("aoc1.txt") as infile:
    lines = [int(x) for x in infile]

toComp = None
for i in range(len(lines) - 2):
    if toComp is not None and sum(lines[i: i+3]) > toComp:
        count += 1
    toComp = sum(lines[i:i+3])

print(count)