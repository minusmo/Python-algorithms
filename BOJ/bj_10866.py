from collections import deque
import sys
input = sys.stdin.readline
# 1 <= N <= 10000
N = int(input())
count = 0
dq = deque()
for _ in range(N):
    raw_input = input().split()
    action = raw_input[0]
    val = None
    if len(raw_input) == 2:
        val = raw_input[1]
    
    if action == 'push_front':
        dq.appendleft(val)
        count += 1
        continue
    elif action == 'push_back':
        dq.append(val)
        count += 1
        continue
    elif action == 'pop_front':
        if count == 0:
            print(-1)
        else:
            count -= 1
            popped = dq.popleft()
            print(popped)
        continue
    elif action == 'pop_back':
        if count == 0:
            print(-1)
        else:
            count -= 1
            popped = dq.pop()
            print(popped)
        continue
    elif action == 'size':
        print(count)
        continue
    elif action == 'empty':
        if count == 0:
            print(1)
        else:
            print(0)
        continue
    elif action == 'front':
        if count == 0:
            print(-1)
        else:
            print(dq[0])
        continue
    elif action == 'back':
        if count == 0:
            print(-1)
        else:
            print(dq[-1])