from collections import deque

n = int(input())
stack = deque()
for _ in range(n):
    num = int(input())
    if not num == 0:
        stack.append(num)
    else:
        stack.pop()
print(sum(list(stack)))