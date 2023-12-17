from itertools import pairwise

from aocd import get_data, submit

data = get_data(day=13, year=2023)

patterns = [row.splitlines() for row in data.split('\n\n')]

def to_number(chars):
    binary = "".join(chars).replace(".", '0').replace('#', '1')
    return int(binary, 2)

def get_almost_symmetrical_index(sequence):
    for pair_index, _ in enumerate(pairwise(sequence), start=1):
        count = 0
        for (left, right) in zip(reversed(sequence[:pair_index]), sequence[pair_index:]):
            if left == right:
                continue
            bit_difference = left ^ right
            if bit_difference & (bit_difference - 1) == 0:  # difference is a power of two i.e. only one bit flipped
                count += 1
            else:
                count += 2  # slightly hacky way to terminate early
                break
        if count == 1:
            return pair_index
    return None

result = 0

for pattern in patterns:
    pattern_score = 0
    row_values = [to_number(row) for row in pattern]
    col_values = [to_number(col) for col in zip(*pattern)]
    row_smudge_line_index = get_almost_symmetrical_index(row_values)
    col_smudge_line_index = get_almost_symmetrical_index(col_values)
    assert (row_smudge_line_index is None) != (col_smudge_line_index is None)
    pattern_score = 100 * row_smudge_line_index if row_smudge_line_index else col_smudge_line_index
    result += pattern_score

submit(result, part="b", day=13)
