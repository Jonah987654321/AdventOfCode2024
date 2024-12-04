#https://adventofcode.com/2024/day/4

wordSearch = []
with open("inputs/day4.txt") as file:
    for line in file:
        wordSearch.append([x for x in line.rstrip("\n")])

# Part 1

def reverse(l):
    return list(reversed(l))

def generateDiagonals(matrix):
    def getDiagonal(matrix, offsetR = 0, offsetC = 0):
        x = offsetR
        y = offsetC
        d = []
        while x < len(matrix) and y < len(matrix[0]):
            d.append(matrix[x][y])
            x += 1
            y += 1
        return d
    ltr = [getDiagonal(matrix, x, 0) for x in range(len(matrix))]+[getDiagonal(matrix, 0, y) for y in range(1, len(matrix[0]))]
    rtl = [getDiagonal(reverse(matrix), x, 0) for x in range(len(matrix))]+[getDiagonal(reverse(matrix), 0, y) for y in range(1, len(matrix[0]))]
    return  ltr + rtl

count = 0

rows = wordSearch
columns = [[wordSearch[x][y] for x in range(len(wordSearch))] for y in range(len(wordSearch[0]))]
diagonals = generateDiagonals(wordSearch)

def searchArray(arr):
    return "".join(arr).count("XMAS")

for arr in [rows, columns, diagonals]:
    for line in arr:
        count += searchArray(line)
        count += searchArray(reverse(line))

print(count)


# Part 2

count = 0

for rowIndex in range(len(wordSearch)):
    for columnIndex in range(len(wordSearch[rowIndex])):
        if wordSearch[rowIndex][columnIndex] == "A":
            if rowIndex >= 1 and rowIndex <= len(wordSearch)-2 and columnIndex >= 1 and columnIndex <= len(wordSearch[rowIndex])-2:
                lrMatch = (wordSearch[rowIndex-1][columnIndex-1]=="M" and wordSearch[rowIndex+1][columnIndex+1]=="S") or (wordSearch[rowIndex-1][columnIndex-1]=="S" and wordSearch[rowIndex+1][columnIndex+1]=="M")
                rlMatch = (wordSearch[rowIndex-1][columnIndex+1]=="M" and wordSearch[rowIndex+1][columnIndex-1]=="S") or (wordSearch[rowIndex-1][columnIndex+1]=="S" and wordSearch[rowIndex+1][columnIndex-1]=="M")
                if lrMatch and rlMatch:
                    count += 1

print(count)
