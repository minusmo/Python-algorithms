from collections import Counter

n = int(input())
N = input().split()
m = int(input())
M = input().split()

n_counts = Counter(N)

m_counts = []

for i in M:
    print(n_counts[i], end=' ')