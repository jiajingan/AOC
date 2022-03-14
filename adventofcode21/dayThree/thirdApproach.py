from collections import defaultdict

fname = "/Users/jackiegan/PycharmProjects/adventofcode21/dayThree/input.txt"

with open(fname, 'r') as f:
    lines = []
    for line in f:
        lines.append(line.split())

#
# for i in range(0,10):
#     print("num"+str(i))

d = defaultdict(int)
print(d)
d[1] = 1
print(dict(d))


