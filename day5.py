#https://adventofcode.com/2024/day/5
import math

rules = []
updates = []

with open("inputs/day5.txt") as file:
    for line in file:
        if "|" in line:
            rules.append([int(x) for x in line.split("|")])
        elif "," in line:
            updates.append([int(x) for x in line.split(",")])

validSum = 0
invalidSum = 0

def checkValid(u):
    for r in rules:
        if r[0] in u and r[1] in u:
            if u.index(r[0]) > u.index(r[1]):
                return False
    return True


for u in updates:
    if checkValid(u):
        validSum += u[math.floor((len(u)-1)/2)]
    else:
        order = [u[0]]
        rest = u.copy()
        rest.pop(0)
        while len(rest) > 0:
            new = rest[0]
            rest.pop(0)

            appR = [r for r in rules if new in r]
            
            inserted = False
            for x in range(len(order)):
                appR_ref = [r for r in appR if new in r and order[x] in r]
                if len(appR_ref) > 0:
                    rule = appR_ref[0]
                    if rule.index(new) == 0:
                        order.insert(x, new)
                        inserted = True
                        break

            if not inserted:
                order.append(new)
            
        invalidSum += order[math.floor((len(order)-1)/2)]

print(validSum)
print(invalidSum)
