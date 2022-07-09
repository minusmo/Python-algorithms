N = int(input())
house = []
for _ in range(N):
    row = [int(i) for i in input().split()]
    house.append(row)

hpaths = [[0 for _ in range(N)] for _ in range(N)]
vpaths = [[0 for _ in range(N)] for _ in range(N)]
dpaths = [[0 for _ in range(N)] for _ in range(N)]
hpaths[0][1] = 1
def getPaths(house, N) -> int:
    for r in range(N):
        for c in range(2,N):
            if house[r][c] == 0:
                if c >= 1:
                    hpaths[r][c] = hpaths[r][c-1] + dpaths[r][c-1]
                if r >= 1:
                    vpaths[r][c] = vpaths[r-1][c] + dpaths[r-1][c]
                if r >= 1 and c >= 1:
                    dpaths[r][c] = dpaths[r-1][c-1] + hpaths[r-1][c-1] + vpaths[r-1][c-1] if house[r-1][c] == 0 and house[r][c-1] == 0 else 0
    return hpaths[N-1][N-1] + vpaths[N-1][N-1] + dpaths[N-1][N-1]

print(getPaths(house, N))