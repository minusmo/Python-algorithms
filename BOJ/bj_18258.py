from queue import deque
import sys
N = int(sys.stdin.readline())
iq = deque()
count = 0
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        iq.append(int(command[1]))
        count += 1
    else:
        if command[0] == "front":
            if count == 0:
                print(-1)
                continue
            print(iq[0])
        elif command[0] == "pop":
            if count == 0:
                print(-1)
                continue
            count -= 1
            print(iq.popleft())
        elif command[0] == "back":
            if count == 0:
                print(-1)
                continue
            print(iq[count-1])
        elif command[0] == "size":
            print(count)
        elif command[0] == "empty":
            if count == 0:
                print(1)
            else:
                print(0)