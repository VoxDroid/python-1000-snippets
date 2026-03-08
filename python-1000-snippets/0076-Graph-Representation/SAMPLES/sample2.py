# sample2.py
# BFS traversal of graph

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)
    def bfs(self, start):
        visited = set([start])
        q = deque([start])
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nbr in self.graph.get(node, []):
                if nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)
        return order

if __name__ == '__main__':
    g = Graph()
    for u,v in [(0,1),(0,2),(1,2),(2,3)]:
        g.add_edge(u,v)
    print('bfs order', g.bfs(0))
