# sample3.py
# Detect cycle in directed graph using DFS recursion stack

def has_cycle(graph):
    visited = set()
    recstack = set()
    def dfs(v):
        visited.add(v)
        recstack.add(v)
        for neigh in graph.get(v, []):
            if neigh not in visited:
                if dfs(neigh):
                    return True
            elif neigh in recstack:
                return True
        recstack.remove(v)
        return False
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

if __name__ == '__main__':
    g1 = {0:[1],1:[2],2:[0]}  # cycle
    g2 = {0:[1],1:[2],2:[]}   # acyclic
    print('g1 has cycle?', has_cycle(g1))
    print('g2 has cycle?', has_cycle(g2))
