# sample1.py
# DFS-based topological sort

def topo_sort(graph):
    visited = set()
    stack = []
    def dfs(u):
        visited.add(u)
        for v in graph.get(u, []):
            if v not in visited:
                dfs(v)
        stack.append(u)
    for u in graph:
        if u not in visited:
            dfs(u)
    return stack[::-1]

if __name__ == '__main__':
    g = {0:[1,2],1:[3],2:[3],3:[]}
    print('order', topo_sort(g))
