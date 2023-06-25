with open("2019/day 1/input.txt") as infile:
    lines = infile.readlines()

answer = 0
for line in lines:
    answer += (int(line.rstrip()) // 3 - 2)
print(answer)

