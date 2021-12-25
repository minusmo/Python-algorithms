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
    for i in team[1:]:
        for j in team[1:]:
            if i != j:
                total_stat += stats[i-1][j-1]
    return total_stat

def find_pairs(start):
    last_added = start[-1]
    pairs_left = [(i, last_added) for i in start[:-1]]
    pairs_right = [(last_added, i) for i in start[:-1]]
    return pairs_left + pairs_right

def calculate_pairs(pairs):
    total_stat = 0
    for pair in pairs:
        total_stat += stats[pair[0]-1, pair[1]-1]
    return total_stat

def search(n, calculated_stat):
    global min_diff, start, link, chosen
    if n >= 2:
        pairs = find_pairs(start)
        total_stat = calculate_pairs(pairs)
        calculated_stat += total_stat
    if n == N/2:
        # calculate difference
        for i in range(1, N+1):
            if chosen[i] == 0:
                link.append(i)
        
        diff = abs(calculated_stat - calculate(link))
        min_diff = min(min_diff, diff)
        link = [0]
    else:
        if chosen[1] == 0 and sum(chosen[1:]) == 1:
            return
        for i in range(1, N+1):
            if chosen[i] == 0:
                start.append(i)
                chosen[i] = 1
                search(n+1, calculated_stat)
                start.pop()
                chosen[i] = 0

search(0, 0)
print(min_diff)
"""
1234

12 34
13 24
14 23
---
21 x
23 x
24 x
31 x
32 x
34 x
41 x
42 x
43 x

123456

123 456 / 12 21 / 13 23 31 32 / 17 27 37 71 72 73 
124 356
125 346
126 345
134 256 / 13 31 / 14 34 41 43
135 246
136 245
145 236
146 235
156 234
---
213
214
215
216
...
"""