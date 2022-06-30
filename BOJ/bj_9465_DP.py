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
    vals = [[0,0] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(2):
            
            vals[j][i] = max()
    maxVal = max()
            
    return maxVal
            
for testCase in testCases:
    n, itemTable = testCase
    maxVal = calculateMaxVal(n, itemTable)
    print(maxVal)