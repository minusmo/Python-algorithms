# 백트래킹 예제: n by n 체스판에 n개의 퀸을 놓는 경우의 수를 출력하는 문제

ways = 0
def dfs(currentRow):
    global ways
    if currentRow == n:
        ways += 1
        return

    for i in range(n):
        isOk = True
        if cols[i] == 1:
            continue
        for j in range(currentRow):
            if abs(currentCands[j]-i) == currentRow-j:
                isOk = False
        if isOk:
            currentCands[currentRow] = i
            cols[i] = 1
            dfs(currentRow+1)
            cols[i] = 0
            currentCands[currentRow] = 0

    
n = int(input())
currentCands = [0] * n
cols = [0] * n
dfs(0)
print(ways)