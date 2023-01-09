import sys
input = sys.stdin.readline

N, M = map(int, input().split())

n = set()

for _ in range(N):
    n.add(input())

count = 0    
for _ in range(M):
    m = input()
    if m in n:
        count += 1
print(count)