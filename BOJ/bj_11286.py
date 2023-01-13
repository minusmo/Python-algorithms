import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
  num = int(input())
  if num == 0:
    if len(heap) == 0:
      print(0)
    else:
      print(heappop(heap)[1])
  else:
    heappush(heap, (abs(num), num))