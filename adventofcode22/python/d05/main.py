import re
from collections import deque
# parse file
fname = "adventofcode22/python/d05/input.txt"
with open(fname,'r', encoding='utf-8') as f:
    lines = f.readlines()
    # process moving data
    # https://bobbyhadz.com/blog/python-typeerror-io-textiowrapper-object-is-not-subscriptable
    movingList = []
    for i in range(10,len(lines)):
        # print(i)
        findNum = re.findall(r'\d+', lines[i])
        movingList.append(findNum)
    
    #try substring approach
    a = lines[7][1::4]
    print(a)
    moverBigList = []
    # https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-168.php
    for i in range(0,8):
        # a = lines[i][1::4]
        moverList = []
        for j in range(len(a)):
            a = lines[i][1::4]
            # print(lines[i][1::4][j])
                # moverList = []
            moverList.append(a[j])
            # moverDict[i] = moverList
                #changed index fixed
        # print(type(moverList))
        moverBigList.append(moverList)

# for i in movingList:
    
# print(moverList[1])
print(moverBigList)
