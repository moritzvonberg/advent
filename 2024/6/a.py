from collections import defaultdict
import bisect
import itertools
from aocd import data, submit

print(data)
board = data.splitlines()

obstacles_x = defaultdict(list)
obstacles_y = defaultdict(list)

starting_coord = None
visited = set()
directions = [
    ("y", False),
    ("x", True),
    ("y", True),
    ("x", False),
]

for y, line in enumerate(data.splitlines()):
    for x, char in enumerate(line):
        if char == "#":
            obstacles_x[y].append(x)
            obstacles_y[x].append(y)
        if char == "^":
            starting_coord = x, y
            visited.add((x, y))
height = y + 1
width = x + 1


def print_board(visited_set: set):
    out = []
    for y in range(len(board)):
        outline = []
        for x in range(len(board[0])):
            if board[y][x] == "^":
                outline.append("^")
            elif (x, y) in visited:
                outline.append("X")
            else:
                outline.append(board[y][x])
        out.append("".join(outline))
    print("\n".join(out))


movement_directions = itertools.cycle(directions)

x_pos, y_pos = starting_coord
while True:
    current_direction = next(movement_directions)
    axis_name, positive_direction = current_direction
    current_axis_is_x_axis = axis_name == "x"
    axis_obstacles = (
        obstacles_x[y_pos] if current_axis_is_x_axis else obstacles_y[x_pos]
    )
    next_obstacle_coordinate_index = bisect.bisect(
        axis_obstacles, x_pos if current_axis_is_x_axis else y_pos
    )
    if positive_direction:
        if next_obstacle_coordinate_index >= len(axis_obstacles):
            for pos in range(
                x_pos if current_axis_is_x_axis else y_pos,
                width if current_axis_is_x_axis else height,
            ):
                visited.add((pos, y_pos) if current_axis_is_x_axis else (x_pos, pos))
            if current_axis_is_x_axis:
                x_pos = width - 1
            else:
                y_pos = height - 1
            break
        else:
            for pos in range(
                x_pos if current_axis_is_x_axis else y_pos,
                axis_obstacles[next_obstacle_coordinate_index],
            ):
                visited.add((pos, y_pos) if current_axis_is_x_axis else (x_pos, pos))
            if current_axis_is_x_axis:
                x_pos = axis_obstacles[next_obstacle_coordinate_index] - 1
            else:
                y_pos = axis_obstacles[next_obstacle_coordinate_index] - 1

    else:
        if next_obstacle_coordinate_index <= 0:
            for pos in range(x_pos + 1 if current_axis_is_x_axis else y_pos + 1):
                visited.add((pos, y_pos) if current_axis_is_x_axis else (x_pos, pos))
            if current_axis_is_x_axis:
                x_pos = 0
            else:
                y_pos = 0
            break
        else:
            for pos in range(
                axis_obstacles[next_obstacle_coordinate_index - 1] + 1,
                x_pos + 1 if current_axis_is_x_axis else y_pos + 1,
            ):
                visited.add((pos, y_pos) if current_axis_is_x_axis else (x_pos, pos))
            if current_axis_is_x_axis:
                x_pos = axis_obstacles[next_obstacle_coordinate_index - 1] + 1
            else:
                y_pos = axis_obstacles[next_obstacle_coordinate_index - 1] + 1

res = len(visited)

print_board(visited)

print(res)

input("enter to submit\n")

submit(res)
