import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  # 0 <N<=M<30
  N,M = map(int, input().split())
  table = [[1 for _ in range(M+1)] for _ in range(N+1)]
  for n in range(2,N+1):
    for m in range(1,M+1):
      table[n][m] = 0
      for i in range(1,m):
        table[n][m] += table[n-1][i]
  print(sum(table[N])-1)