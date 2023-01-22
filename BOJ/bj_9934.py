import sys
from collections import defaultdict, deque

input = sys.stdin.readline
K = int(input())
heap = defaultdict(defaultdict)
traversal_order = list(map(int,input().split()))

visited = set()
root = len(traversal_order)//2

def in_order(root_idx, left_end, right_end):
  left_idx = (root_idx+left_end) // 2
  right_idx = (root_idx+right_end) // 2
  root_item = traversal_order[root_idx]
  left_item = traversal_order[left_idx]
  right_item = traversal_order[right_idx]
  if root_item in visited:
    return
  else:
    if left_idx == root_idx or right_idx == root_idx:
      heap[root_item]['l'] = None
    elif left_idx >= 0 and left_item in visited:
      pass
    elif left_idx >= 0 and not left_item in visited:
      heap[root_item]['l'] = left_item
      in_order(left_idx,left_end,root_idx)
      
    visited.add(root_item)
    
    if left_idx == root_idx or right_idx == root_idx:
      heap[root_item]['r'] = None
    elif right_idx < len(traversal_order) and right_item in visited:
      pass
    elif right_idx < len(traversal_order) and not right_item in visited:
      heap[root_item]['r'] = right_item
      in_order(right_idx,root_idx,right_end)
    
in_order(root,0,len(traversal_order))

q = deque()
q.append(traversal_order[root])
level = 1
visits = 0
while len(q) != 0:
  current_item = q.popleft()
  print(current_item, end=' ')
  visits += 1
  if (2**level-1) == visits:
    print()
    level += 1
  if heap[current_item]['l']:
    q.append(heap[current_item]['l'])
  if heap[current_item]['r']:
    q.append(heap[current_item]['r'])
  