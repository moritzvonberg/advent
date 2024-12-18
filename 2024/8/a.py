from itertools import combinations
from aocd import data, submit
from collections import defaultdict

GRID = data.splitlines()

antennas = defaultdict(list)

for y, row in enumerate(GRID):
    for x, value in enumerate(row):
        if value != ".":
            antennas[value].append((x, y))
WIDTH = x + 1
HEIGHT = y + 1

antinodes = set()

for symbol, coords in antennas.items():
    for (x1, y1), (x2, y2) in combinations(coords, r=2):
        dx = x2 - x1
        dy = y2 - y1

        candidate_antinodes = (x2 + dx, y2 + dy), (x1 - dx, y1 - dy)

        for antinode in candidate_antinodes:
            antinode_x, antinode_y = antinode
            if 0 <= antinode_x < WIDTH and 0 <= antinode_y < HEIGHT:
                antinodes.add(antinode)

res = len(antinodes)

print(res)

input("enter to submit")

submit(res)
