N = int(input())
xs = list(map(int, input().split()))

def compress_coord(xs):
    x_compressed = []
    xss = list(sorted(set(xs)))
    inds = [i for i in range(len(xss))]
    d = dict(zip(xss, inds))
    for x in xs:
        x_compressed.append(d[x])
    return x_compressed

for xp in compress_coord(xs):
    print(xp, end=' ')