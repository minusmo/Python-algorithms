import sys
input = sys.stdin.readline

# 1 <= N <= 1000
N = int(input())

# (original idx, move)
items = list(map(int, input().split()))

pop_seq = []

pop_idx = 0
while len(pop_seq) != N:
    pop_seq.append(pop_idx+1)
    if len(pop_seq) == N:
        break
    items[pop_idx] = 0
    move = items[pop_idx]
    right = True if move > 0 else False
    steps = abs(move)
    if right:
        while steps > 0:
            pop_idx += 1
            pop_idx %= N
            if items[pop_idx] == 0:
                continue
            else:
                steps -= 1
    else:
        while steps > 0:
            pop_idx -= 1
            if pop_idx < 0:
                pop_idx += N
            if items[pop_idx] == 0:
                continue
            else:
                steps -= 1
        
print(*pop_seq)