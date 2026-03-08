# 0095-Topological-Sort Cheatsheet

- Topological sorting applies only to Directed Acyclic Graphs (DAGs).
- Can be implemented via DFS (post-order) or Kahn’s algorithm (indegree queue).
- DFS version:
  ```python
  def topo(graph):
      visited, stack = set(), []
      def dfs(u):
          visited.add(u)
          for v in graph[u]:
              if v not in visited:
                  dfs(v)
          stack.append(u)
      for u in graph:
          if u not in visited:
              dfs(u)
      return stack[::-1]
  ```
- Kahn’s algorithm:
  ```python
  indeg = {u:0 for u in graph}
  for u in graph:
      for v in graph[u]: indeg[v]+=1
  q = [u for u in graph if indeg[u]==0]
  order = []
  while q:
      u=q.pop(0)
      order.append(u)
      for v in graph[u]:
          indeg[v]-=1
          if indeg[v]==0: q.append(v)
  ```
- Use cycle detection: graph with remaining nodes and indegree >0 indicates cycle.
- Common uses: scheduling, resolution of dependencies, build order.
