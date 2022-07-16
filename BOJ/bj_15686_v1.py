from sys import maxsize

def getItemCosts(house: tuple, item: tuple) -> int:
    return abs(house[0] - item[0]) + abs(house[1] - item[1])

def calculateCostsFromItems(costsForItems: list, houses: list, items: list) -> None:
    for item in items:
        cost = [getItemCosts(house, item) for house in houses]
        costsForItems.append(cost)

def updateSavedItems(savedItems: list, newItem: int, constraint: int, minCostsFromHouse: list, houses: list, costsForItems: list) -> int:
    totalDiff = 0
    currentCosts = [0] * len(houses)
    if sum(savedItems) < constraint:
        for i in range(len(houses)):
            ithMinCost = minCostsFromHouse[i]
            newCost = costsForItems[newItem][i]
            if newCost < ithMinCost:
                minCostsFromHouse[i] = newCost
                savedItems[newItem] = 1
    elif sum(savedItems) == constraint:
        for i in range(len(houses)):
            ithMinCost = minCostsFromHouse[i]
            newCost = costsForItems[newItem][i]
            currentCosts[i] = min(ithMinCost, newCost)
            totalDiff += ithMinCost - newCost
        if totalDiff < 0:
            minCostsFromHouse = currentCosts
    return sum(minCostsFromHouse)

def getMinCost(minCostsFromHouse, costsForItems, items, M, houses) -> int:
    CCD = maxsize
    savedItems = [0] * len(items)
    for i in range(len(items)):
        newCCD = updateSavedItems(savedItems, i, M, minCostsFromHouse, houses, costsForItems)
        CCD = newCCD
    return CCD

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

    minCostsFromHouse = [maxsize] * len(houses)
    calculateCostsFromItems(costsForItems, houses, items)
    CCD = getMinCost(minCostsFromHouse, costsForItems, items, N, houses)
    print(CCD)
    
main()