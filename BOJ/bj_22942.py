import sys
from collections import deque
input = sys.stdin.readline

# 2<= N <= 200000
# -1000000 <= x <= 1000000
# 1 <= r <= 10000
N = int(input())
circles = [None for _ in range(20000001)]

is_right_data = True
for _ in range(N):
    x, r = map(int, input().split())
    if circles[(x-r)+1000000] != None or circles[(x+r)+1000000] != None:
        is_right_data = False
    else:
        circles[(x-r)+1000000] = r
        circles[(x+r)+1000000] = -r

if not is_right_data:
    print('NO')
else:
    circles = list(filter(lambda x: x != None, circles))

    stack = deque()
    for item in circles:
        if item > 0:
            stack.append(item)
        else:
            if len(stack) != 0 and (stack[-1] + item) == 0:
                stack.pop()
            else:
                is_right_data = False
                break
    if len(stack) != 0:
        is_right_data = False
    if is_right_data:
        print('YES')
    else:
        print('NO')