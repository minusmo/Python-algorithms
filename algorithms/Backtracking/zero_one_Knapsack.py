from enum import Enum
"""
Take backtracking approach.
Design a Promising/bounding function and
Do DFS in State-Space Tree.
"""

class ItemIs(Enum):
    NOTTAKEN = 0
    TAKEN = 1

class KnapSack:
    def __init__(self) -> None:
        self.items = self.getItems()
        self.weights = self.getWeights()
        self.constraint = self.getConstraint()
        self.bestProfit = 0
        self.maxProfit = 0
        self.getMaxProfit()
    
    def getItems(self):
        items = [40, 30, 50, 10]
        return items

    def getWeights(self):
        weights = [2, 5, 10, 5]
        return weights
    
    def getConstraint(self):
        return 16
    
    def getMaxProfit(self):
        self.bestProfit = 0
        sackState = {
            "sumOfProfit": 0,
            "sumOfWeight": 0,
        }
        
        self.DFS(sackState, 0)
    
    def DFS(self, sackState, itemInProcess):
        for itemState in ItemIs:
            potentialProfit = self.calculatePotentialProfit(sackState, itemInProcess, itemState)
            if self.isPromising(potentialProfit):
                sackState = self.updateSackState(sackState, itemInProcess, itemState)
                self.updateBestProfit(sackState["sumOfProfit"])
                self.DFS(sackState, itemInProcess + 1)
    
    def calculatePotentialProfit(self, sackState, itemInProcess, itemState):
        leftWeight = self.constraint - sackState["sumOfWeight"]
        if self.constraint < self.items[itemInProcess]:
            return -1
        
        sumOfProfit = sackState["sumOfProfit"]
        potentialItems = itemInProcess if itemState == ItemIs.TAKEN else itemInProcess + 1
        itemNotTaken = None
        for potentialItem in range(potentialItems, len(self.items)):
            if self.weights[potentialItem] <= leftWeight:
                leftWeight -= self.weights[potentialItem]
                sumOfProfit += self.items[potentialItem]
            else:
                itemNotTaken = potentialItem
                break
            
        sumOfProfit += leftWeight * (self.items[itemNotTaken] / self.weights[itemNotTaken])
        return sumOfProfit
        
    def isPromising(self, potentialProfit):
        if potentialProfit < self.bestProfit:
            return False
        else:
            return True
    
    def updateSackState(self, sackState, itemInProcess, itemState):
        newState = {
            "sumOfProfit": 0,
            "sumOfWeight": 0,
        }
        newState["sumOfProfit"] = sackState["sumOfProfit"] + self.items[newState["itemsIn"]]
        newState["sumOfWeight"] = sackState["sumOfWeight"] + self.weights[newState["itemsIn"]]
        return newState
        
    def updateBestProfit(self, sumOfProfit):
        self.bestProfit = sumOfProfit