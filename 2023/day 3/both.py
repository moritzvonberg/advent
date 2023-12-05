from collections import namedtuple
from dataclasses import dataclass
import re

from aocd import get_data, submit

data = get_data()

schematic = data.splitlines()
width = len(schematic[0])

def get_surrounding_characters(row_index: int, start: int, end: int) -> str:
    above = schematic[row_index - 1][max(start - 1, 0):min(end + 1, width)] if row_index > 0 else ""
    left = schematic[row_index][start - 1] if start > 0 else ""
    right = schematic[row_index][end] if end < width else ""
    below = schematic[row_index + 1][max(start - 1, 0):min(end + 1, width)] if row_index + 1 < len(schematic) else ""
    
    return "".join((above, left, right, below))


@dataclass
class Number:
    number: int
    row: int
    start: int
    end: int
    adjacent_symbols: set[str] = None
    
    def __post_init__(self):
        self.adjacent_symbols = set(get_surrounding_characters(self.row, self.start, self.end))


numbers = []

for line_index, line in enumerate(schematic):
    for found_number in re.finditer(r'\d+', line):
        numbers.append(Number(int(found_number.group()), line_index, found_number.start(), found_number.end()))

result = sum(number.number for number in numbers if number.adjacent_symbols != {'.'})

submit(result, part="a")

asterisk_coords = []

result_2 = 0

for line_index, line in enumerate(schematic):
    for char_index, char in enumerate(line):
        if char == "*":
            asterisk_coords.append((char_index, line_index))

# inefficient but fast enough
for x, y in asterisk_coords:
    if any(char.isdigit() for char in get_surrounding_characters(y, x, x + 1)):
        count = 0
        product = 1
        for number in numbers:
            if number.row < y - 1:
              continue  
            if (
                number.row - 1 <= y <= number.row + 1
                and number.start - 1 <= x <= number.end
            ):
                product *= number.number
                count += 1
            if number.row > y + 1:
                break
        if count == 2:
            result_2 += product

submit(result_2, "b")
