from sys import maxsize
A, B = map(int, input().split())

def minOperations(A, B) -> int:
    if A == B:
        return 0
    ops = [None] * maxsize
    ops[A] = 0
    ops[A*2] = 1
    ops[A*10 + 1] = 1
    for i in range(A*2 + 1, B+1):
        if (i & 1) == 0:
            ops[i] = ops[i/2] + 1 if ops[i/2] != None else None
        elif i % 10 == 1:
            ops[i] = ops[(i-1)/10] + 1 if ops[(i-1)/10] != None else None
        else:
            continue
    
    return ops[B] + 1 if ops[B] != None else -1
    
print(minOperations(A,B))