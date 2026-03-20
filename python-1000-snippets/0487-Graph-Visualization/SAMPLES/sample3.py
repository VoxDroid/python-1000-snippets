# sample3.py
# Compute basic graph statistics (degree centrality) for a small graph.


def build_graph():
    return {
        "A": {"B", "C"},
        "B": {"A", "D"},
        "C": {"A", "D"},
        "D": {"B", "C", "E"},
        "E": {"D"},
    }


def degree_centrality(graph: dict[str, set[str]]) -> dict[str, float]:
    # Degree / (n-1)
    n = len(graph)
    return {node: len(neighbors) / (n - 1) for node, neighbors in graph.items()}


def main() -> None:
    graph = build_graph()
    centrality = degree_centrality(graph)
    sorted_nodes = sorted(centrality.items(), key=lambda item: item[1], reverse=True)
    print("Degree centrality:")
    for node, score in sorted_nodes:
        print(f"  {node}: {score:.2f}")


if __name__ == "__main__":
    main()
