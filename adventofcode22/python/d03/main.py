# AOC day 3 in python

fname = "adventofcode22/python/d3/input.txt"
with open(fname) as f:
    lines = []
    for line in f:
        a=line.strip("\n")
        s1 = a[:len(a)//2]
        s2 = a[len(a)//2:]
        lines.append([s1,s2])
total = 0
for i in lines:
    # https://bobbyhadz.com/blog/python-find-common-characters-between-two-strings#:~:text=To%20find%20common%20characters%20between,the%20set%20into%20a%20string.
    common_character = ''.join(set(i[0]).intersection(i[1]))   
    if(ord(common_character)>64 and ord(common_character)<91):
        # isupper
        total += ord(common_character)-38
    if(ord(common_character)>96 and ord(common_character)<123):
        # islower
        total += ord(common_character)-96
# print(lines)
print(total)