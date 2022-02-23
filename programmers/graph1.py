from queue import PriorityQueue

def solution(n, edge):
    farest_nodes = 0
    min_distances = get_min_distances(n, edge)
    for distance in min_distances:
        if distance == max(min_distances):
            farest_nodes += 1
    return farest_nodes

def get_min_distances(n, edge):
    graph = get_graph(n, edge)
    distances = initialize_distances(n)
    need_visited = PriorityQueue()
    need_visited.put(Edge(0, 0))
    
    while not need_visited.empty():
        current_distance, current_node = need_visited.get()
        
        if current_distance > distances[current_node]:
            continue
        
        for near_node in graph[current_node]:
            distance = current_distance + 1
            if distances[near_node] > distance:
                distances[near_node] = distance
                need_visited.put(Edge(distance, near_node))
    return distances

def get_graph(n, edge):
    graph = [[] for _ in range(n)]
    for source, target in edge:
        graph[source-1].append(target-1)
        graph[target-1].append(source-1)
    return graph

def initialize_distances(n):
    distances = [19999] * n
    distances[0] = 0
    return distances

def Edge(distance, node):
    return (distance, node)