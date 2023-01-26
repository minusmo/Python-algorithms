import sys
from collections import deque, defaultdict

input = sys.stdin.readline
tree = defaultdict(set)
# 2<=N<=500000
N, W = map(int, input().split())
ROOT = 1
for _ in range(N-1):
  u, v = map(int,input().split())
  tree[u].add(v)
  tree[v].add(u)

water_stored = [0 for _ in range(N+1)]
water_stored[1] = W
node_leaves = set()
def waterfall(tree, ROOT, water_stored):
		visited = set()
		q = deque()
		q.append(ROOT)
		while len(q) != 0:
			current_v = q.popleft()
			visited.add(current_v)
			children = 0
			if current_v == ROOT:
				children = len(tree[current_v])
			else:
				children = len(tree[current_v])-1
			water_per_child = 0.0
			if children > 0:
				water_per_child = water_stored[current_v] / children
			elif children == 0:
				node_leaves.add(current_v)
			for child in tree[current_v]:
				if not child in visited:
					water_stored[child] += water_per_child
					q.append(child)
			
waterfall(tree, ROOT, water_stored)

avg_sum = 0.0
for leaf in node_leaves:
  avg_sum += water_stored[leaf]

if len(node_leaves) > 0:
  print(format(avg_sum/len(node_leaves),'.10f'))
else:
  print(avg_sum)