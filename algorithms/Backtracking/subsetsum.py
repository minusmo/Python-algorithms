from winreg import REG_NO_LAZY_FLUSH


class SubSetSum:
    def __init__(self) -> None:
        self.total_nodes = 0
        self.targetSum = 0
        self.superSet = []
        self.state = {
            "superSetSize": 0,
            "subSetSize": 0,
            "sumSoFar": 0,
            "nodesCount": 0,
            "subSet": [],
            "subSetSize": 0,
        }
        
    def subsetSum(self, superSet, state, targetSum):
        self.total_nodes += 1
        if self.targetSum == state["sumSofFar"]:
            self.printSubsetSum(state["subSet"], state["subSetSize"])
            if (state["nodesCount"] + 1 < state["subSetSize"] and 
               state["sumSoFar"] - self.superSet[state["nodesCount"]] + self.superSet[state["nodesCount"] + 1] <= self.targetSum):
                newState = self.updateState(state)
                self.subSetSum(superSet, newState, targetSum)
            return
        else:
            if state["nodesCount"] < state["subSetSize"] and state["sumSoFar"] + self.superSet[state["nodesCount"]] <= self.targetSum:
                for i in range(state["nodesCount"], state["subSetSize"]):
                    state["subSet"]
    def updateState(self, state):
        newState = state.copy()
        newState["subSetSize"] -= 1
        newState["sumSoFar"] -= self.superSet[state["nodesCount"]]
        newState["nodesCount"] += 1
        return newState