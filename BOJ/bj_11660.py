N, M = map(int, input().split())
table = []
aux = []
for i in range(N):
    row = input().split()
    if i == 0:
        aux.append([int(num) for num in row])
    else:
        auxRow = [int(row[j])+aux[i-1][j] for j in range(N)]
        aux.append(auxRow)
    table.append(row)

positions = []
for _ in range(M):
    position = [int(i)-1 for i in input().split()]
    positions.append(position)
    
for i in range(N):
    for j in range(1, N):
        aux[i][j] += aux[i][j-1]

def calculateSubSum(position):
    x1,y1,x2,y2 = position
    subSum = aux[x2][y2]
    if x1 == x2 and y1 == y2:
        return int(table[x2][y2])
    if x1 > 0:
        subSum -= aux[x1-1][y2]
    if y1 > 0:
        subSum -= aux[x2][y1-1]
    if x1 > 0 and y1 > 0:
        subSum += aux[x1-1][y1-1]
    return subSum

for position in positions:
    subSum = calculateSubSum(position)
    print(subSum)