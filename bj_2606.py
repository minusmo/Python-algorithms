class WormVirus:
    def __init__(self, computers, pairs) -> None:
        self.computers = self.computers
        self.pairs = pairs
        self.computerGraph = [[] for _ in range(self.computers + 1)]
        self.linkComputers()
        self.infectedComputers = [0] * (self.computers + 1)
        self.needVisit = [1]
        
    def linkComputers(self):
        for _ in range(self.pairs):
            source, target = map(int, input().split())
            self.computerGraph[source].append(target)
            
    def checkInfected(self):
        while len(self.needVisit) > 0:
            