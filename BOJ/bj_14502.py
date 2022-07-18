from itertools import combinations
from queue import Queue
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
Map = []
paths = []
viruses = []
maxSafeArea = 0
W = 3
w = 0
v = 0
for r in range(N):
    row = []
    for c, p in enumerate(input().split()):
        if p == '0':
            paths.append((r,c))
        elif p == '2':
            viruses.append((r,c))
            v += 1
        elif p == '1':
            w += 1
        row.append(int(p))
    Map.append(row)
pathLen = len(paths)
walls = []

def calculateSafeArea(infections):
    safeArea =  N * M - w - v - infections - W
    return safeArea

def simulateInfectedArea(Map):
    infectedMap = [row[:] for row in Map]
    totalInfections = 0
    for wall in walls:
        path = paths[wall]
        infectedMap[path[0]][path[1]] = 1
    for virus in viruses:
        infections = bfs(infectedMap, virus)
        totalInfections += infections
    return totalInfections

def bfs(infectedMap, virus):
    moves = [(1,0),(0,1),(-1,0),(0,-1)]
    infections = 0
    q = Queue()
    q.put(virus)
    while not q.qsize() == 0:
        path = q.get()
        for move in moves:
            r, c = movePath(path, move)
            if isInBound(r,c) and infectedMap[r][c] == 0:
                infectedMap[r][c] = 2
                infections += 1
                q.put((r,c))
    return infections
                
def movePath(path, move):
    return (path[0] + move[0], path[1] + move[1])

def isInBound(r,c):
    if r < 0 or r >= N or c < 0 or c >= M:
        return False
    else:
        return True
    
# def getMaxSafeArea(Map, p):
#     if len(walls) == W:
#         infections = simulateInfectedArea(Map)
#         safeArea = calculateSafeArea(infections)
#         if safeArea > maxSafeArea[0]:
#             maxSafeArea[0] = safeArea
#         return

#     for path in range(p, pathLen):
#         if path not in walls:
#             walls.append(path)
#             getMaxSafeArea(Map, path+1)
#             walls.pop()
        
for combination in combinations(paths, 3):
    for position in combination:
        Map[position[0]][position[1]] = 1
    infections = simulateInfectedArea(Map)
    safeArea = calculateSafeArea(infections)
    if safeArea > maxSafeArea:
        maxSafeArea = safeArea
    for position in combination:
        Map[position[0]][position[1]] = 0
            
print(maxSafeArea)