# sample1.py
# Basic Bellman-Ford computation

def bellman_ford(graph, start):
    distances = {v: float('infinity') for v in graph}
    distances[start] = 0
    for _ in range(len(graph)-1):
        for u in graph:
            for v,w in graph[u]:
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
    # negative cycle check
    for u in graph:
        for v,w in graph[u]:
            if distances[u] + w < distances[v]:
                return None
    return distances

if __name__ == '__main__':
    g = {0:[(1,4),(2,8)],1:[(2,2),(3,5)],2:[(3,5)],3:[(1,-1)]}
    print('distances', bellman_ford(g,0))
