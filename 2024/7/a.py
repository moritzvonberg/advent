from aocd import data, submit

equations = []

for line in data.splitlines():
    expected, parts = line.split(": ")
    equations.append((int(expected), tuple(map(int, parts.split()))))

res = 0

for expected, parts in equations:
    possible_results = None
    for part in parts:
        next_step_possibilities = []
        if possible_results:
            for intermediate_value in possible_results:
                for candidate in (intermediate_value * part, intermediate_value + part):
                    if candidate <= expected:
                        next_step_possibilities.append(candidate)
        else:
            next_step_possibilities = [part]
        possible_results = next_step_possibilities
    if expected in next_step_possibilities:
        res += expected

print(res)

input("enter to submit")

submit(res)
