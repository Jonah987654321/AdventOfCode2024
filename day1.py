#https://adventofcode.com/2024/day/1

list1 = []
list2 = []

with open("inputs/day1.txt", "r") as file:
    for line in file:
        data = line.split("   ")
        list1.append(int(data[0]))
        list2.append(int(data[1]))


# Part 1:
list1.sort()
list2.sort()

distance = 0

for x in range(len(list1)):
    distance += abs(list1[x]-list2[x])

print(distance)


# Part 2
appearances = {}
for x in list2:
    if x in appearances.keys():
        appearances[x] += 1
    else:
        appearances[x] = 1

simScore = 0
for x in list1:
    simScore += x*(appearances[x] if x in appearances else 0)

print(simScore)
