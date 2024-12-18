from aocd import data, submit
import re

res = 0

enabled = True
for match in re.finditer(r"(?:mul\((\d{1,3}),(\d{1,3})\))|(do(?:n't)?\(\))", data):

    if match.group(0) == "do()":
        enabled = True
    elif match.group(0) == "don't()":
        enabled = False
    elif enabled:
        res += int(match.group(1)) * int(match.group(2))

print(res)

input()

submit(res)
