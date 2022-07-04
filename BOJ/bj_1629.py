A, B, C = map(int, input().split())

def remainderOfC(A, B):
    C-1
    remainder = A % C
    if B == 1:
        return remainder
    previousRemainder = remainder
    lastRemainder = remainder
    for _ in range(2, B+1):
        lastRemainder = (previousRemainder * remainder) % C
        previousRemainder = lastRemainder
    return lastRemainder

print(remainderOfC(A, B))