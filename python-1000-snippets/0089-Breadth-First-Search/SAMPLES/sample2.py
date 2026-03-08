# sample2.py
# Find shortest path between two nodes in unweighted graph

from collections import deque

def shortest_path(graph, start, goal):
    visited = {start}
    queue = deque([(start, [start])])
    while queue:
        v, path = queue.popleft()
        if v == goal:
            return path
        for nbr in graph.get(v, []):
            if nbr not in visited:
                visited.add(nbr)
                queue.append((nbr, path+[nbr]))
    return None

if __name__ == '__main__':
    g = {0:[1,2],1:[0,3],2:[0,3],3:[1,2]}
    print('path 0->3', shortest_path(g,0,3))
