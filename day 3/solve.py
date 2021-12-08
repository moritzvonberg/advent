import copy

lines = []
with open('new 4.txt') as infile:
    lines = [str(x).replace('\n', '') for x in infile]
index = 0
temp_lines = copy.copy(lines)


while index < 12 and len(temp_lines) > 1:
    current = [x[index] for x in temp_lines]
    if current.count('0') > current.count('1'):
        temp_lines = [x for x in temp_lines if x[index] == '0']
    else:
        temp_lines = [x for x in temp_lines if x[index] == '1']
    index += 1

most_res = temp_lines[0]

print(most_res)
temp_lines = copy.copy(lines)

index = 0
while index < 12 and len(temp_lines) > 1:
    current = [x[index] for x in temp_lines]
    if current.count('0') <= current.count('1'):
        temp_lines = [x for x in temp_lines if x[index] == '0']
    else:
        temp_lines = [x for x in temp_lines if x[index] == '1']
        
    index += 1

least_res = temp_lines[0]

print(least_res)

print(int(most_res, 2) * int(least_res, 2))

    


