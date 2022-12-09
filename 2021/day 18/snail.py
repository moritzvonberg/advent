from ast import literal_eval

nums = []

with open('day 18/snailnums.txt') as infile:
    nums = [x.rstrip('\n') for x in infile]

x = literal_eval(nums[0])

print(x)