N = int(input())
def sugar(N):
    y = 0
    for i in range(N//3+1):
        y = (N-3*i) // 5
        if (N-3*i) % 5 == 0:
            return i + y
    if N % 3 == 0:
        return N // 3
    else:
        return -1
print(sugar(N))