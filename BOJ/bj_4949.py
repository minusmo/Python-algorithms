from collections import deque

lines = []
while True:
    line = input()
    if line != '.':
        lines.append(line)
    else:
        break
is_balanced = []
stack = deque()
for line in lines:
    stack.clear()
    for char in line:
        if char == ']':
            try:
                if stack[-1] != '[':
                    stack.append(char)
                else:
                    stack.pop()
            except:
                stack.append(char)
        elif char == ')':
            try:
                if stack[-1] != '(':
                    stack.append(char)
                else:
                    stack.pop()
            except:
                stack.append(char)
        elif char == '[' or char == '(':
            stack.append(char)
    if len(stack) == 0:
        is_balanced.append('yes')
    else:
        is_balanced.append('no')
        
for isbal in is_balanced:
    print(isbal)