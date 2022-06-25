N, M = map(int, input().split())
table = []
for _ in range(N):
    row = [int(i) for i in input().split()]
    table.append(row)
positions = []
for _ in range(M):
    position = [int(i) for i in input().split()]
    positions.append(position)
    
sumVals = [[0 for _ in range(N)] for _ in range(N)]
# def calculateSum(position):
#     x1, y1, x2, y2 = [coor-1 for coor in position]
#     if (x1-x2) == 0 and (y1-y2) == 0:
#         sumVals[x1][y1] = table[x1][y1]
#         return sumVals[x1][y1]
#     if sumVals[x2][y2] != 0:
#         return sumVals[x2][y2]
#     if (x1-x2) == 0:# 세로 합
#         sumVals[x2][y2] = calculateSum([x1,y1,x2,y2-1]) + table[x2][y2]
#     elif (y1-y2) == 0: #가로 합
#         sumVals[x2][y2] = calculateSum([x1,y1,x2-1,y2]) + table[x2][y2]
#     else:
#         sumVals[x2][y2] = calculateSum([x1,y1,x2-1,y2]) + calculateSum([x1, y1, x2, y2-1]) + table[x2][y2]
#     return sumVals[x2][y2]

def calculateSum(position):
    x1, y1, x2, y2 = [coor-1 for coor in position]
    sumVal = 0
    if x1 == x2 and y1 == y2:
        return table[x1][y1]
    if (x2-x1) <= 1 or (y2-y1) <= 1:
        for x in range(x1, x2):
            for y in range(y1, y2):
                sumVal += table[x][y]
        return sumVal
    elif (y2-y1) > (x2-x1):
        yHalf = (y2-y1) // 2
        sumVal = calculateSum([x1,y1,x2,yHalf]) + calculateSum([x1,yHalf+1,x2,y2])
    else:
        xHalf = (x2-x1) // 2
        sumVal = calculateSum([x1,y1,xHalf,y2]) + calculateSum([xHalf+1,y1, x2,y2])
    return sumVal
        
for position in positions:
    sumVal = calculateSum(position)
    print(sumVal)