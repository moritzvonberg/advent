from collections import Counter

base = ""

with open("day 14/input.txt", 'r') as infile:
    lines = [line.strip() for line in infile.readlines()]

base = lines[0]
rules = [line.split("->") for line in lines if "->" in line]
rules = {rule[0].strip(): rule[1].strip() for rule in rules}

print(rules)
print(base)

def step():
    global base
    new_base = []
    for i in range(len(base) - 1):
        pair = base[i: i+2]
        new_base.append(pair[0] + rules[pair])
    new_base.append(base[-1])
    base = "".join(new_base)
for i in range(3):
    step()
    print(base)

counts = Counter(base)
print(counts.most_common()[0][1] - counts.most_common()[-1][1])