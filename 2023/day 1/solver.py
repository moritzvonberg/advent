from operator import itemgetter
import re

from aocd import get_data, submit

data = get_data()


words = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]
res = 0

for line in data.splitlines():
    found_nums = []
    for i, char in enumerate(line):
        if char.isdigit():
            found_nums.append((i, char))
    for i, word in enumerate(words):
        for match in re.finditer(word, line):
            found_nums.append((match.start(), str(i + 1)))

    found_nums.sort(key=itemgetter(0))

    numbers = "".join(digit for (_, digit) in sorted(found_nums, key=itemgetter(0)))
    res += int(numbers[0] + numbers[-1])

submit(res)