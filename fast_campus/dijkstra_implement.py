import sys
from queue import PriorityQueue

def Edge(distance, vertex):
    return (distance, vertex)

class Dijkstra:
    def __init__(self, start) -> None:
        self.graph = {
            'a': [Edge(8,'b'), Edge(1,'c'), Edge(2,'d')],
            'b': [],
            'c': [Edge(5,'b'), Edge(2,'d')],
            'd': [Edge(3,'e'), Edge(5,'f')],
            'e': [Edge(1,'f')],
            'f': [Edge(5,'a')]
        }
        
        self.startEdge = Edge(0, start)
        
        self.initializeDistances()
        
        self.prioriryQueue = PriorityQueue()
        self.prioriryQueue.put(self.startEdge)
    
    def initializeDistances(self):
        self.distances = {}
        for key in self.graph.keys():
            self.distances[key] = sys.maxsize
        self.distances[self.startEdge[1]] = 0
        
    def dijkstraPath(self):
        while not self.prioriryQueue.empty():
            currentDistance, edgeNode = self.prioriryQueue.get()
            currentNode = edgeNode
            
            if currentDistance > self.distances[currentNode]:
                continue
            
            nodeList = self.graph[currentNode]
            for adjacentNode in nodeList:
                adjacent = adjacentNode[1]
                weight = adjacentNode[0]
                distance = currentDistance + weight
                
                if distance < self.distances[adjacent]:
                    self.distances[adjacent] = distance
                    self.prioriryQueue.put(Edge(distance, adjacent))
        
        return self.distances
    

dijkstra = Dijkstra('a')
print(dijkstra.dijkstraPath())