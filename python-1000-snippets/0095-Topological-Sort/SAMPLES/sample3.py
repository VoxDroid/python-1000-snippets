# sample3.py
# Use topological sort to schedule tasks with prerequisites

def topo_sort(graph):
    visited=set();stack=[]
    def dfs(u):
        visited.add(u)
        for v in graph.get(u,[]):
            if v not in visited:
                dfs(v)
        stack.append(u)
    for u in graph:
        if u not in visited:
            dfs(u)
    return stack[::-1]

if __name__ == '__main__':
    tasks = {'cook':[], 'eat':['cook'], 'clean':['eat'], 'shop':[]}
    print('task order', topo_sort(tasks))
