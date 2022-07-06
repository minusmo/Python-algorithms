from collections import defaultdict
A, B = map(int, input().split())

def minOperations(A, B) -> int:
    if A == B:
        return 0
    doubles = defaultdict(int)
    doubles[A] = 0
    padds = defaultdict(int)
    padds[A] = 0
    for i in range(A*2, B+1):
        if i/2 in padds:
            doubles[i] = padds[i//2] + 1
        elif i/2 in doubles:
            doubles[i] = doubles[i//2] + 1
        elif (i-1)/10 in padds:
            padds[i] = padds[(i-1)//10] + 1
        elif (i-1)/10 in doubles:
            padds[i] = doubles[(i-1)//10] + 1
        else:
            continue
    
    if B in doubles:
        return doubles[B] + 1
    elif B in padds:
        return padds[B] + 1
    else:
        return -1
    
print(minOperations(A,B))