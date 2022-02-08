from collections import deque
n = int(input())

prs = []
for _ in range(n):
    pr = input()
    prs.append(pr)

is_balanced = []
stack = deque()
for line in prs:
    stack.clear()
    for char in line:
        if char == ')':
            try:
                if stack[-1] != '(':
                    stack.append(char)
                else:
                    stack.pop()
            except:
                stack.append(char)
        else:
            stack.append(char)
    if len(stack) == 0:
        is_balanced.append('YES')
    else:
        is_balanced.append('NO')
        
for isbal in is_balanced:
    print(isbal)