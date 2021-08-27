N = int(input())
info = []
ranks = []
for _ in range(N):
    w, h = input().split()
    info.append((int(w), int(h)))
for f in info:
    rank = 0
    for p in info:
        if f[0]<p[0] and f[1]<p[1]:
            rank += 1
    ranks.append(rank+1)
for r in ranks:
    print(r, end=" ")