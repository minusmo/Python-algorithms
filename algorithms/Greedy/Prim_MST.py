'''
Prim's Algorithm은 MST(Minimum Spanning Tree)
를 만드는 알고리즘으로, 그리디 접근법을 사용한다.
정점기반의 접근방식(node based approach)으로, 
Ranking function으로 아직 MST에 속하지 않은 정점들 중 가장 가까운 것을 고른다.
'''
# graph is given as adjacency matrix

import sys
class Prim:
    def __init__(self, vertices, graph):
        self.V = vertices
        self.graph = graph
        
    def prim_mst(self):
        # while NOT solved yet
        # choose the closest vertex not in mst set
        # if mst set is |V| exit else repeat
        dist_from_mstSet = [sys.maxsize] * self.V
        dist_from_mstSet[0] = 0
        mstSet = [False] * self.V
        parent = [None] * self.V
        parent[0] = -1
        mstSetSize = 0
        while not mstSetSize == self.V:
            closest_vertex = self.get_closest_vertex(dist_from_mstSet, mstSet)
            mstSet[closest_vertex] = True
            mstSetSize += 1
            self.update_dist_from_mstSet(closest_vertex, dist_from_mstSet, parent, mstSet)
    
    def get_closest_vertex(self, dist_from_mstSet, mstSet):
        min_dist = sys.maxsize
        closest_one = -1
        for vertex in range(self.V):
            dist = dist_from_mstSet[vertex]
            if dist < min_dist and mstSet[vertex] == False:
                min_dist = dist
                closest_one = vertex
        return closest_one
    
    def update_dist_from_mstSet(self, closest_vertex, dist_from_mstSet, parent, mstSet):
        for i in range(self.V):
            if self.graph[closest_vertex][i] < dist_from_mstSet[i] and mstSet[i] == False:
                dist_from_mstSet[i] = self.graph[closest_vertex][i]
                parent[i] = closest_vertex