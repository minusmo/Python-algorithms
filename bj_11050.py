from math import factorial
n, k = input().split()
n, k = int(n), int(k)
def comb(n, k):
    if n < 0:
        return 0
    elif k > n:
        return 0
    elif n == 0 or k == 0:
        return 1
    return int(factorial(n)/(factorial(k)*factorial(n-k)))
print(comb(n, k))