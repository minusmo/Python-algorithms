k, n = input().split()
k, n = int(k), int(n)
lines = []
for _ in range(k):
    line = int(input())
    lines.append(line)
minimum = min(lines)
if n == k:
    print(max(lines))
else:
    if max(lines) 
    for i in range(minimum, 0, -1):
        lans = [j//i for j in lines]
        if sum(lans) >= n:
            print(i)
            break