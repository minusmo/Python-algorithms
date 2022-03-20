"""
Graph

그래프는 인접행렬을 이용한 방법과 연결리스트를 이용한 방법이 있는데,
인접행렬을 이용하는 방법은 2차원 배열을 이용한다.

인접행렬은 그래프간의 간선이 많이 존재하는 밀집 그래프를 표현하는데는 적합하나,
그래프 내의 적은 숫자의 간선을 가지는 희소 그래프의 경우에는 메모리의 낭비가 크므로 적합하지 않다.

인접행렬을 이용하면 두 정점을 연결하는 간선의 존재여부를 O(1)시간 안에 알 수 있다.
정점 i 와 j를 연결하는 간선이 있는지를 검사하려면 행렬의 [i][j]값을 조사하면 바로 알 수 있다.

또한 정점의 차수는 인접행렬의 행이나 열을 조사하면 알 수 있으므로 O(n)의 연산에 의해 알 수 있다.
정점 i에 대한 차수는 인접 배열의 i번째 행에 있는 값을 모두 더하면 된다.

degree(i) = sum(M[i][k]) for k in range(0, n)

정점을 삽입할 때 정점의 번호는 순차적으로 증가한다고 가정한다.
"""
max_vertex = 50

class Graph:
	def __init__(self, max_vertex, n):
		self.graph = [[None for _ in range(0, max_vertex)] for _ in range(0, max_vertex)]
		self.vertexes = n
		print(self.graph)

	# 정점을 하나 삽입하는 연산. 전체 정점의 개수를 1 증가시킨다.
	def insert_vertex(self, v):
		if self.vertexes > max_vertex:
			print("정점 개수 초과")
		self.vertexes += 1

	# 간선을 하나 삽입하는 연산. 정점 u에 간선(u, v)를 삽입한다.
	def insert_edge(self, start, end):
		if (start >= self.vertexes or end <= self.vertexes):
			print("정점 번호 오류")
		self.graph[start][end] = 1
		self.graph[end][start] = 1


"""
그래프의 탐색
1. 깊이우선탐색(depth first search: DFS)
깊이우선탐색은 먼저 시작 정점을 방문하고, 방문하였다고 표시한다.
그리고 이에 인접한 정점들 중 아직 방문하지 않은 정점을 선택하고, 
만약 그러한 정점이 없다면 탐색은 종료한다. 
만약 그러한 정점이 있다면, 그 정점을 시작 정점으로하여 깊이우선탐색을 다시 시작한다.

깊이우선탐색을 구현하는데에는 2가지 방법이 있는데,
하나는 위처럼 순환호출을 이용하는 것이고,
다른 하나는 명시적인 스택을 이용하여 방문한 정점들을 스택에 저장하였다가
다시 꺼내어 작업하는 것이다. 

지금은 순환호출을 이용하는 방법으로 구현해본다.
방문여부를 기록하기위해 배열 visited를 사용하며,
모든 정점의 visited 배열 값은 False로 초기화되고, 정점이 방문될 때마다
해당 정점의 visited 배열값은 True로 변경된다.  

dfs_mat 함수를 작성하고,
이 함수는 그래프와 시작정점을 인수로 받는다.

깊이우선탐색은 그래프의 모든 간선을 조사하므로, 정점의 수가 n이고 간선의 수가 e인 그래프를 
깊이우선탐색하는 시간은 그래프가 인접리스트 방식이라면 O(n+e)이고, 인접행렬로 표시되어 있다면
O(n^2)이다. 
이는 희소 그래프의 경우 깊이우선 탐색은 인접 리스트 방식이 인접 행렬 방식보다 시간적으로 유리함을
뜻한다. 
"""

visited = [ False for _ in range(0, max_vertex)]

def dfs_mat(graph, start_vertex_index):
	visited[start_vertex_index] = True # 방문한 정점 표시
	print(f"방문한 정점: {start_vertex_index}") # 방문한 정점 출력
	for w in range(0, graph.vertexes):
		if graph.graph[start_vertex_index][w] and not visited[w]:
			dfs_mat(graph, w)


"""
너비우선탐색(breadth first search: bfs)은 시작 정점으로부터 가까운 정점을 먼저 방문하고,
멀리 떨어져 있는 정점을 나중에 방문하는 순회방법이다.

너비우선탐색을 사용하기 위해서는 방문한 정점을 차례대로 저장한 후 꺼낼 수 있는 자료구조인
큐가 필요하다. 즉 정점이 방문될 때마다 큐에 방문된 정점을 삽입하고, 더이상 방문할 인접 정점이 없는 경우
큐의 앞에서 정점을 꺼내어 그 정점과 인접한 정점들을 모두 차례대로 방문하게 된다. 
초기상태의 큐는 시작정점만이 저장되고, 너비우선탐색 과정은 큐가 소진될 때까지 계속한다.

너비우선탐색의 특징은 시작 정점으로부터 거리가 가까운 정점의 순서대로 탐색이 진행된다는 것이다.
여기서 거리란 시작 정점으로부터 어떤 정점까지의 경로 중 가장 짧은 경로의 길이를 뜻한다.
즉, 너비우선탐색은 거리가 d인 정점들을 모두 방문한 후, 거리가 d+1인 정점들을 모두 방문하게 된다.

"""

from queue import Queue

def bfs_mat(graph, start):
	q = Queue() # 큐 초기화
	visited[start] = True
	print(f"{start} is visited")

	q.put(start) # 시작 정점을 큐에 저장
	while not q.empty():
		start = q.get() # 큐에서 정점 추출
		for end in range(0, graph.vertexes): # 인접 정점 탐색
			if graph.graph[start][end] and not visited[end]:
				visited[end] = True # 방문 표시
				print(f"{end}")
				q.put(end) # 방문한 정점을 큐에 저장