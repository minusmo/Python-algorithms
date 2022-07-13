from collections import defaultdict
TCs = int(input())
tcs = []
for tc in range(TCs):
    NMW = [int(i) for i in input().split()]
    tcs.append(NMW)
    adjacencyList = defaultdict(defaultdict)
    # get roads
    for i in range(M):
        S,E,T = map(int, input().split())
        adjacencyList[S][E]
    # get wormholes
    for i in range(W):
        S,E,T = map(int, input().split())
        adjacencyList[S].append((E, -T))
        
    
def allCycleDetection(u: int, parentNode: int, parents: defaultdict, visits: defaultdict, cycles: defaultdict, cycleNumber: int) -> None:
    if visits[u] == 2:
        return
    elif visits[u] == 1:
        cycleNumber += 1
        currentNode = parentNode
        travelTime = 0
        while currentNode != u:
            travelTime += adjacencyList[currentNode]