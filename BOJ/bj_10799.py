import sys
from collections import deque
input = sys.stdin.readline

# 2 <= N <= 100000
pattern = input()

stack = deque()
lasers = [0 for _ in range(len(pattern))]

total_splits = 0
for item in enumerate(pattern):
    if len(stack) == 0:
        stack.append(item)
        lasers[item[0]] = lasers[item[0]-1] if (item[0]-1) >= 0 else 0
    elif stack[-1][1] == '(' and item[1] == ')':
        if abs(stack[-1][0] - item[0]) == 1:
            lasers[item[0]] = (lasers[item[0]-1] if (item[0]-1) >= 0 else 0) + 1
        else:
            lasers[item[0]] = lasers[item[0]-1] if (item[0]-1) >= 0 else 0
            lasers_in_between = lasers[item[0]] - lasers[stack[-1][0]]
            total_splits += (lasers_in_between + 1)
        stack.pop()
    else:
        stack.append(item)
        lasers[item[0]] = lasers[item[0]-1] if (item[0]-1) >= 0 else 0
        
print(total_splits)