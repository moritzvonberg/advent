from aocd import data, submit

lines = data.splitlines()

firsts = []
seconds = []

for line in lines:
    n1, n2 = map(int, line.split())
    firsts.append(n1)
    seconds.append(n2)

firsts.sort()
seconds.sort()

res = 0
for n1, n2 in zip(firsts, seconds):
    res += abs(n1 - n2)
submit(res)
