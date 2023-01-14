import sys
from heapq import heappop, heappush
input = sys.stdin.readline

class DBEQ:
  def __init__(self) -> None:
    self.is_removed = False
  
  def remove(self, heap: list, idx, x):
    if self.is_removed or idx >= len(heap):
      return
    if heap[idx] == x:
      left = heap[0:idx]
      right = heap[idx+1:]
      heap.clear()
      heap.extend(left)
      heap.extend(right)
      self.is_removed = True
    else:
      self.remove(heap,idx*2+1,x)
      self.remove(heap,idx*2+2,x)
      
results = []
minheap = []
maxheap = []
T = int(input())

for _ in range(T):
  k = int(input())
  minheap.clear()
  maxheap.clear()
  for _ in range(k):
    oper, n = input().strip().split()
    if oper == 'I':
      heappush(minheap, int(n))
      heappush(maxheap, -1*int(n))
    else:
      if len(minheap) == 0:
        continue
      elif n == '1':
        max_item = -1*heappop(maxheap)
        DBEQ().remove(minheap,0,max_item)
      elif n == '-1':
        min_item = heappop(minheap)
        DBEQ().remove(maxheap,0,-1*min_item)

  if len(minheap) == 0:
    results.append('EMPTY')
  else:
    results.append('{0} {1}'.format(-1*maxheap[0], minheap[0]))

for result in results:
  print(result)