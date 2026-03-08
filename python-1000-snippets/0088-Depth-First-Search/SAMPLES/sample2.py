# sample2.py
# Iterative DFS using explicit stack

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            # push neighbors in reverse for same order as recursive
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    return order

if __name__ == '__main__':
    g = {0:[1,2],1:[0,3],2:[0],3:[1]}
    print('dfs iter', dfs_iterative(g,0))
