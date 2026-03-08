# sample1.py
# Basic BFS traversal

from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []
    while queue:
        v = queue.popleft()
        order.append(v)
        for nbr in graph.get(v, []):
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)
    return order

if __name__ == '__main__':
    g = {0:[1,2],1:[0,3],2:[0],3:[1]}
    print('bfs', bfs(g,0))
