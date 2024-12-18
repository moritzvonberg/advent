from collections import defaultdict
from aocd import data, submit

rules, pages = data.split("\n\n")

rules = [list(int(n) for n in line.split("|")) for line in rules.splitlines()]

pages = [list(int(n) for n in line.split(",")) for line in pages.splitlines()]

after_to_before_mapping = defaultdict(set)

for should_be_first, should_be_after in rules:
    after_to_before_mapping[should_be_after].add(should_be_first)

res = 0

for page in pages:
    seen = set()
    page_valid = True
    for i, update in enumerate(page):
        if update not in seen:
            if not seen <= after_to_before_mapping[update]:
                page_valid = False
            else:
                seen.add(update)
    if page_valid:
        res += page[i // 2]

print(res)

input("enter to submit\n")

submit(res)
