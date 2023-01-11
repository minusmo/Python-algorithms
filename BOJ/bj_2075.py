import sys
from heapq import heappush, heapify
input = sys.stdin.readline

N = int(input())
heap = []
result = []
for _ in range(N):
    for item in map(int, input().split()):
        heappush(heap, -1 * item)
    result = heap[:N]
    heap.clear()
    heap.extend(result)
    
print(-1 * result[N-1])
