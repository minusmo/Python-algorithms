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
            "itemsIn": 0,
        }
        
        self.DFS(sackState, 0)
    
    def DFS(self, sackState, item_to_process):
        for itemState in ItemIs:
            potentialProfit = self.calculatePotentialProfit(sackState, item_to_process, itemState)
            if self.isPromising(potentialProfit):
                sackState = self.updateSackState(sackState, item_to_process, itemState)
                self.updateBestProfit(sackState["sumOfProfit"])
                self.DFS(sackState)
    
    def calculatePotentialProfit(self, sackState, item_to_process, itemState):
        leftWeight = self.constraint - sackState["sumOfWeight"]
        sumOfProfit = sackState["sumOfProfit"]
        itemsIn = sackState["itemsIn"]
        for i in range(itemsIn, len(self.items)):
            if self.weights[i] <= leftWeight:
                leftWeight -= self.weights[i]
                sumOfProfit += self.items[i]
            else:
                itemsIn = i
                break
            
        sumOfProfit += leftWeight * (self.items[itemsIn] / self.weights[itemsIn])
        return sumOfProfit
        
    def isPromising(self, potentialProfit):
        if potentialProfit < self.bestProfit:
            return False
        else:
            return True
    
    def updateSackState(self, sackState, item_to_process, itemState):
        newState = {
            "sumOfProfit": 0,
            "sumOfWeight": 0,
            "itemsIn": 0,
        }
        newState["itemsIn"] = sackState["itemsIn"] + 1
        newState["sumOfProfit"] = sackState["sumOfProfit"] + self.items[newState["itemsIn"]]
        newState["sumOfWeight"] = sackState["sumOfWeight"] + self.weights[newState["itemsIn"]]
        return newState
        
    def updateBestProfit(self, sumOfProfit):
        self.bestProfit = sumOfProfit