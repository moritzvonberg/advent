rucks = []

with open("2022/day 3/input.txt") as infile:
    rucks = [x.strip() for x in infile.readlines()]

def content_prio(char: str) -> int:
    if not char.isalpha():
        return 0
    if char.islower():
        return ord(char) - ord("a") + 1
    else:
        return ord(char) - ord("A") + 27

rucks = [(ruck[:len(ruck) // 2], ruck[len(ruck) // 2:]) for ruck in rucks]

res = 0

for ruck1, ruck2 in rucks:
    shared = set(ruck1) & set(ruck2)
    if not len(shared) == 1:
        raise ValueError("ruck has more than one common element")
    res += content_prio(shared.pop())
print(res)
pass