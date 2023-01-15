import sys
from heapq import heappop, heappush
from collections import defaultdict
input = sys.stdin.readline

# unique container
hash = defaultdict(int)
minheap = []
maxheap = []

T = int(input())

for _ in range(T):
  k = int(input())
  minheap.clear()
  maxheap.clear()
  hash.clear()
  for _ in range(k):
    oper, n = input().strip().split()
    if oper == 'I':
      n = int(n)
      hash[n] += 1
      heappush(minheap, n)
      heappush(maxheap, -n)
    else:
      if n == '1':
        if len(maxheap) == 0:
          continue
        if -maxheap[0] in hash:
          max_item = -heappop(maxheap)
          hash[max_item] -= 1
          if hash[max_item] == 0:
            del hash[max_item]
        else:
          while not -maxheap[0] in hash:
            heappop(maxheap)
            if len(maxheap) == 0:
              break
          if len(maxheap) != 0:
            max_item = -heappop(maxheap)
            hash[max_item] -= 1
            if hash[max_item] == 0:
              del hash[max_item]
        
      elif n == '-1':
        if len(minheap) == 0:
          continue
        if minheap[0] in hash:
          min_item = heappop(minheap)
          hash[min_item] -= 1
          if hash[min_item] == 0:
            del hash[min_item]
        else:
          while not minheap[0] in hash:
            heappop(minheap)
            if len(minheap) == 0:
              break
          if len(minheap) != 0:
            min_item = heappop(minheap)
            hash[min_item] -= 1
            if hash[min_item] == 0:
              del hash[min_item]
          
  if len(hash) == 0:
    print('EMPTY')
  else:
    hash_vals = list(hash.keys())
    max_val, min_val = hash_vals[0], hash_vals[0]
    for item in hash_vals:
      if item > max_val:
        max_val = item
      if item < min_val:
        min_val = item
    print('{0} {1}'.format(max_val, min_val))