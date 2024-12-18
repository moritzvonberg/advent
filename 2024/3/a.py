from aocd import data, submit
import re

res = 0

for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", data):
    res += int(match.group(1)) * int(match.group(2))

print(res)

input()

submit(res)
