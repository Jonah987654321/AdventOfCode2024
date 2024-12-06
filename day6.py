#https://adventofcode.com/2024/day/6
import copy

labMap = []
with open("inputs/day6.txt") as file:
    for line in file:
        labMap.append([x for x in line.rstrip("\n")])

directions = ["^", ">", "v", "<"]

for row in range(len(labMap)):
    for column in range(len(labMap[0])):
        if labMap[row][column] in directions:
            current = labMap[row][column]
            posRow = row
            posColumn = column

startingPoint = [posRow, posColumn]
startDirection = current

# Part 1
visited = [[posRow, posColumn]]

while True:
    if current == "^":
        n_posRow = posRow-1
        n_posColumn = posColumn
    elif current == ">":
        n_posColumn = posColumn+1
        n_posRow = posRow
    elif current == "v":
        n_posRow = posRow+1
        n_posColumn = posColumn
    elif current =="<":
        n_posColumn = posColumn-1
        n_posRow = posRow

    if n_posColumn < 0 or n_posColumn >= len(labMap[0]) or n_posRow < 0 or n_posRow >= len(labMap):
        break

    if labMap[n_posRow][n_posColumn] == "#":
        cI = directions.index(current)
        current = directions[0] if cI == 3 else directions[cI+1]
    else:
        posRow = n_posRow
        posColumn = n_posColumn

        if not [posRow, posColumn] in visited:
            visited.append([posRow, posColumn])

print(len(visited))

# Part 2
success = 0
for row in range(len(labMap)):
    for column in range(len(labMap[0])):
        posRow = startingPoint[0]
        posColumn = startingPoint[1]
        current = startDirection
        if [row, column] != [posRow, posColumn]:

            newMap = copy.deepcopy(labMap)
            newMap[row][column] = "#"

            visited = {f"{posRow}|{posColumn}": current}

            while True:
                if current == "^":
                    n_posRow = posRow-1
                    n_posColumn = posColumn
                elif current == ">":
                    n_posColumn = posColumn+1
                    n_posRow = posRow
                elif current == "v":
                    n_posRow = posRow+1
                    n_posColumn = posColumn
                elif current =="<":
                    n_posColumn = posColumn-1
                    n_posRow = posRow

                if n_posColumn < 0 or n_posColumn >= len(newMap[0]) or n_posRow < 0 or n_posRow >= len(newMap):
                    break
                
                if newMap[n_posRow][n_posColumn] == "#":
                    cI = directions.index(current)
                    current = directions[0] if cI == 3 else directions[cI+1]
                else:    
                    posRow = n_posRow
                    posColumn = n_posColumn

                if f"{posRow}|{posColumn}" in visited.keys():
                    if visited[f"{posRow}|{posColumn}"] == current:
                        success += 1
                        break
                else:
                    visited[f"{posRow}|{posColumn}"] = current

print(success)
