# sample2.py
# Dijkstra with path reconstruction

import heapq

def dijkstra_with_path(graph, start):
    dist = {v: float('infinity') for v in graph}
    prev = {v: None for v in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d,u = heapq.heappop(pq)
        if d>dist[u]: continue
        for v,w in graph[u]:
            if dist[u]+w < dist[v]:
                dist[v] = dist[u]+w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev

def reconstruct(prev, target):
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    return list(reversed(path))

if __name__ == '__main__':
    g = {0:[(1,1),(2,4)],1:[(2,2),(3,5)],2:[(3,1)],3:[]}
    dist, prev = dijkstra_with_path(g,0)
    print('distances', dist)
    print('path to 3', reconstruct(prev,3))
