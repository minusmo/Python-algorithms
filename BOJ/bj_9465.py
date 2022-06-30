from queue import PriorityQueue
from sys import maxsize

T = int(input())
testCases = []
for i in range(T):
    n = int(input())
    itemTable = []
    items0 = [int(k) for k in input().split()]
    items1 = [int(k) for k in input().split()]
    itemTable.append(items0)
    itemTable.append(items1)
    testCase = (n, itemTable)
    testCases.append(testCase)

def calculateMaxVal(n, itemTable):
    maxVal = 0
    leftItems = 2 * n
    items = [[False for _ in range(n)] for _ in range(2)]
    pq = PriorityQueue()
    for i in range(2):
        for j in range(n):
            pq.put((maxsize - itemTable[i][j], i, j))
            
    while leftItems > 0:
        priority, i, j = pq.get()
        if items[i][j] == False:
            disabledItems = disableItems(i,j,items,n)
            maxVal += itemTable[i][j]
            leftItems -= disabledItems
            
    return maxVal

def disableItems(i,j,items,n):
    disabledItems = 0
    items[i][j] = True
    disabledItems += 1
    if i == 0:
        if items[i+1][j] == False:
            items[i+1][j] = True
            disabledItems += 1
        if j == 0:
            if items[i][j+1] == False:
                items[i][j+1] = True
                disabledItems += 1
        elif j == n-1:
            if items[i][j-1] == False:
                items[i][j-1] = True
                disabledItems += 1
        else:
            if items[i][j-1] == False:
                items[i][j-1] = True
                disabledItems += 1
            if items[i][j+1] == False:
                items[i][j+1] = True
                disabledItems += 1
    else:
        if items[i-1][j] == False:
            items[i-1][j] = True
            disabledItems += 1
        if j == 0:
            if items[i][j+1] == False:
                items[i][j+1] = True
                disabledItems += 1
        elif j == n-1:
            if items[i][j-1] == False:
                items[i][j-1] = True
                disabledItems += 1
        else:
            if items[i][j-1] == False:
                items[i][j-1] = True
                disabledItems += 1
            if items[i][j+1] == False:
                items[i][j+1] = True
                disabledItems += 1
    return disabledItems
            
for testCase in testCases:
    n, itemTable = testCase
    maxVal = calculateMaxVal(n, itemTable)
    print(maxVal)