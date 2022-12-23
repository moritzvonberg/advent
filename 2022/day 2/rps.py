move_pairs = []

with open("2022/day 2/input.txt") as infile:
    move_pairs = [x.strip().split(" ") for x in infile.readlines()]

score = 0
moves = ["rock", "paper", "scissors"]

for move_pair in move_pairs:
    opponent_move_index = ord(move_pair[0]) - ord("A")
    own_move_index = ord(move_pair[1]) - ord('X')
    
    own_move_score = own_move_index + 1
    win_loss_score = 3 * (((own_move_index - opponent_move_index) + 1) % 3)
    score += own_move_score + win_loss_score
print(score)