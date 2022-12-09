from collections import deque

lines = []

with open('day 10/brackets.txt') as infile:
    lines = [line.rstrip('\n') for line in infile]

score_dict = {')': 1, ']' : 2, '}' : 3, '>' : 4}
bracket_dict = {'(': ')', '[': ']','{': '}','<': '>',}

scores = []

for line in lines:
    stack = deque()
    invalid = False
    for char in line:
        if char in ('<', '(', '{', '['):
            stack.append(bracket_dict[char])
        else:
            if char == stack[-1]:
                stack.pop()
            else:
                invalid = True
                break
    if not invalid:
        score_str = "".join(str(score_dict[x]) for x in stack)
        score = int(score_str[::-1], 5)
        scores.append(score)

scores.sort()
print(scores[len(scores) // 2])