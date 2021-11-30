N = int(input())

stairs = []
for _ in range(N):
    stairs.append(int(input()))

def max_score(stairs):
    max_stairs = [0 for _ in range(len(stairs)+1)]
    
    if len(stairs) == 1:
        return stairs[0]
    elif len(stairs) == 2:
        return stairs[0]+stairs[1]
    
    stairs = [0] + stairs
    max_stairs[1] = stairs[1]
    max_stairs[2] = stairs[1]+stairs[2]
    for i in range(3, len(stairs)+1):
        max_stairs[i] = stairs[i]+max(max_stairs[i-1] if max_stairs[i-1] != max_stairs[i-2]+stairs[i-1] else -1, max_stairs[i-2])
    return max_stairs[-1]

print(max_score(stairs))