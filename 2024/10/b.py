from aocd import data, submit

board = [[int(char) for char in line] for line in data.splitlines()]

height = len(board)
width = len(board[0])


def iter_board():
    for y, line in enumerate(board):
        for x, field in enumerate(line):
            yield ((x, y), field)


def neigboring_coords(coord):
    x, y = coord

    if x > 0:
        yield x - 1, y
    if y > 0:
        yield x, y - 1
    if x < width - 1:
        yield x + 1, y
    if y < height - 1:
        yield x, y + 1


class Frontier:
    def __init__(self, coordinate):
        self.step = 1
        self.original_coordinate = coordinate
        self.ways_to_get_to_coordinates = {coordinate: 1}

    def do_step(self):
        next_step_coords = {}
        for coord, ways_to_get_there in self.ways_to_get_to_coordinates.items():
            for x, y in neigboring_coords(coord):
                if board[y][x] == self.step:
                    try:
                        next_step_coords[(x, y)] += ways_to_get_there
                    except KeyError:
                        next_step_coords[(x, y)] = ways_to_get_there
        self.step += 1
        self.ways_to_get_to_coordinates = next_step_coords

    def calculate_score(self):
        while self.step <= 9:
            self.do_step()

        for x, y in self.ways_to_get_to_coordinates:
            assert board[y][x] == 9

        return sum(self.ways_to_get_to_coordinates.values())


frontiers: list[Frontier] = []
for coord, val in iter_board():
    if val == 0:
        frontiers.append(Frontier(coord))

res = sum(frontier.calculate_score() for frontier in frontiers)

print(res)

input("enter to submit")

submit(res)
