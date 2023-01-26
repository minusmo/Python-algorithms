import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
results = []
for _ in range(N):
    command = int(input())
    if command == 0:
        if len(heap) == 0:
            results.append(0)
        else:
            results.append(-1 * heapq.heappop(heap))
    elif command > 0:
        heapq.heappush(heap,-command)

for result in results:
    print(result)