from collections import defaultdict
import sys
input = sys.stdin.readline

edges = []
tree = defaultdict(set)

N = int(input())
for _ in range(N-1):
  v1, v2 = map(int, input().split())
  tree[v1].add(v2)
  tree[v2].add(v1)
  edges.append((v1,v2))
  
def execute(query, param):
  if query == 1:
    if len(tree[param]) > 1:
      print('yes')
    else:
      print('no')
  elif query == 2:
    print('yes')

q = int(input())

for _ in range(q):
  query, param = map(int, input().split())
  execute(query,param)