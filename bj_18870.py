N = int(input())
xs = list(map(int, input().split()))

def compress_coord(xs):
    x_compressed = []
    for ind, x in enumerate(xs):
        xp = [i-x for i in xs]
        xp = sum([1 if i<0 else 0 for i in xp])
        x_compressed.append(xp)
    return x_compressed

for xp in compress_coord(xs):
    print(xp, end=' ')