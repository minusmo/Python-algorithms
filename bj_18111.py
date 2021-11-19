N, M, B = map(int, input().split())
land = []
current_blocks = 0
for _ in range(N):
    row = list(map(int, input().split()))
    land.append(row)
    current_blocks += sum(row)

start = (current_blocks//(N*M)) if (current_blocks//(N*M)) > 0 else 0
end = start + B//(N*M) + 1
time = 0
level = 0
answers = []
inven = B

for i in range(start, end+1):
    for row in land:
        for dist in row:
            if i-dist < 0:
                time += (dist-i)*2
                inven += dist-i
    for row in land:
        for dist in row:
            if i-dist >= 0:
                time += (i-dist)*1
                inven -= i-dist
    if inven < 0:
        time = 0
        inven = B
        continue
    else:
        level = i
        answers.append((time, level))
        time = 0
        inven = B

for ind, answer in enumerate(answers):
    if ind < len(answers)-1:
        if answer[0] < answers[ind+1][0]:
            answers = answers[0:ind+1]
            break
    
max_level = max(answers, key=lambda x: x[1])
print(max_level[0], max_level[1], sep=' ')