# sample3.py
# Illustrate union-find operations separately

class UnionFind:
    def __init__(self, n):
        self.parent=list(range(n))
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        self.parent[self.find(x)] = self.find(y)

if __name__ == '__main__':
    uf=UnionFind(5)
    print('initial parents', uf.parent)
    uf.union(0,1);
    uf.union(1,2);
    print('parents after unions', uf.parent)
    print('find 2', uf.find(2), 'find 0', uf.find(0))
