# sample1.py
# Build an undirected graph and display adjacency list

class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)
    def display(self):
        return self.graph

if __name__ == '__main__':
    g = Graph()
    edges = [(0,1),(0,2),(1,2),(2,3)]
    for u,v in edges:
        g.add_edge(u,v)
    print('adj list', g.display())
