from aocd import data, submit

board = data.splitlines()

starting_coord = None
obstacles = set()
considered_extra_obstacles = set()

for y_index, line in enumerate(board):
    for x_index, char in enumerate(line):
        if char == "#":
            obstacles.add((x_index, y_index))
        if char == "^":
            starting_coord = x_index, y_index
            considered_extra_obstacles.add(starting_coord)
height = y_index + 1
width = x_index + 1


def walk(start_x, start_y):
    loop_causing_obstacles = set()
    x = start_x
    y = start_y
    dx = 0
    dy = -1
    already_visited = set()
    while (0 <= x < width) and (0 <= y < height):
        already_visited.add((x, y, dx, dy))
        print(f"walk: {x, y}")
        if obstacle_in_front_of_pos_causes_loop(x, y, dx, dy, already_visited) and not (
            x + dx == start_x and y + dy == start_y
        ):
            loop_causing_obstacles.add((x + dx, y + dy))
        new_x, new_y = x + dx, y + dy
        if (new_x, new_y) in obstacles:
            dx, dy = -dy, dx  # right rotation
        else:
            x = new_x
            y = new_y
    return loop_causing_obstacles


def obstacle_in_front_of_pos_causes_loop(x, y, dx, dy, already_visited: set):
    visited_after = set()

    extra_obstacle_x = x + dx
    extra_obstacle_y = y + dy

    if (extra_obstacle_x, extra_obstacle_y) in obstacles:
        return False

    if (extra_obstacle_x, extra_obstacle_y) in considered_extra_obstacles:
        return False

    if not (0 <= extra_obstacle_x < width and 0 <= extra_obstacle_y < height):
        return False  # this is the most frustrating thing to overlook, I was off by one for SO long

    considered_extra_obstacles.add((extra_obstacle_x, extra_obstacle_y))

    while (0 <= x < width) and (0 <= y < height):
        visited_after.add((x, y, dx, dy))
        new_x, new_y = x + dx, y + dy
        if (new_x, new_y) in obstacles or (extra_obstacle_x, extra_obstacle_y) == (
            new_x,
            new_y,
        ):
            dx, dy = -dy, dx  # right rotation
            newly_visited = (x, y, dx, dy)
            if newly_visited in already_visited or newly_visited in visited_after:
                return True
        else:
            newly_visited = (new_x, new_y, dx, dy)
            if newly_visited in already_visited or newly_visited in visited_after:
                return True
            x = new_x
            y = new_y
    return False


looping_obstacles = walk(*starting_coord)

res = len(looping_obstacles)

print(res)

input("enter to submit\n")

submit(res)
