import re

# advent of code day2
fname = "/Users/jackiegan/PycharmProjects/adventofcode21/dayTwo/input.txt"

forwardCount = 0
upCount = 0
downCount = 0
aimCount = 0

with open(fname) as f:
    lines = []
    for line in f:
        lines.append(line.split())

# challenge 1
for i in range(0, len(lines)):
    if lines[i][0] == "forward":
        forwardCount += int(lines[i][1])

    if lines[i][0] == "down":
        downCount += int(lines[i][1])

    if lines[i][0] == "up":
        upCount += int(lines[i][1])

print(forwardCount)
print(downCount)
print(upCount)
print("challenge 1:%d", (downCount - upCount) * forwardCount)


