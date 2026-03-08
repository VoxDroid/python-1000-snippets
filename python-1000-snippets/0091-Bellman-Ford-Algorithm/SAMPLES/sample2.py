# sample2.py
# Detect negative-weight cycle

def bellman_ford(graph, start):
    dist = {v: float('infinity') for v in graph}
    dist[start] = 0
    for _ in range(len(graph)-1):
        for u in graph:
            for v,w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    for u in graph:
        for v,w in graph[u]:
            if dist[u] + w < dist[v]:
                return None
    return dist

if __name__ == '__main__':
    # create negative cycle 1->2->3->1 with total weight -1
    g = {1:[(2,1)],2:[(3,-2)],3:[(1,0)]}
    print('negative cycle result', bellman_ford(g,1))
