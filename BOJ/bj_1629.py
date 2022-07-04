A, B, C = map(int, input().split())

def remainder(A, B, C):
    remainder = 1
    A = A % C
    if A == 0:
        return 0
    while B > 0:
        # if B is odd
        if (B & 1) == 1:
            remainder = (remainder * A) % C
        # and now make B even
        B = B >> 1 # divide by 2
        A = (A*A) % C
    return remainder

print(remainder(A, B, C))