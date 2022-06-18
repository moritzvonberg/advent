lines = []
basin_map = dict() #dict((x,y) -> basin_lowpoint

def is_lowest(line, col):
    up = line == 0 or lines[line][col] < lines[line - 1][col]
    down = line == len(lines) - 1 or lines[line][col] < lines[line + 1][col]
    left = col == 0 or lines[line][col] < lines[line][col - 1]
    right = col == len(lines[0]) - 1 or lines[line][col] < lines[line][col + 1]

    return all((up, down, left, right))

def get_lowest_neighbors_coords(line, col):
    res = []
    if lines[line][col] == 9:
        return None
    
    up = lines[line - 1][col] if line != 0 else 9
    down = lines[line + 1][col] if line != len(lines) - 1 else 9
    left = lines[line][col - 1] if col != 0 else 9
    right = lines[line][col + 1] if col != len(lines[0]) - 1 else 9
    
    minimum = min(up, down, left, right)
    if minimum == 9:
        return None
    else:
        if up == minimum:
            res.append((col, line - 1))
        if down == minimum:
            res.append((col, line + 1))
        if left == minimum:
            res.append((col - 1, line))
        if right == minimum:
            res.append((col + 1, line))
    return res

def add_path_coords_to_basin_map(coords, low_point):
    for coord in coords:
        basin_map[coord] = low_point
        
def gradient_descent(line, col, path=None):
    if not path:
        path = []
    if (col, line) in basin_map:
        add_path_coords_to_basin_map(path, basin_map[(col, line)])
    
    path.append((col, line))
    if is_lowest(line, col):
        add_path_coords_to_basin_map(path, (col, line))
    elif get_lowest_neighbors_coords(line, col):
        for y, x in get_lowest_neighbors_coords(line, col):

            if (x, y) not in path:
                gradient_descent(x, y, path)

with open("day 9/map.txt", 'r') as infile:
    lines = [list(int(num) for num in line if num != '\n') for line in infile.readlines()]


low_point_coords = []
low_point_sum = 0

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if is_lowest(y, x):
            low_point_coords.append((x, y))
            low_point_sum += lines[y][x] + 1

for line in range(len(lines)):
    for col in range(len(lines[0])):
        gradient_descent(line, col)

basins = dict() # dict((col, line): list[basin coords])

for k, v in basin_map.items():
    if v in basins:
        basins[v].append(k)
    else:
        basins[v] = [k]

sizes = sorted([len(coords) for _, coords in basins.items()])

print(low_point_coords)
print(low_point_sum) # solution 1
result = 1
for num in sizes[-3:]:
    result *= num
print(result)


