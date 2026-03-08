# sample3.py
# Bellman-Ford with path reconstruction

def bellman_ford_with_path(graph, start):
    dist = {v: float('infinity') for v in graph}
    prev = {v: None for v in graph}
    dist[start] = 0
    for _ in range(len(graph)-1):
        for u in graph:
            for v,w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
    for u in graph:
        for v,w in graph[u]:
            if dist[u] + w < dist[v]:
                return None, None
    return dist, prev

def path(prev, target):
    p = []
    while target is not None:
        p.append(target)
        target = prev[target]
    return list(reversed(p))

if __name__ == '__main__':
    g = {0:[(1,5),(2,2)],1:[(3,1)],2:[(1,1),(3,7)],3:[]}
    d,pred = bellman_ford_with_path(g,0)
    print('distances', d)
    print('path to 3', path(pred,3))
