from aocd import data, submit
import itertools

res = 0

board = data.splitlines()
height = len(board)
width = len(board[0])
res = 0

for x, y in itertools.product(range(1, width - 1), range(1, height - 1)):
    if board[y][x] == "A":
        up_left = board[y - 1][x - 1]
        up_right = board[y - 1][x + 1]
        down_left = board[y + 1][x - 1]
        down_right = board[y + 1][x + 1]

        corners = [up_left, up_right, down_left, down_right]

        if (
            corners.count("M") == 2
            and corners.count("S") == 2
            and up_left != down_right
        ):
            res += 1

print(res)

input("press enter to submit")

submit(res)
