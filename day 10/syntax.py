from collections import deque

lines = []

with open('day 10/brackets.txt') as infile:
    lines = [line.rstrip('\n') for line in infile]

score_dict = {')': 3, ']' : 57, '}' : 1197, '>' : 25137}
bracket_dict = {'(': ')', '[': ']','{': '}','<': '>',}

score = 0

for line in lines:
    stack = deque()
    for char in line:
        if char in ('<', '(', '{', '['):
            stack.append(bracket_dict[char])
        else:
            if char == stack[-1]:
                stack.pop()
            else:
                score += score_dict[char]
                break

print(score)