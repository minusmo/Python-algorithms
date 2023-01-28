import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N,M = map(int,input().split())
graph = defaultdict(list)
for _ in range(M):
  u,v = map(int,input().split())
  graph[v].append(u)

maxheap = []
max_hacked = -1
q = deque()
visited = set()
for vertex in range(1,N+1):
  if len(graph[vertex]) == 0:
    continue
  visited.clear()
  visits = 0
  q.clear()
  
  q.append(vertex)
  visits += 1
  visited.add(vertex)
  while len(q) > 0:
    current_v = q.popleft()
    for adj_v in graph[current_v]:
      if not adj_v in visited:
        visited.add(adj_v)
        visits += 1
        q.append(adj_v)
  if visits > max_hacked:
    maxheap.clear()
    maxheap.append(vertex)
    max_hacked = visits
  elif visits == max_hacked:
    maxheap.append(vertex)

print(*maxheap)

# import sys
# from collections import deque
# input = sys.stdin.readline
# print = sys.stdout.write
# ############################입력 처리
# n, m = map(int, input().split())
# arr = [[] for _ in range(n+1)]
# ans = [0 for _ in range(n+1)]
# for i in range(m):
#     a, b = map(int, input().split())
#     arr[b].append(a)

# ###############bfs 함수 
# def bfs(start):
#     flag = [0] * (n+1)
#     q = deque([start])
#     flag[start] = 1
#     while q:
#         node = q.popleft()
#         ans[start] += 1
#         for i in arr[node]:
#             if flag[i] == 0:
#                 flag[i] = 1
#                 q.append(i)
# #########################메인                
# maxlist = list()
# mx = -1
# for i in range(1, n+1):
#     if len(arr[i]) != 0:
#         bfs(i)

#     if ans[i] > mx:
#         maxlist.clear()
#         mx = ans[i]
#         maxlist.append(i)
#     elif ans[i] == mx:
#         maxlist.append(i)
#     else:
#         continue

# #######################정답 출력
# for i in maxlist: 
#     print(str(i) + " ")

