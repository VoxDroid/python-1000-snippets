# sample2.py
# Prim algorithm on disconnected graph

import heapq

def prim(graph, start):
    mst=[]
    visited=set([start])
    edges=[(w,start,v) for v,w in graph[start]]
    heapq.heapify(edges)
    while edges:
        w,u,v=heapq.heappop(edges)
        if v in visited: continue
        visited.add(v)
        mst.append((u,v,w))
        for nv,nw in graph[v]:
            if nv not in visited:
                heapq.heappush(edges,(nw,v,nv))
    return mst

if __name__ == '__main__':
    g = {0:[(1,1)],1:[(0,1)],2:[(3,2)],3:[(2,2)]}
    print('MST component', prim(g,0))
