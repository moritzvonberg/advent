from aocd import data, submit

lines = data.splitlines()

firsts = []
seconds = []

for line in lines:
    n1, n2 = map(int, line.split())
    firsts.append(n1)
    seconds.append(n2)

from collections import Counter

counts = Counter(seconds)

res = 0

for n in firsts:
    res += n * counts[n]
submit(res)
