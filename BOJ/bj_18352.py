import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

N,M,K,X = map(int, input().split())

graph = defaultdict(set)
vertices = set()
for _ in range(M):
	a,b = map(int, input().split())
	graph[a].add(b)
	vertices.add(a)
	vertices.add(b)
def dijkstra(graph, start) -> list:
	distances_from_start = dict([(key, M) for key in vertices])
	distances_from_start[start] = 0
	minheap = []

	heappush(minheap, (0,start))
	while len(minheap) != 0:
		current_dist, vertex = heappop(minheap)
		for adj_v in graph[vertex]:
			new_dist = 1 + current_dist
			if new_dist < distances_from_start[adj_v]:
				distances_from_start[adj_v] = new_dist
				heappush(minheap,(new_dist,adj_v))

	cities = list(filter(lambda distance_from_start: distance_from_start[1] == K, distances_from_start.items()))
	return sorted(cities) if len(cities) != 0 else [(-1,-1)]

for city,distance in dijkstra(graph,X):
	print(city)