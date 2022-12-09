lines = []

with open('day 22/input.txt') as infile:
    lines = [line.split() for line in infile]


print(lines)
lines = [[line[0]=='on', line[1].split(',')] for line in lines]
for i, line in enumerate(lines):
    cube_dict = dict()
    for param in line[1]:
        var_name = param[0]
        cube_dict[var_name+'_min'] = 

print(lines)