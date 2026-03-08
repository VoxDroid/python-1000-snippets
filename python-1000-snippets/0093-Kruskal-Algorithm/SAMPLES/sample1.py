# sample1.py
# Basic MST computation

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def kruskal(graph, V):
    edges = []
    for u in graph:
        for v,w in graph[u]:
            if u < v:
                edges.append((w,u,v))
    edges.sort()
    uf = UnionFind(V)
    mst = []
    for w,u,v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u,v)
            mst.append((u,v,w))
    return mst

if __name__ == '__main__':
    g = {
        0:[(1,4),(2,8)],
        1:[(0,4),(2,2),(3,5)],
        2:[(0,8),(1,2),(3,5)],
        3:[(1,5),(2,5)]
    }
    print('MST', kruskal(g,4))
