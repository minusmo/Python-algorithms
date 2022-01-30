class BFS:
    def __init__(self):
        self.hashMap = {
            'a': ['b', 'c'],
            'b': ['a', 'd'],
            'c': ['a', 'g', 'h', 'i'],
            'd': ['b', 'e', 'f'],
            'e': ['d'],
            'f': ['d'],
            'g': ['c'],
            'h': ['c'],
            'i': ['c', 'j'],
            'j': ['i'],
            }
        self.visited = []
        self.needVisit = []

    def bfs_search(self, start_node):
        self.needVisit.append(start_node)

        while not len(self.needVisit) == 0:
            need_visit = self.needVisit.pop(0)
            if not need_visit in self.visited:
                self.visited.append(need_visit)
                self.needVisit.extend(self.hashMap[need_visit])
        print(self.visited)
        

bfs = BFS()
bfs.bfs_search('a')
