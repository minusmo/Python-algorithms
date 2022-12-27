import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
series = []

for _ in range(N):
    series.append(int(input()))

items = [i for i in range(N,0,-1)]
stack = deque()

operations = []

while True:
    if len(stack) == 0:
        if len(items) == 0:
            break
        else:
            stack.append(items.pop())
            operations.append('+')
    else:
        if stack[-1] == series[0]:
            operations.append('-')
            series.pop(0)
            stack.pop()
        else:
            if len(items) == 0:
                operations.clear()
                operations.append('NO')
                break
            else:
                stack.append(items.pop())
                operations.append('+')
                
for operation in operations:
    print(operation)