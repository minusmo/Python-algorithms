# 백트래킹 예제: n by n 체스판에 n개의 퀸을 놓는 경우의 수를 출력하는 문제

def isAvailable(currentCandidate, currentCol):
    currentRow = len(currentCandidate)
    for i in range(currentRow):
        if currentCandidate[i] == currentCol or (abs(currentCandidate[i]-currentCol)) == currentRow-i:
            return False
    return True
    
def dfs(n, currentRow, currentCandidate):
    ways = 0
    if currentRow == n:
        return 1
    
    for i in range(n):
        if isAvailable(currentCandidate, i):
            currentCandidate.append(i)
            cands = dfs(n, currentRow+1, currentCandidate)
            ways += cands
            currentCandidate.pop(len(currentCandidate)-1)
    return ways

def nqueen(n):
    nq = [0] * (n+1)
    if n == 1:
        return 1
    if n < 5:
        return 0
    if n == 5:
        return 10
    nq[1] = 1
    nq[5] = 10
    
    for i in range(6, n+1):
        nq[i] = nq[i-1] + dfs(i,1,[i-1])
    return nq[n]
    
n = int(input())

print(nqueen(n))
# print(len(nqueen(n)))