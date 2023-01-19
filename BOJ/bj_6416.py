import sys
from collections import defaultdict

input = sys.stdin.readline

vertices = set()
edges_out = defaultdict(list)
edges_in = defaultdict(set)
root = -1
is_tree = True
while True:
  nodes = input().split()
  if nodes == '':
    vertices.clear()
    edges_in.clear()
    edges_out.clear()
    root = -1
    is_tree = True
    continue
  if not is_tree:
    continue
  for i in range(0,len(nodes)/2,2):
    u = int(nodes[i])
    v = int(nodes[i+1])
    if u == -1:
      break
    if u == 0:
      # check if it is a tree
      vertices.clear()
      edges_in.clear()
      edges_out.clear()
      root = -1
      pass
    else:
      vertices.add(u)
      vertices.add(v)
      if u in edges_in[v]:
        is_tree = False
      else:
        edges_in[v].add(u)
      