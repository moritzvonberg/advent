with open("2019/day 1/input.txt") as infile:
    lines = infile.readlines()

def calc_fuel(mass):
    return mass // 3 - 2

answer = 0
for line in lines:
    mass = int(line.rstrip())
    while calc_fuel(mass) > 0:
        answer += calc_fuel(mass)
        mass = calc_fuel(mass)

print(answer)