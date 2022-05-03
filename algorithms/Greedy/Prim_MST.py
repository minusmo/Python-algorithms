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
        mstSet = []
        vertices_in_mstSet = [False] * self.V
        dist_from_mstSet[0] = 0
        while not len(mstSet) == self.V:
            closest_vertex = self.get_closest_vertex(dist_from_mstSet, vertices_in_mstSet)
            vertices_in_mstSet[closest_vertex] = True
            self.update_dist_from_mstSet(closest_vertex, dist_from_mstSet)
            self.add_to_mstSet(closest_vertex, mstSet)