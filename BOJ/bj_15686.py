from sys import maxsize
N, M = map(int, input().split())
houses = []
items = []
for r in range(N):
    row = input().split()
    for c in range(N):
        if row[int(c)] == 1:
            houses.append((r,c))
        elif row[int(c)] == 2:
            items.append((r,c))
            
minCostsFromHouse = []
costsForItems = []

def getItemCosts(house: list, item: list) -> int:
    return abs(house[0] - item[0]) + abs(house[1] - item[1])

def calculateCostsFromItems(costsForItems: list) -> None:
    for item in items:
        cost = [getItemCosts(house, item) for house in houses]
        costsForItems.append(cost)

# def calculateMinCostsFromHouses(minCostsFromHouses: list) -> None:
#     for house in houses:
#         costs = [getItemCosts(house, item) for item in items]
#         minCostsFromHouses.append(min(costs))

def calculateCCD(savedItems: list, item: int) -> int:
    CCD = 0
    for i in range(len(houses)):
        ithMinCost = maxsize
        for savedItem in savedItems:
            ithMinCost = min(costsForItems[savedItem][i], ithMinCost)
        ithMinCost = min(costsForItems[item][i], ithMinCost)
        CCD += ithMinCost
    return CCD

def updateSavedItems(savedItems: list, i: int):
    
def getMinCost() -> int:
    CCD = maxsize
    constraint = M
    savedItems = []
    for i in range(len(items)):
        newCCD = calculateCCD(savedItems, i)
        if newCCD < CCD:
            if len(savedItems) < constraint:
                savedItems.append(items[i])
            else:
                updateSavedItems(savedItems, i)
            CCD = newCCD
    return CCD