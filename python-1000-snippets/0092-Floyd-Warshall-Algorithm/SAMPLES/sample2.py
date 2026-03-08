# sample2.py
# Detect negative cycle using Floyd-Warshall

def floyd_warshall(graph):
    V = len(graph)
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]
    for i in range(V):
        dist[i][i] = 0
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

if __name__ == '__main__':
    inf = float('infinity')
    # graph with negative cycle 0->1->2->0 weights -1,-1,-1
    g = [
        [0, -1, inf],
        [inf, 0, -1],
        [-1, inf, 0]
    ]
    res = floyd_warshall(g)
    print('diag', [res[i][i] for i in range(len(res))])
    print('negative cycle?' , any(res[i][i] < 0 for i in range(len(res))))
