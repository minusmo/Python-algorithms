from collections import defaultdict, deque
import sys
input = sys.stdin.readline

tree = defaultdict(set)
N = int(input())
vertices = list(map(int,input().split()))
vertex_to_remove = int(input())
root = -1
for idx, vertex in enumerate(vertices):
  if vertex == -1:
    root = idx
  else:
    tree[vertex].add(idx)
  if not idx in tree:
    tree[idx] = set()

q = deque()
q.append(vertex_to_remove)
while len(q) != 0:
  current_v = q.popleft()
  for child in tree[current_v]:
    q.append(child)
  del tree[current_v]

for vertex in tree.keys():
  if vertex_to_remove in tree[vertex]:
    tree[vertex].remove(vertex_to_remove)


leaves = 0
if vertex_to_remove != root:
  for vertex, adj_vertices in tree.items():
    if len(adj_vertices) == 0:
      leaves += 1
    
print(leaves)