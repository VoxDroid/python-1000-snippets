# sample3.py
# Graph with unreachable node

import heapq

def dijkstra(graph, start):
    dist = {v: float('infinity') for v in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d,u = heapq.heappop(pq)
        if d>dist[u]: continue
        for v,w in graph[u]:
            if dist[u]+w < dist[v]:
                dist[v] = dist[u]+w
                heapq.heappush(pq, (dist[v], v))
    return dist

if __name__ == '__main__':
    g = {0:[(1,1)],1:[(2,2)],2:[],3:[(0,1)]}  # node 3 unreachable from 0
    print('dists from 0', dijkstra(g,0))
