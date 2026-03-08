# sample1.py
# Recursive DFS traversal

def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    result = [vertex]
    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result

if __name__ == '__main__':
    graph = {0: [1,2], 1: [0,3], 2: [0], 3: [1]}
    print('dfs from 0', dfs(graph, 0))
