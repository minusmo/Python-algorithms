# 백트래킹 예제: n by n 체스판에 n개의 퀸을 놓는 경우의 수를 출력하는 문제

def nqueen(n):
    def isAvailable(currentCandidate, currentCol):
        currentRow = len(currentCandidate)
        # promising: 가능한 경우의 수를 체크하는 과정
        for i in range(currentRow):
            # promising 중 같은 column에 있는지 혹은 대각선에 있는지를 검사
            if currentCandidate[i] == currentCol or (abs(currentCandidate[i]-currentCol)) == currentRow-i:
                return False
        return True
    
    def dfs(n, currentRow, currentCandidate):
        if currentRow == n:
            print(currentCandidate)
            return
        
        for i in range(n):
            if isAvailable(currentCandidate, i):
                currentCandidate.append(i)
                dfs(n, currentRow+1, currentCandidate)
                # pruning: 가능하지 않은 경우의 수를 제거하는 과정
                currentCandidate.pop(len(currentCandidate)-1)
    
    dfs(n, 0, [])
    
n = int(input())

nqueen(n)