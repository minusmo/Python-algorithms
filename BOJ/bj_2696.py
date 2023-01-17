import sys
from heapq import heappop, heappush

input = sys.stdin.readline

T = int(input())
items = []
mean_at_odds = []
sequence = []

for _ in range(T):
  sequence.clear()
  M = int(input())
  while M > 0:
    sequence.extend(list(map(int, input().split())))
    M -= 10
  items.clear()
  mean_at_odds.clear()
  for idx, item in enumerate(sequence):
    if idx % 2 == 0:
      if idx == 0:
        mean_at_odds.append(item)
        heappush(items, item)
        continue
      heappush(items, item)
      smaller_items = []
      for _ in range(int(len(items)/2)):
        smaller_items.append(heappop(items))
      mean_item = heappop(items)
      mean_at_odds.append(mean_item)
      heappush(items, mean_item)
      for smaller_item in smaller_items:
        heappush(items,smaller_item)
    else:
      heappush(items, item)
      
  print(len(mean_at_odds))
  idx = 0
  while idx < len(mean_at_odds):
    print(*mean_at_odds[idx:idx+10])
    idx += 10