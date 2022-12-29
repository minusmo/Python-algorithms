import sys
input = sys.stdin.readline

# 1 <= N <= 1000
N = int(input())
items = list(map(int, input().split()))

pop_seq = []

pop_idx = 0
while len(items) != 0:
    pop_seq.append(pop_idx)
    next_move = items.pop(pop_idx)
    if pop_idx + next_move > len(items):
        next_pop = (pop_idx + next_move) % len(items) 
    elif pop_idx + next_move <= len(items):
        # -1
        pass
    elif pop_idx + next_move >= 0:
        # just pop
        pass
    elif pop_idx + next_move < 0:
        # +1
        pass
    