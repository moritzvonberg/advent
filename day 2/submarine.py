lines = []
with open("path.txt") as infile:
    lines = [x.split(' ') for x in infile]

aim = 0
pos = 0
depth = 0


for line in lines:
    val = int(line[1])
    if line[0] in ('forward', 'back'):
        if line[0] == 'forward':
            pos += val
            depth += aim * val
        else:
            pos -= val
            depth -= aim * val
    if line[0] in ('up', 'down'):
        if line[0] == 'down':
            aim += val
        else:
            aim -= val

print(depth * pos)