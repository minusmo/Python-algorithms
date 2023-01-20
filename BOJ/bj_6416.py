import sys
from collections import defaultdict, deque

input = sys.stdin.readline

targets = set()
vertices = set()
edges_out = defaultdict(list)
edges_in = defaultdict(set)
root = -1
is_tree = True
results = []
case_order = 1

while True:
  nodes = input().split()
  if len(nodes) == 0:
    continue
  if int(nodes[0]) < 0:
    break
  
  for i in range(0,len(nodes),2):
    u = int(nodes[i])
    v = int(nodes[i+1])
    if u < 0:
      break
    elif u == 0:
      # check if it is a tree and initialize variables
      for vertex in vertices:
        if not is_tree:
          break
        if root == -1 and not vertex in targets:
          root = vertex
        elif root != -1 and not vertex in targets:
          is_tree = False
          break
      
      if root == -1:
        is_tree = False
      else:
        # check if the graph has a cycle
        q = deque()
        q.append(root)
        visited = 0
        while len(q) != 0:
          current_vertex = q.popleft()
          visited += 1
          for adj_vertex in edges_out[current_vertex]:
            edges_in[adj_vertex].remove(current_vertex)
            if len(edges_in[adj_vertex]) == 0:
              q.append(adj_vertex)
        if visited != len(vertices):
          is_tree = False
              
      if len(vertices) == 0:
        is_tree = True
        
      condition = ' not ' if not is_tree else ' '
      results.append('Case {0} is'.format(case_order) + condition + 'a tree.')
      
      targets.clear()
      vertices.clear()
      edges_in.clear()
      edges_out.clear()
      root = -1
      case_order += 1
      is_tree = True
    elif not is_tree:
      continue
    else:
      vertices.add(u)
      vertices.add(v)
      targets.add(v)
      if u in edges_in[v]:
        is_tree = False
      elif len(edges_in[v]) > 0:
        is_tree = False
        continue
      else:
        edges_in[v].add(u)
      if root == u and v in edges_out[root]:
        is_tree = False
        continue
      else:
        edges_out[u].append(v)
        
for result in results:
  print(result)