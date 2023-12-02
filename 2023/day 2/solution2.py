from aocd import get_data, submit

data = get_data()

counts = {"red": 0, "green": 0, "blue": 0}

result = 0

for i, line in enumerate(data.splitlines()):
    game, rounds_str = line.split(": ")
    game_idx = int(game[5:])
    rounds = rounds_str.split("; ")
    possible = True

    round_counts = counts.copy()
    for round in rounds:
        for shown in round.split(", "):
            count, key = shown.split(" ")
            count = int(count)
            if count > round_counts[key]:
                round_counts[key] = count
    
    result += (round_counts["blue"] * round_counts["red"] * round_counts["green"])


if result:
    submit(result)