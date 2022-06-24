N = int(input())
parentPointers = [None] * (N+1)
adjList = [[] for _ in range(N+1)]
            
for _ in range(N-1):
    s, t = map(int, input().split())
    adjList[s].append(t)
    adjList[t].append(s)
    
def setParentPointers(adjList, parentPointers):
    queue = [1]
    while len(queue) > 0:
        node = queue.pop(0)
        for adjNode in adjList[node]:
            if parentPointers[adjNode] == None:
                parentPointers[adjNode] = node
                queue.append(adjNode)
            
        
setParentPointers(adjList, parentPointers)
for i in range(2, N+1):
    print(parentPointers[i])