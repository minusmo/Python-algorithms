import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
items = map(int, input().split())
stack = deque()

result = []
for item in enumerate(items):
    if item[0] == 0:
        result.append(0)
    else:
        while len(stack) != 0 and item[1] > stack[-1][1]:
            stack.pop()
        if len(stack) == 0:
            result.append(0)
        else:
            result.append(stack[-1][0]+1)
    stack.append(item)

print(*result)