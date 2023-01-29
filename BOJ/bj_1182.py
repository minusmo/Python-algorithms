import sys
input = sys.stdin.readline

N, S = map(int, input().split())
sequence = list(map(int,input().split()))

count = 0
visited = set()
def find_sub_seq_sum(idx,summation):
  global count
  if len(visited) > 0 and summation == S:
    count += 1
  for i in range(idx+1,N):
    if i in visited:
      continue
    else:
      visited.add(i)
      summation += sequence[i]
      find_sub_seq_sum(i,summation)
      visited.remove(i)
      summation -= sequence[i]

find_sub_seq_sum(-1,0)
      
print(count)