import sys
from heapq import nlargest
input = sys.stdin.readline

N = int(input())
heap = []
temp = []
result = []
for _ in range(N):
    temp.extend(result)
    temp.extend(list(map(int, input().split())))
    result = nlargest(N,temp)
    temp.clear()

print(result[N-1])
