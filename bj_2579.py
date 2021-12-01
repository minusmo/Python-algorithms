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
    elif len(stairs) == 3:
        return max(stairs[0]+stairs[2], stairs[1]+stairs[2])
    
    stairs = [0] + stairs
    max_stairs[1] = stairs[1]
    max_stairs[2] = stairs[1]+stairs[2]
    for i in range(3, len(stairs)):
        max_stairs[i] = stairs[i]+max(stairs[i-1]+max_stairs[i-3], max_stairs[i-2])
    return max_stairs[-1]

print(max_score(stairs))
# 케이스를 정확히 분리할것!!!
# 10
# 100
# 100
# 1
# 1
# 100
# 100
# 1
# 1000
# 1000
# 1000