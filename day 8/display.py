lines = None
with open('day 8/day8.txt') as infile:
    lines = [x.rstrip('\n') for x in infile]

end_lines = [x.split('|')[1] for x in lines]

for i, x in enumerate(end_lines):
    end_lines[i] = [word for word in x.split() if len(word) in {2,3,4,7}]

print(sum([len(line) for line in end_lines]))