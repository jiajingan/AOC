fname = "/Users/jackiegan/PycharmProjects/adventofcode21/dayTwo/input.txt"

horizontalCount = 0
depthCount = 0
aimCount = 0

with open(fname) as f:
    lines = []
    for line in f:
        lines.append(line.split())

# challenge 2
for i in range(0, len(lines)):
    if lines[i][0] == "forward":
        horizontalCount += int(lines[i][1])
        depthCount += aimCount * int(lines[i][1])

    elif lines[i][0] == "down":
        aimCount += int(lines[i][1])

    elif lines[i][0] == "up":
        aimCount -= int(lines[i][1])

print(horizontalCount*depthCount)