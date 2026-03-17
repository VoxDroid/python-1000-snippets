"""Compute centrality metrics on a small social network graph."""

try:
    import networkx as nx
except ImportError as e:
    raise SystemExit("networkx is required; install with `pip install networkx`.\n" + str(e))

# Build a small undirected social network graph
G = nx.Graph()
G.add_edges_from([
    ("Alice", "Bob"),
    ("Alice", "Claire"),
    ("Bob", "Claire"),
    ("Bob", "David"),
    ("Claire", "Eve"),
    ("Eve", "Frank"),
])

print("Nodes:", list(G.nodes()))
print("Edges:", list(G.edges()))

# Centrality metrics
print("\nDegree centrality:", nx.degree_centrality(G))
print("Betweenness centrality:", nx.betweenness_centrality(G))
print("Closeness centrality:", nx.closeness_centrality(G))
