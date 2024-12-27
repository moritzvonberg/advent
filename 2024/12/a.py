from collections.abc import Iterator
from typing import NamedTuple
from aocd import data, submit

GRID = data.splitlines()


class Group(NamedTuple):
    member_coords: set[tuple[int, int]]
    edge_count: int
    key: str

    def price(self):
        return len(self.member_coords) * self.edge_count


def split_groups(grid: list[str]):
    grid_width = len(grid[0])
    grid_height = len(grid)

    def get_grid_data_at(x, y) -> str | None:
        if not (0 <= x < grid_width and 0 <= y < grid_height):
            return None
        return grid[y][x]

    def iter_neighbors(x, y) -> Iterator[int | None]:
        for coord in ((x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)):
            yield coord

    def make_group(initial_coord) -> Group:
        edge_count = 0
        group_coords = set()
        group_key = get_grid_data_at(*initial_coord)
        frontier = {initial_coord}
        while frontier:
            new_square_coord = frontier.pop()
            group_coords.add(new_square_coord)
            for neighbor in iter_neighbors(*new_square_coord):
                if neighbor not in group_coords:
                    if get_grid_data_at(*neighbor) == group_key:
                        frontier.add(neighbor)
                    else:
                        edge_count += 1
        return Group(group_coords, edge_count, group_key)

    def make_groups(grid) -> list[Group]:
        to_visit = set()
        groups = []
        for y, row in enumerate(grid):
            for x, _ in enumerate(row):
                to_visit.add((x, y))

        while to_visit:
            coord = to_visit.pop()
            new_group = make_group(coord)

            to_visit -= new_group.member_coords

            groups.append((new_group))
        return groups

    return make_groups(grid)


groups = split_groups(GRID)

result = sum(group.price() for group in groups)

assert sum(len(group.member_coords) for group in groups) == len(GRID[0]) * len(GRID)

print(result)

input("enter to submit")

submit(result)
