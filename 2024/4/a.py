import itertools
from typing import Iterator
from aocd import data, submit

res = 0

board = data.splitlines()

to_find = "XMAS"

search_string_length = len(to_find)


def count_xmases(chars: Iterator[str]) -> int:
    res = 0

    index = 0
    reverse_index = 0

    for char in chars:
        if char == to_find[index]:
            index += 1
            if index >= search_string_length:
                res += 1
                index = 0
        else:
            index = 0 if char != to_find[0] else 1

        if char == to_find[search_string_length - reverse_index - 1]:
            reverse_index += 1
            if reverse_index >= search_string_length:
                res += 1
                reverse_index = 0
        else:
            reverse_index = 0 if char != to_find[-1] else 1
    return res


def iterate_horizontally(board: list[str]):
    for line in board:
        for char in line:
            yield char
        yield "."


def iterate_diagonally(board: list[str], right: bool):
    height = len(board)
    width = len(board[1])
    start_index_range = itertools.chain(
        zip(
            range(width - 1, 0, -1), itertools.repeat(0)
        ),  # intentionally doesn't include 0, 0 so we don't repeat
        zip(itertools.repeat(0), range(height)),
    )

    x_step = 1 if right else -1
    y_step = 1
    for start_x, start_y in start_index_range:
        x = start_x if right else width - start_x - 1
        y = start_y
        try:
            while True:
                if x < 0:
                    raise IndexError  # we don't want to restart on the other side for negative indices
                yield board[y][x]
                x += x_step
                y += y_step
        except IndexError:
            yield "."


def iterate_vertically(board):
    for chars in zip(*board):
        for char in chars:
            yield char
        yield "."


assert "".join(iterate_vertically(board)).split(".")[1] == "".join(
    line[1] for line in board
)


def iterate_all(board):
    return itertools.chain(
        iterate_horizontally(board),
        iterate_vertically(board),
        iterate_diagonally(board, right=False),
        iterate_diagonally(board, right=True),
    )


res = count_xmases(iterate_all(board))

test_data = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]

assert count_xmases(iterate_all(test_data)) == 18

print(res)

input()

submit(res)
