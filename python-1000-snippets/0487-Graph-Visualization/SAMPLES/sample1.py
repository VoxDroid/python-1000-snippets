# sample1.py
# Build a small graph and print its adjacency list.

from __future__ import annotations


def build_example_graph():
    # Graph represented as an adjacency list (node -> set of neighbors)
    graph: dict[str, set[str]] = {
        "A": {"B", "C"},
        "B": {"A", "D"},
        "C": {"A", "D"},
        "D": {"B", "C", "E"},
        "E": {"D"},
    }
    return graph


def print_adjacency_list(graph: dict[str, set[str]]) -> None:
    for node in sorted(graph):
        neighbors = ", ".join(sorted(graph[node]))
        print(f"{node}: {neighbors}")


def main() -> None:
    graph = build_example_graph()
    print("Adjacency list:")
    print_adjacency_list(graph)
    edge_count = sum(len(neighbors) for neighbors in graph.values()) // 2
    print(f"Nodes: {len(graph)}, Edges: {edge_count}")


if __name__ == "__main__":
    main()
