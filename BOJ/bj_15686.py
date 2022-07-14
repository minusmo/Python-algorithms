N, M = map(int, input().split())
houses = []
chickens = []
for r in range(N):
    row = input().split()
    for c in range(N):
        if row[int(c)] == 1:
            houses.append((r,c))
        elif row[int(c)] == 2:
            chickens.append((r,c))
            
chickenDistances = [0] * len(houses)

def getMinChickhenDistance():
    chicken = getChicken()
    