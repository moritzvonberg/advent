from collections import Counter

inlines = []

with open('lines.txt') as infile:
    inlines = [x.split(' -> ') for x in infile]

for i, line in enumerate(inlines):
    points = []
    for point in line:
        s1, s2 = point.rstrip('\n').split(',')
        points.append(((int(s1), int(s2))))
    
    inlines[i] = tuple(points)

filtered_inlines = [line for line in inlines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]

intersect_map = Counter()

for line in inlines:
    if line[0][0] == line[1][0]:
        start = min(line[0][1], line[1][1])
        end = max(line[0][1], line[1][1])
        for i in range(start, end + 1):
            intersect_map[(line[0][0], i)] += 1
    elif line[0][1] == line[1][1]:
        start = min(line[0][0], line[1][0])
        end = max(line[0][0], line[1][0])
        for i in range(start, end + 1):
            intersect_map[(i,line[0][1])] += 1
    else:
        xStep = 1 if line[0][0] < line[1][0] else -1
        yStep = 1 if line[0][1] < line[1][1] else -1
        xCoord = line[0][0]
        yCoord = line[0][1]
        for _ in range(abs(line[0][0] - line[1][0]) + 1):
            intersect_map[(xCoord, yCoord)] += 1
            xCoord += xStep
            yCoord += yStep

    
for point in intersect_map:
    intersect_map[point] -= 1

intersects = [x for x,y in intersect_map.items() if y > 0]
print(len(intersects))
