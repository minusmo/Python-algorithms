"""
N = int(input())

sum = 1
time = 1
while sum < N:
    sum += 6 * time
    time += 1
print(time)
"""

# 재귀적 풀이
def get_livings(k, n):
    if k == 0:
        return n
    living = 0
    for i in range(1, n+1):
        living += get_livings(k-1, i)
    return living



T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    print(get_livings(k, n))
