N, M, B = map(int, input().split())
land = []
current_blocks = 0
for _ in range(M):
    row = map(int, input().split())
    land.append(row)
    current_blocks += sum(row)

# 0.083 -> 0.083 - /99
# 63.91 -> 0.91 + /1
# 63.91 -> 0.91 + /0