# sample3.py
# Floyd-Warshall with path reconstruction

def floyd_warshall_paths(graph):
    V = len(graph)
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]
    next_node = [[None if graph[i][j] == float('infinity') else j for j in range(V)] for i in range(V)]
    for i in range(V):
        dist[i][i] = 0
        next_node[i][i] = i
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]
    return dist, next_node

def reconstruct_path(next_node, u, v):
    if next_node[u][v] is None:
        return None
    path = [u]
    while u != v:
        u = next_node[u][v]
        path.append(u)
    return path

if __name__ == '__main__':
    inf = float('infinity')
    g = [
        [0,4,inf],
        [inf,0,1],
        [inf,inf,0]
    ]
    dist, nxt = floyd_warshall_paths(g)
    print('dist', dist)
    print('path 0->2', reconstruct_path(nxt,0,2))
