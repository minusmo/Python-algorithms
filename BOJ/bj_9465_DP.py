T = int(input())
testCases = []
for i in range(T):
    n = int(input())
    itemTable = []
    items0 = [0]+[int(k) for k in input().split()]
    items1 = [0]+[int(k) for k in input().split()]
    itemsNone = [0 for _ in range(n+1)]
    itemTable.append(items0)
    itemTable.append(items1)
    itemTable.append(itemsNone)
    testCase = (n, itemTable)
    testCases.append(testCase)

def calculateMaxVal(n, itemTable):
    maxVal = 0
    for i in range(1, n+1):
        selection0 = itemTable[0][i]+max(itemTable[1][i-1], itemTable[2][i-1])
        selection1 = itemTable[1][i]+max(itemTable[0][i-1], itemTable[2][i-1])
        selectionNone = max(itemTable[0][i-1], itemTable[1][i-1])
        itemTable[0][i] = selection0
        itemTable[1][i] = selection1
        itemTable[2][i] = selectionNone
    maxVal = max(itemTable[0][n], itemTable[1][n], itemTable[2][n])
    return maxVal
            
for testCase in testCases:
    n, itemTable = testCase
    maxVal = calculateMaxVal(n, itemTable)
    print(maxVal)