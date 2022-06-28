import functools
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
    def getlastItem(self):
        return self.lastItem
    def setlastItem(self, lastItem):
        self.lastItem = lastItem

@functools.total_ordering
class ComparableState(State):
    def __gt__(self, other):
        return self.g > other.g
    def __eq__(self, other):
        return self.g == other.g
    
def calculateHVal(nextItem , W):
    hVal = 0
    availableW = K - W
    for i in range(nextItem, N):
        if items[i][0] > availableW:
            fractionalValue = items[i][1] / items[i][0]
            hVal += availableW * fractionalValue
            break
        else:
            hVal += items[i][1]
            availableW -= items[i][0]
    return hVal

def calculateBestProfit(items):
    bestProfit = 0
    pq = PriorityQueue()
    hValWithItem = calculateHVal(0, 0)
    hValWithoutItem = calculateHVal(1, 0)
    withItem = ComparableState(items[0][1], hValWithItem, items[0][0], 0)
    withoutItem = ComparableState(0, hValWithoutItem, 0, 0)
    pq.put([maxsize - withItem.hVal(), withItem])
    pq.put([maxsize - withoutItem.hVal(), withoutItem])
    while not pq.qsize() == 0:
        priority, bestProfitState = pq.get()
        nextItem = bestProfitState.getlastItem() + 1
        if nextItem > N-1:
            continue
        if items[nextItem][0] > K - bestProfitState.wVal():
            if bestProfitState.gVal() > bestProfit:
                bestProfit = bestProfitState.gVal()
        else:
            hValWithItem = calculateHVal(nextItem+1, bestProfitState.wVal()+items[nextItem][0])
            hValWithoutItem = calculateHVal(nextItem+1, bestProfitState.wVal())
            if bestProfitState.gVal() + items[nextItem][1] + hValWithItem > bestProfit:
                withItem = ComparableState(bestProfitState.gVal() + items[nextItem][1], hValWithItem, bestProfitState.wVal() + items[nextItem][0], nextItem)
                pq.put([maxsize - withItem.hVal(), withItem])
            if bestProfitState.gVal() + hValWithoutItem > bestProfit:
                bestProfitState.setlastItem(nextItem)
                bestProfitState.sethVal(hValWithoutItem)
                pq.put([maxsize - bestProfitState.hVal(), bestProfitState])
    return bestProfit
bestProfit = calculateBestProfit(items)
print(bestProfit)