import sys
input = sys.stdin.readline

# 1 <= N <= 1000
N = int(input())

# (original idx, move)
items = list(map(int, input().split()))

pop_seq = []

pop_idx = 0
def next_pop_idx_right(N, items, pop_idx, steps) -> int:
    while steps > 0:
        pop_idx += 1
        pop_idx %= N
        if items[pop_idx] == 0:
            continue
        else:
            steps -= 1
    return pop_idx

def next_pop_idx_left(N, items, pop_idx, steps):
    while steps > 0:
        pop_idx -= 1
        if pop_idx < 0:
            pop_idx += N
        if items[pop_idx] == 0:
            continue
        else:
            steps -= 1
    return pop_idx

while len(pop_seq) != N:
    pop_seq.append(pop_idx+1)
    if len(pop_seq) == N:
        break
    move = items[pop_idx]
    items[pop_idx] = 0
    right = True if move > 0 else False
    steps = abs(move)
    if right:
        pop_idx = next_pop_idx_right(N, items, pop_idx, steps)
    else:
        pop_idx = next_pop_idx_left(N, items, pop_idx, steps)
        
print(*pop_seq)