from collections import Counter
from math import log
from aocd import data, submit

stone_counts = Counter(int(num) for num in data.split())


def transform_stone(stone: int) -> tuple[int]:
    if stone == 0:
        return (1,)
    elif (num_digits := int(log(stone, 10)) + 1) % 2 == 0:
        threshold = 10 ** (num_digits // 2)
        return stone // threshold, stone % threshold
    else:
        return (stone * 2024,)


for step in range(75):
    new_stones = Counter()
    for stone, count in stone_counts.items():
        for new_stone in transform_stone(stone):
            new_stones[new_stone] += count
    stone_counts = new_stones


res = sum(stone_counts.values())

print(res)

input("enter to submit")

submit(res)
