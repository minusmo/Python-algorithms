from sys import maxsize
from operator import itemgetter
from queue import PriorityQueue


N, K = [int(i) for i in input().split()]
items = []
for _ in range(N):
    W, V = [int(i) for i in input().split()]
    items.append((W,V))
items = sorted(items, key=itemgetter(0))
class State:
    def __init__(self, g, h, W, lastItem):
        self.g = g
        self.h = h
        self.W = W
        self.lastItem = lastItem
    def gVal(self):
        return self.g
    def setgVal(self, g):
        self.g = g
    def hVal(self):
        return self.h
    def sethVal(self, h):
        self.h = h
    def wVal(self):
        return self.W
    def setwVal(self, W):
        self.W = W
    def lastItem(self):
        return self.lastItem
    def setlastItem(self, lastItem):
        self.lastItem = lastItem

def calculateHVal(nextItem , W):
    hVal = 0
    for i in range(nextItem, N):
        if items[i][0] > K - W:
            availableWeight = K - W
            fractionalWeight = items[i][1] / items[i][0]
            hVal = availableWeight * fractionalWeight
            break
        else:
            hVal += items[i][1]
    return hVal

bestProfit = 0
def calculateBestProfit(items):
    pq = PriorityQueue()
    hValWithItem = calculateHVal(0, K)
    hValWithoutItem = calculateHVal(1, K)
    withItem = State(items[0][1], hValWithItem, items[0][0], 0)
    withoutItem = State(0, hValWithoutItem, 0, 0)
    pq.put((maxsize - withItem.hVal(), withItem))
    pq.put((maxsize - withoutItem.hVal(), withoutItem))
    while not pq.empty():
        priority, bestProfitState = pq.get()
        nextItem = bestProfitState.lastItem() + 1
        if items[nextItem][0] > K - bestProfitState.wVal():
            if bestProfitState.gVal() > bestProfit:
                bestProfit = bestProfitState.gVal()
        else:
            hValWithItem = calculateHVal(nextItem, K)
            hValWithoutItem = calculateHVal(nextItem+1, K)
            if hValWithItem > bestProfit:
                withItem = State(bestProfitState.gVal() + items[nextItem][1], hValWithItem, bestProfitState.wVal() + items[nextItem][0], nextItem)
                pq.put((maxsize - withItem.hVal(), withItem))
            if hValWithoutItem > bestProfit:
                withoutItem = bestProfitState.setLastItem(nextItem)
                withoutItem.sethVal(hValWithoutItem)
                pq.put((maxsize - withoutItem.hVal(), withoutItem))

calculateBestProfit(items)
print(bestProfit)