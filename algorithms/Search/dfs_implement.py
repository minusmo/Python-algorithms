class DFS:
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
        self.visited = [] #queue
        self.needVisit = [] #stack

    def dfs_search(self, start_node):
        self.needVisit.append(start_node)

        while not len(self.needVisit) == 0:
            need_visit = self.needVisit.pop()
            if not need_visit in self.visited:
                self.visited.append(need_visit)
                self.needVisit.extend(self.hashMap[need_visit])
        print(self.visited)
        
dfs = DFS()
dfs.dfs_search('a')
