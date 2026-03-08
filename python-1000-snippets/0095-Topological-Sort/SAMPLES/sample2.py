# sample2.py
# Kahn's algorithm with cycle detection

def kahn(graph):
    indeg = {u:0 for u in graph}
    for u in graph:
        for v in graph[u]:
            indeg[v] = indeg.get(v,0) + 1
    q = [u for u in graph if indeg[u]==0]
    order = []
    while q:
        u = q.pop(0)
        order.append(u)
        for v in graph.get(u, []):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(order) != len(graph):
        return None  # cycle
    return order

if __name__ == '__main__':
    g = {0:[1],1:[2],2:[0]}  # cycle
    print('kahn cycle', kahn(g))
    g2 = {0:[1],1:[2],2:[]}
    print('kahn no cycle', kahn(g2))
