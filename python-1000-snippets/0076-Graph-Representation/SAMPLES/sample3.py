# sample3.py
# Find path between two nodes using DFS

class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)
    def find_path(self, start, goal, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == goal:
            return path
        for node in self.graph.get(start, []):
            if node not in path:
                newpath = self.find_path(node, goal, path)
                if newpath:
                    return newpath
        return None

if __name__ == '__main__':
    g = Graph()
    for u,v in [(0,1),(0,2),(1,2),(2,3)]:
        g.add_edge(u,v)
    print('path 0->3', g.find_path(0,3))
