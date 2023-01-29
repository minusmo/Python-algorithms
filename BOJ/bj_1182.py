import sys
input = sys.stdin.readline

N, S = map(int, input().split())
sequence = list(map(int,input().split()))
prefix_sums = [sum(sequence[:i]) for i in range(1,N+1)]

count = 0
if sequence[0] == S:
  count += 1
if prefix_sums[N-1] == S:
  count += 1
for i in range(N):
  for j in range(i+1,N):
    if prefix_sums[j] - prefix_sums[i] == S:
      count += 1
      
print(count)