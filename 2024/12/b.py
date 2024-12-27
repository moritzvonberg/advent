from collections import defaultdict
from collections.abc import Iterator
from enum import Enum
from typing import NamedTuple, Self
from aocd import data, submit

GRID = data.splitlines()


class Direction(Enum):

    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    def perpendicular_directions(self) -> tuple[Self]:
        horizontal_directions = (Direction.RIGHT, Direction.LEFT)
        vertical_directions = (Direction.UP, Direction.DOWN)
        x_offset, y_offset = self.value
        if x_offset:
            return vertical_directions
        elif y_offset:
            return horizontal_directions


class Group(NamedTuple):
    member_coords: set[tuple[int, int]]
    edge_coords: dict[tuple[int, int], set[tuple[int, int]]]
    key: str

    def price(self):
        return len(self.member_coords) * self.count_edges()

    def count_edges(self) -> int:
        edge_count = 0
        for direction in Direction:
            unseen_edge_coords_in_direction = set(
                coord
                for coord, directions in self.edge_coords.items()
                if direction in directions
            )

            while unseen_edge_coords_in_direction:
                edge_member_x, edge_member_y = unseen_edge_coords_in_direction.pop()
                for perpendicular_direction in direction.perpendicular_directions():
                    delta_x, delta_y = perpendicular_direction.value
                    candidate_x, candidate_y = (
                        edge_member_x + delta_x,
                        edge_member_y + delta_y,
                    )

                    while (candidate_x, candidate_y) in unseen_edge_coords_in_direction:
                        unseen_edge_coords_in_direction.remove(
                            (candidate_x, candidate_y)
                        )
                        candidate_x += delta_x
                        candidate_y += delta_y

                edge_count += 1
        return edge_count


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
        edge_coords = defaultdict(set)
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
                        neighbor_x, neighbor_y = neighbor
                        x, y = new_square_coord
                        edge_coords[new_square_coord].add(
                            Direction((neighbor_x - x, neighbor_y - y))
                        )
        return Group(group_coords, edge_coords, group_key)

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

TEST_1 = """AAAA
BBCD
BBCC
EEEC""".splitlines()

assert sum(group.price() for group in split_groups(TEST_1)) == 80

result = sum(group.price() for group in groups)

assert sum(len(group.member_coords) for group in groups) == len(GRID[0]) * len(GRID)

print(result)

input("enter to submit")

submit(result)
