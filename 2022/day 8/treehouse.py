from aocd import get_data, submit

data = get_data(year=2022, day=8).splitlines(keepends=False)
data = [[int(digit) for digit in line] for line in data]

visible_horizontal = set()
visible_vertical = set()

def get_visible_indices(line):
    result = []
    max_seen = line[0] - 1
    for i, tree_height in enumerate(line):
        if tree_height > max_seen:
            max_seen = tree_height
            result.append(i)
    max_seen_reverse = line[-1] - 1
    for i, tree_height in enumerate(line[::-1]):
        if tree_height > max_seen_reverse:
            max_seen_reverse = tree_height
            result.append(len(line) - (i + 1))
    return set(result)

for row_index, row in enumerate(data):
    for index in get_visible_indices(row):
        visible_horizontal.add((index, row_index))

for colunm_index, col in enumerate(zip(*data)):
    for index in get_visible_indices(col):
        visible_vertical.add((colunm_index, index))

upper_bound = 99 ** 2
lower_bound = (99 + 98) * 2

answer = len(visible_horizontal | visible_vertical)

if not (lower_bound <= answer <= upper_bound):
    print(f"answer {answer} not in [{lower_bound, upper_bound}], aborting")
    raise SystemExit

input(f"answer = {answer}. press anything to submit")

submit(answer=answer, part="a", year=2022, day=8)