"""Detect communities and clustering coefficient in a social network."""

try:
    import networkx as nx
except ImportError as e:
    raise SystemExit("networkx is required; install with `pip install networkx`. " + str(e))

# Create a graph with two clear communities
G = nx.Graph()
G.add_edges_from([
    ("A", "B"), ("A", "C"), ("B", "C"),  # community 1
    ("D", "E"), ("D", "F"), ("E", "F"),  # community 2
    ("C", "D"),  # bridge between communities
])

# Use greedy modularity communities (networkx >= 2.2)
try:
    communities = list(nx.algorithms.community.greedy_modularity_communities(G))
    print("Communities:", [set(c) for c in communities])
except AttributeError:
    print("Community detection not available in this(networkx) version.")

# Clustering coefficient
print("Clustering coefficient:", nx.clustering(G))
print("Average clustering:", nx.average_clustering(G))
