k, n = input().split()
k, n = int(k), int(n)
lines = []
for _ in range(k):
    line = int(input())
    lines.append(line)
# minimum = min(lines)

# max_len = -1
# for i in range(minimum, 0, -1):
#     lans = [j//i for j in lines]
#     if sum(lans) >= n:
#         max_len = i
#         break
M = max(lines)
m = -1
length = -1
lengs = [i for i in range(1,M+1)]
start = 0
end = M+1
while start < end:
    lengs = lengs[start:end]
    mid = lengs[round((start+end)/2)]
    if sum([line//mid for line in lines]) >= n and mid > m:
        m = mid
        start = round((start+end)/2)
    else:
        end = round((start+end)/2)
print(m)

# 4 4
# 10
# 3
# 1
# 1
# :3

# 4 5
# 10 
# 1
# 1
# 1
# :2