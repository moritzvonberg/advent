from collections import defaultdict
from aocd import data, submit

rules, pages = data.split("\n\n")

rules = [list(int(n) for n in line.split("|")) for line in rules.splitlines()]

pages = [list(int(n) for n in line.split(",")) for line in pages.splitlines()]

after_to_before_mapping = defaultdict(set)

for should_be_first, should_be_after in rules:
    after_to_before_mapping[should_be_after].add(should_be_first)

res = 0


def reorder_updates(page):
    updates = set(page)
    relevant_rules = {
        update: len(after_to_before_mapping[update] & updates) for update in updates
    }
    ordered = sorted(relevant_rules.items(), key=lambda x: x[1])
    for i, (update, num_before) in enumerate(ordered):
        assert num_before == i
    return [update for update, _ in ordered]


for page in pages:
    seen = set()
    page_valid = True
    for i, update in enumerate(page):
        if update not in seen:
            if not seen <= after_to_before_mapping[update]:
                res += reorder_updates(page)[len(page) // 2]
                break
            else:
                seen.add(update)

print(res)

input("enter to submit\n")

submit(res)
