move_pairs = []

with open("2022/day 2/input.txt") as infile:
    move_pairs = [x.strip().split(" ") for x in infile.readlines()]

score = 0
moves = ["rock", "paper", "scissors"] # for watch expressions
results = ["loss", "draw", "win"]
for move_pair in move_pairs:
    opponent_move_index = ord(move_pair[0]) - ord("A")
    result_index = ord(move_pair[1]) - ord("X")
    own_move_index = (opponent_move_index + (result_index - 1)) % 3

    score += 3 * result_index + own_move_index + 1

print(score)