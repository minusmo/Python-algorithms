N = int(input())

stairs = []
for _ in range(N):
    stairs.append(int(input()))

def max_score(stairs):
    max_stairs = [0 for _ in range(len(stairs))]
    if len(stairs) < 3:
        max_stairs[-1] = stairs[0] + stairs[1]
    for i in range(len(stairs)-1,0,-1):
        max_stairs[]
    return max_stairs[-1]