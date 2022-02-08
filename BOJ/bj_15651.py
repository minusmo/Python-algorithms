# back tracking

N, M = map(int, input().split())

def unique_series(n,m):
    def dfs(n,m,series):
        if m == 0:
            print(" ".join(map(str,series)))
            return
        
        for i in range(1, n+1):
            series.append(i)
            dfs(n,m-1,series)
            # pruning
            series.pop()
    
    dfs(n,m,[])
    

unique_series(N,M)

"""
dfs를 사용할 때는
state space tree(상태 공간 트리):
문제 해결 과정의 중간 상태를 각각의 노드로 나타낸 트리
를 생각하자

탐색의 범위와 차례도 생각할것!
트리의 형태로 탐색을 진행 한다!
"""