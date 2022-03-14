from collections import defaultdict

fname = "/Users/jackiegan/PycharmProjects/adventofcode21/dayThree/input.txt"

binaryEpsilon = 0
binaryGamma = 0
Epsilon = 0
Gamma = 0

count = 0
d = {}

with open(fname, 'r') as f:
    lines = []
    for line in f:
        lines.append(line.split())

# for i in range(0, len(lines)):
#     for j in range(0, len(lines[i])):
#         if lines[i][j] ==

for j in range(0, len(lines[0])):
    count = 1
    # counterBit1 = 0
    d[count] = 0
    for i in range(0, len(lines)):
        if int(lines[i][j]) == 1:
            # counterBit1 += 1
            # d.setdefault(count, 0)
            # d.update(count, counterBit1)
            d[count] += 1
        # counterBit1 = 0
    count += 1

print(d)

