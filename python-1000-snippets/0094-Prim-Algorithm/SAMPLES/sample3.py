# sample3.py
# Prim’s using adjacency matrix (dense graph)

import heapq

def prim_matrix(mat, start):
    V = len(mat)
    visited = {start}
    edges = [(mat[start][v], start, v) for v in range(V) if v!=start]
    heapq.heapify(edges)
    mst = []
    while edges and len(visited) < V:
        w,u,v = heapq.heappop(edges)
        if v in visited:
            continue
        visited.add(v)
        mst.append((u,v,w))
        for nxt in range(V):
            if nxt not in visited:
                heapq.heappush(edges,(mat[v][nxt], v, nxt))
    return mst

if __name__ == '__main__':
    inf = float('infinity')
    mat = [
        [0,2,inf],
        [2,0,3],
        [inf,3,0]
    ]
    print('MST matrix', prim_matrix(mat,0))
