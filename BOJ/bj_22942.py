import sys
from collections import deque
input = sys.stdin.readline

# 2<= N <= 200000
N = int(input())
circles = [None for _ in range(20000001)]

isRightData = True
for _ in range(N):
    x, r = map(int, input().split())
    if circles[(x-r)+1000000] != None or circles[(x+r)+1000000] != None:
        isRightData = False
    else:
        circles[(x-r)+1000000] = '('
        circles[(x+r)+1000000] = ')'

if not isRightData:
    print('NO')
else:
    circles = list(filter(lambda x: x != None, circles))

    stack = deque()
    for item in circles:
        if item == '(':
            stack.append(item)
        elif item == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                isRightData = False
                break
    if len(stack) != 0:
        isRightData = False
    if isRightData:
        print('YES')
    else:
        print('NO')