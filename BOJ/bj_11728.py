from collections import deque
import sys
input = sys.stdin.readline

# 1<=N.M<=1000000
N, M = map(int, input().split())
A = deque(map(int, input().split()))
B = deque(map(int, input().split()))
merged = []
while len(A) != 0 and len(B) != 0:
  if A[0] < B[0]:
    merged.append(A.popleft())
  else:
    merged.append(B.popleft())

if len(A) == 0:
  merged.extend(B)
elif len(B) == 0:
  merged.extend(A)

print(*merged)