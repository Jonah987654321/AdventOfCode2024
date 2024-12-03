#https://adventofcode.com/2024/day/3
import re

inputs = ""
with open("inputs/day3.txt") as file:
    for line in file:
        inputs += line

# Part 1
total = 0
for op in re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", inputs):
    nums = op.lstrip("mul(").rstrip(")").split(",")
    total += int(nums[0])*int(nums[1])

print(total)


# Part 2
rest = inputs
total = 0
while rest:
    enabledUntil = re.search(r"don't\(\)", rest)
    operate = rest if enabledUntil is None else rest[:enabledUntil.span()[0]]
    for op in re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", operate):
        nums = op.lstrip("mul(").rstrip(")").split(",")
        total += int(nums[0])*int(nums[1])
    
    if enabledUntil is None:
        rest = ""
    else:
        tmp = rest[enabledUntil.span()[1]:]
        disabledUntil = re.search(r"do\(\)", tmp)
        rest = "" if disabledUntil is None else tmp[disabledUntil.span()[1]:]

print(total)
