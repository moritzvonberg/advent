from operator import itemgetter
import re

from aocd import get_data, submit

data = get_data()

words = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]

word_values = {word: str(i + 1) for i, word in enumerate(words)}
word_pattern = '|'.join(words)
lookahead_pattern = f"(?=({word_pattern}))"

res = 0
for line in data.splitlines():
    found_nums = []
    for i, char in enumerate(line):
        if char.isdigit():
            found_nums.append((i, char))
    for match in re.finditer(lookahead_pattern, line):
        found_nums.append((match.start(1), word_values[match.group(1)]))

    found_nums.sort(key=itemgetter(0))

    numbers = "".join(digit for (_, digit) in sorted(found_nums, key=itemgetter(0)))
    res += int(numbers[0] + numbers[-1])

submit(res)