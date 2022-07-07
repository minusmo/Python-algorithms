from queue import PriorityQueue
from sys import maxsize

A, B = map(int, input().split())

def minOperations(A, B) -> int:
    if A == B:
        return 0
    ops = maxsize
    pq = PriorityQueue()
    pq.put([0, A])
    found = False
    while not pq.qsize() == 0:
        minOps, num = pq.get()
        if minOps > ops:
            continue
        if num == B:
            found = True
            ops = minOps if minOps < ops else ops
            continue
        doubled = num * 2
        padded = num * 10 + 1
        if doubled <= B:
            pq.put([minOps+1, doubled])
        if padded <= B:
            pq.put([minOps+1, padded])
    
    return ops + 1 if found else -1
    
print(minOperations(A,B))