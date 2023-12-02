from aocd import get_data, submit

data = get_data()

allowed = {"red": 12, "green": 13, "blue": 14}

result = 0

for i, line in enumerate(data.splitlines()):
    game, rounds_str = line.split(": ")
    game_idx = int(game[5:])
    rounds = rounds_str.split("; ")
    possible = True
    for round in rounds:
        for shown in round.split(", "):
            count, key = shown.split(" ")
            if key not in allowed or allowed[key] < int(count):
                possible = False
                break
        if not possible:
            break
    if possible:
        result += game_idx



if result:
    submit(result)