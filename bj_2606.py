class WormVirus:
    def __init__(self, computers, pairs):
        self.computers = computers
        self.pairs = pairs
        self.computerGraph = [[] for _ in range(self.computers + 1)]
        self.linkComputers()
        self.infectedComputers = [0] * (self.computers + 1) #큐
        self.needVisit = [] #큐
        
    def linkComputers(self):
        for _ in range(self.pairs):
            source, target = map(int, input().split())
            self.computerGraph[source].append(target)
            self.computerGraph[target].append(source)
            
    def checkInfected(self):
        if self.computers == 0 or self.pairs == 0:
            return 0
        
        self.needVisit.append(1)
        while len(self.needVisit) > 0:
            visitedComputer = self.needVisit.pop()
            if not self.infectedComputers[visitedComputer] == 1:
                self.infectedComputers[visitedComputer] = 1
                self.needVisit.extend(self.computerGraph[visitedComputer])
        return sum(self.infectedComputers) - 1
        

computers = int(input())
linkedPairs = int(input())
wormVirus = WormVirus(computers, linkedPairs)
infectedComputersWithoutFirst = wormVirus.checkInfected()
print(infectedComputersWithoutFirst)