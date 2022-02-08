from collections import Counter
N, M = map(int, input().split())
d = []
b = []
for _ in range(N):
    d.append(input())
for _ in range(M):
    b.append(input())
C = Counter(d)
C.subtract(b)
db = []
for elem, cnt in C.items():
    if cnt == 0:
        db.append(elem)
db.sort()
print(len(db))
for who in db:
    print(who)