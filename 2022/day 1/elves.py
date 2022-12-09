with open("2022/day 1/input.txt") as infile:
    elves = infile.read().split('\n\n')
max_sum = 0
for elf in elves:
    elf_calories = sum((int(x) for x in elf.split('\n') if x != ""))
    if elf_calories > max_sum:
        max_sum = elf_calories

print(max_sum)
