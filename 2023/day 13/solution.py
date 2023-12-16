from itertools import pairwise

from aocd import get_data, submit


data = get_data(day=13, year=2023)

patterns = [row.splitlines() for row in data.split('\n\n')]

def to_number(chars):
    binary = "".join(chars).replace(".", '0').replace('#', '1')
    return int(binary, 2)

def get_symmetrical_indices(sequence):
    indices_of_symmetry = []
    for pair_index, _ in enumerate(pairwise(sequence), start=1):
        if all(left == right for (left, right) in zip(reversed(sequence[:pair_index]), sequence[pair_index:])):
            indices_of_symmetry.append(pair_index)
    return indices_of_symmetry

result = 0

for pattern in patterns:
    pattern_score = 0

    print('\n'.join(pattern))

    col_values = [to_number(col) for col in zip(*pattern)]
    row_values = [to_number(row) for row in pattern]

    print(f"{col_values=}")
    print(f"{row_values=}")

    row_symmetry_indices = get_symmetrical_indices(row_values)
    col_symmetry_indices = get_symmetrical_indices(col_values)

    print(f"{row_symmetry_indices=}")
    print(f"{col_symmetry_indices=}")

    pattern_score = sum(col_symmetry_indices) + sum(row_symmetry_indices) * 100
    print(f"{pattern_score=}")
    result += pattern_score

submit(result)
...