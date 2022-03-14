from collections import Counter

fname = "/Users/jackiegan/PycharmProjects/adventofcode21/dayThree/input.txt"

with open(fname, 'r') as f:
    lines = []
    for line in f:
        lines.append(line.split())


# https://www.geeksforgeeks.org/python-find-most-common-element-in-each-column-in-a-2d-list/

def mostCommon(lst):
    return [Counter(col).most_common()[0][0] for col in zip(*lst)]


def leastCommon(lst):
    return [Counter(col).most_common()[-1][0] for col in zip(*lst)]


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal
    # print(decimal)


a = int(mostCommon(lines)[0])
b = int(leastCommon(lines)[0])
c = binaryToDecimal(a) * binaryToDecimal(b)
print(c)
