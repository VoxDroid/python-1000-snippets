"""Compute connected components and shortest path in a social graph."""

try:
    import networkx as nx
except ImportError as e:
    raise SystemExit("networkx is required; install with `pip install networkx`. " + str(e))

# Create a graph with two connected components
G = nx.Graph()
G.add_edges_from([
    ("A", "B"),
    ("B", "C"),
    ("C", "D"),
    ("E", "F"),
])

components = list(nx.connected_components(G))
print("Connected components:", components)

# Find shortest path in the first component
source, target = "A", "D"
print(f"Shortest path {source}->{target}:", nx.shortest_path(G, source=source, target=target))

# Handle case where nodes are disconnected
try:
    print("Shortest path A->F:", nx.shortest_path(G, source="A", target="F"))
except nx.NetworkXNoPath:
    print("No path between A and F (different components)")
