N = int(input())
stats = []

for _ in range(N):
    stats.append(list(map(int, input().split())))

min_diff = 100 * N
start = [0]
link = [0]
chosen = [0]*(N+1)

def calculate(team):
    total_stat = 0
    for i in team:
        for j in team:
            if i != j:
                total_stat += stats[i-1][j-1]
    return total_stat
                
def search(n):
    global min_diff, start, link, chosen
    if n == N/2:
        # calculate difference
        for i in range(1, N+1):
            if chosen[i] == 0:
                link.append(i)
        diff = abs(calculate(start) - calculate(link))
        min_diff = min(min_diff, diff)
    else:
        for i in range(1, N+1):
            if chosen[i] == 0:
                start.append(i)
                chosen[i] = 1
                search(n+1)
                start.pop()
                chosen[i] = 0

search(0)
print(min_diff)
"""
123

12
13
21
23
31
32
"""