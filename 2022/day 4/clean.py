with open("2022/day 4/input.txt") as infile:
    assignment_pairs = [x.strip().split(',') for x in infile.readlines()]

count = 0

for i, assignment_pair in enumerate(assignment_pairs):
    pair = []
    for assignment in assignment_pair:
        low, high = assignment.split('-')
        pair.append((int(low), int(high)))
    assignment_pairs[i] = pair

def fully_overlap(range1: int, range2: int) -> bool:
    return (range1[0] <= range2[0] and range1[1] >= range2[1]) or (range1[0] >= range2[0] and range1[1] <= range2[1])

for range1, range2 in assignment_pairs:
    if fully_overlap(range1, range2):
        print(f"range1:{range1}, range2:{range2}")
        count += 1
    

print(count)
