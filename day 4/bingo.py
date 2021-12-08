def get_bingo_sets(board):
    result = []
    for i in range(5):
        result.append(set(board[i * 5:(i + 1) * 5]))
        result.append(set((board[i], board[5 + i], board[10 + i], board[15 + i], board[20 + i])))
    return(result)

#doesn't cover the case where there is no bingo in drawn nums but we don't care
def get_bingo_turn(bingo_sets, drawn_numbers):
    to_compare = set()
    is_bingo = [False] * 10
    turn = 0
    while(not any(is_bingo) and turn < len(drawn_numbers)):
        to_compare.add(drawn_numbers[turn])
        turn += 1
        is_bingo = [bingo_set.issubset(to_compare) for bingo_set in bingo_sets]
    return(turn if any(is_bingo) else -1)

def calculate_score_if_won(board, drawn_numbers, turn):
    result = sum(set(board) - set(drawn_numbers[:turn]))
    return(result * drawn_numbers[turn - 1])
    

drawn_numbers = None

boards = None

with open("bingo.txt") as infile:
    drawn_numbers = infile.readline()
    infile.readline()
    boards = infile.read().split('\n\n')

drawn_numbers = [int(num) for num in drawn_numbers.split(',')]
for i, board in enumerate(boards):
    boards[i] = " ".join(boards[i].split())
    boards[i] = [int(val) for val in boards[i].replace('\n', ' ').split(' ')]

last_bingo_turn = 0
last_bingo_index = 0
for i, board in enumerate(boards):
    bingo_turn = get_bingo_turn(get_bingo_sets(board), drawn_numbers)
    if bingo_turn > last_bingo_turn:
        last_bingo_index = i
        last_bingo_turn = bingo_turn

x = calculate_score_if_won(boards[last_bingo_index], drawn_numbers, last_bingo_turn)
print(x)


