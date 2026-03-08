# sample1.py
# Basic Prim’s algorithm MST

import heapq

def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [(w, start, v) for v, w in graph[start]]
    heapq.heapify(edges)
    while edges:
        w, u, v = heapq.heappop(edges)
        if v in visited:
            continue
        visited.add(v)
        mst.append((u, v, w))
        for next_v, next_w in graph[v]:
            if next_v not in visited:
                heapq.heappush(edges, (next_w, v, next_v))
    return mst

if __name__ == '__main__':
    g = {
        0: [(1,4),(2,8)],
        1: [(0,4),(2,2),(3,5)],
        2: [(0,8),(1,2),(3,5)],
        3: [(1,5),(2,5)]
    }
    print('MST', prim(g,0))
