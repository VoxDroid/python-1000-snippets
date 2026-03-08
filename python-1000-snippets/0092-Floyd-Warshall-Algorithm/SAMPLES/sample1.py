# sample1.py
# Basic Floyd-Warshall demonstration

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
    g = [
        [0,4,8,inf],
        [inf,0,2,5],
        [inf,inf,0,5],
        [inf,inf,inf,0]
    ]
    res = floyd_warshall(g)
    for row in res:
        print(row)
