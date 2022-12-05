import re
from collections import deque
# parse file
fname = "adventofcode22/python/d5/input.txt"
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
    mover1 = []
    mover2 = []
    mover3 = []
    mover4 = []
    mover5 = []
    mover6 = []
    mover7 = []
    mover8 = []
    
    # a = lines[1][1::4].strip()
    # print(a)
    moverList = []
    for i in range(0,8):
        a = lines[i][1::4].strip()
        for j in range(len(a)):
            if(j == 0 and a[j] != ' '):
                mover1.append(a[j])
            if(j == 1 and a[j] != ' '):
                mover2.append(a[j])
            if(j == 2 and a[j] != ' '):
                mover3.append(a[j])
            if(j == 3 and a[j] != ' '):
                mover4.append(a[j])
            if(j == 4 and a[j] != ' '):
                mover5.append(a[j])
            if(j == 5 and a[j] != ' '):
                mover6.append(a[j])
            if(j == 6 and a[j] != ' '):
                mover7.append(a[j])
            if(j == 7 and a[j] != ' '):
                mover8.append(a[j])
    moverList.append(mover1)
    moverList.append(mover2)
    moverList.append(mover3)
    moverList.append(mover4)
    moverList.append(mover5)
    moverList.append(mover6)
    moverList.append(mover7)
    moverList.append(mover8)

# for i in movingList:
    
print(moverList[1])
