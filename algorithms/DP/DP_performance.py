import time

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + n

def fibonacci_dp(n):
    results = [0 for _ in range(n+1)]
    results[0] = 0
    results[1] = 1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    for i in range(2, n+1):
        results[i] = results[i-1] + results[i-2]
    return results[-1]

startRecursive = time.time()
print(fibonacci_recursive(10))
endRecursive = time.time()
print(endRecursive - startRecursive)

startDp = time.time()
print(fibonacci_dp(10))
endDp = time.time()
print(endDp - startDp)