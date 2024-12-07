#https://adventofcode.com/2024/day/7
import copy

eq = []
with open("inputs/day7.txt") as file:
    for line in file:
        data = line.rstrip("\n").split(": ")
        eq.append({"value": int(data[0]), "operation": [int(x) for x in data[1].split(" ")]})


# Part 1

successTests = 0
for e in eq:
    stack = [{"alr": e["operation"][0], "rem": e["operation"][1:].copy()}]
    while len(stack) > 0:
        task = stack[0]
        stack.pop(0)

        if task["alr"]*task["rem"][0] <= e["value"]:
            newTask = copy.deepcopy(task)
            newTask["alr"] = task["alr"]*task["rem"][0]
            newTask["rem"].pop(0)

            if len(newTask["rem"]) == 0:
                if newTask["alr"] == e["value"]:
                    successTests += e["value"]
                    break
            else:
                stack.insert(0, newTask)
        
        if task["alr"]+task["rem"][0] <= e["value"]:
            newTask = copy.deepcopy(task)
            newTask["alr"] = task["alr"]+task["rem"][0]
            newTask["rem"].pop(0)

            if len(newTask["rem"]) == 0:
                if newTask["alr"] == e["value"]:
                    successTests += e["value"]
                    break
            else:
                stack.insert(0, newTask)

print(successTests)


# Part 2

successTests = 0
for e in eq:
    stack = [{"alr": e["operation"][0], "rem": e["operation"][1:].copy()}]
    while len(stack) > 0:
        task = stack[0]
        stack.pop(0)

        if task["alr"]*task["rem"][0] <= e["value"]:
            newTask = copy.deepcopy(task)
            newTask["alr"] = task["alr"]*task["rem"][0]
            newTask["rem"].pop(0)

            if len(newTask["rem"]) == 0:
                if newTask["alr"] == e["value"]:
                    successTests += e["value"]
                    break
            else:
                stack.insert(0, newTask)
        
        if task["alr"]+task["rem"][0] <= e["value"]:
            newTask = copy.deepcopy(task)
            newTask["alr"] = task["alr"]+task["rem"][0]
            newTask["rem"].pop(0)

            if len(newTask["rem"]) == 0:
                if newTask["alr"] == e["value"]:
                    successTests += e["value"]
                    break
            else:
                stack.insert(0, newTask)

        newVal = int(str(task["alr"])+str(task["rem"][0]))
        if newVal <= e["value"]:
            newTask = copy.deepcopy(task)
            newTask["alr"] = newVal
            newTask["rem"].pop(0)

            if len(newTask["rem"]) == 0:
                if newTask["alr"] == e["value"]:
                    successTests += e["value"]
                    break
            else:
                stack.insert(0, newTask)

print(successTests)
