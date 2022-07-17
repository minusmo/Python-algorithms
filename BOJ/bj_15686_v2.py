from sys import maxsize

def getItemCosts(house: tuple, item: tuple) -> int:
    return abs(house[0] - item[0]) + abs(house[1] - item[1])

def calculateCostsFromItems(costsForItems: list, houses: list, items: list) -> None:
    for item in items:
        cost = [getItemCosts(house, item) for house in houses]
        costsForItems.append(cost)

def calculateMinCost(savedItems, costsForItems, houses) -> int:
    CDC = 0
    for house in range(len(houses)):
        minCostFromHouse = maxsize
        for item in range(len(savedItems)):
            if costsForItems[item][house] < minCostFromHouse and savedItems[item] == 1:
                minCostFromHouse = costsForItems[item][house]
        CDC += minCostFromHouse
    return CDC 

def getMinCost(minCostsFromHouse, costsForItems, items, M, houses, savedItems, item):
    if sum(savedItems) == M:
        minCost = calculateMinCost(savedItems, costsForItems, houses)
        if minCost < minCostsFromHouse[0]:
            minCostsFromHouse[0] = minCost
        return
    else:
        for i in range(item, len(items)):
            if savedItems[i] != 1:
                savedItems[i] = 1
                getMinCost(minCostsFromHouse, costsForItems, items, M, houses, savedItems, i+1)
                savedItems[i] = 0
    return

def main():
    N, M = map(int, input().split())
    houses = []
    items = []
    for r in range(N):
        row = input().split()
        for c in range(N):
            if int(row[c]) == 1:
                houses.append((r,c))
            elif int(row[c]) == 2:
                items.append((r,c))

    costsForItems = []
    savedItems = [0] * len(items)
    minCostsFromHouse = [maxsize]
    calculateCostsFromItems(costsForItems, houses, items)
    getMinCost(minCostsFromHouse, costsForItems, items, M, houses, savedItems, 0)
    print(minCostsFromHouse[0])
    
main()