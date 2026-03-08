# sample2.py
# Running Kruskal on a disconnected graph

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
    edges=[]
    for u in graph:
        for v,w in graph[u]:
            if u<v: edges.append((w,u,v))
    edges.sort()
    uf=UnionFind(V)
    mst=[]
    for w,u,v in edges:
        if uf.find(u)!=uf.find(v):
            uf.union(u,v)
            mst.append((u,v,w))
    return mst

if __name__ == '__main__':
    g = {0:[(1,1)], 1:[(0,1)], 2:[(3,2)], 3:[(2,2)]}
    print('MST of disconnected', kruskal(g,4))
