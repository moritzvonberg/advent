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
        self.coords = {coordinate}

    def __repr__(self) -> str:
        pass

    def do_step(self):
        next_step_coords = set()
        for coord in self.coords:
            for x, y in neigboring_coords(coord):
                if board[y][x] == self.step:
                    next_step_coords.add((x, y))
        self.step += 1
        self.coords = next_step_coords

    def calculate_score(self):
        while self.step <= 9:
            self.do_step()

        for x, y in self.coords:
            assert board[y][x] == 9

        return len(self.coords)


frontiers: list[Frontier] = []
for coord, val in iter_board():
    if val == 0:
        frontiers.append(Frontier(coord))

res = sum(frontier.calculate_score() for frontier in frontiers)

print(res)

input("enter to submit")

submit(res)
