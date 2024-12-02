#https://adventofcode.com/2024/day/2

def checkSafe(r):
    levelType = None
    for i in range(1, len(r)):
        if i == 1:
            levelType = 1 if r[1] > r[0] else 2

        if abs(r[i]-r[i-1]) > 3 or abs(r[i]-r[i-1]) < 1 or (levelType == 1 and r[i]<r[i-1]) or (levelType == 2 and r[i]>r[i-1]):
            return i # Return index of bad level
    
    return 0 # Return 0 = no bad level found

# Part 1
reports = []
with open("inputs/day2.txt") as file:
    for line in file:
        reports.append([int(x) for x in line.split(" ")])

safe = sum(1 for r in reports if checkSafe(r) == 0)
print(safe)


# Part 2
safe = 0
for r in reports:
    badLvl = checkSafe(r)

    if badLvl != 0:
        suc = False

        for x in range(len(r)):
            toCheck = r.copy()
            toCheck.pop(x)

            if (checkSafe(toCheck) == 0):
                suc = True
                break

        if suc:
            safe += 1
    else:
        safe += 1

print(safe)
