from collections import Counter
from math import log
from aocd import data, submit

data_stones = [int(num) for num in data.split()]

test_stones = [125, 17]

counter = Counter()


def transform_stone(stone: int) -> tuple[int]:
    counter[stone] += 1
    if stone == 0:
        return (1,)
    elif (num_digits := int(log(stone, 10)) + 1) % 2 == 0:
        threshold = 10 ** (num_digits // 2)
        return stone // threshold, stone % threshold
    else:
        return (stone * 2024,)


def blink(stones: list[int]) -> list[int]:
    new_stones = []
    for stone in stones:
        to_add = transform_stone(stone)
        for new_stone in to_add:
            new_stones.append(new_stone)
    print(new_stones)
    return new_stones


assert transform_stone(0) == (1,)

assert transform_stone(12345678) == (1234, 5678)

assert transform_stone(2) == (4048,)

print(data_stones)

for step in range(25):
    data_stones = blink(data_stones)

res = len(data_stones)

print(counter)

print(res)

input("enter to submit")

submit(res)
