import re
from re import findall, finditer

from aocd import get_data, submit

result = 1

data = get_data()

time, distance = data.splitlines()

_, *times = time.split()
_, *distances = distance.split()

for time, distance in zip(times, distances):
    time = int(time)
    distance = int(distance)
    count = 0
    for speed in range(1, time):
        if distance / speed < time - speed:
            count += 1
        elif count:
            break
    result *= count

if result:
    submit(result, part="a", day=6)

full_time = int(''.join(times))
full_distance = int(''.join(distances))

result_2 = 0
for speed in range(1, full_time):
    
    if full_distance / speed < full_time - speed:
        result_2 += 1
    else:
        if result_2:
            break

submit(result_2, part="b", day=6)