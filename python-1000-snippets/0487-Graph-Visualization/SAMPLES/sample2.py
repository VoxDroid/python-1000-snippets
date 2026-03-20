# sample2.py
# Export a graph to a Graphviz DOT file (text-based graph format).

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "../../temp/graph.dot")


def build_graph_edges():
    # Return a list of undirected edges in a small example graph.
    return [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("D", "E"),
    ]


def write_dot(path: str, edges: list[tuple[str, str]]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write("graph G {\n")
        for u, v in edges:
            f.write(f"    \"{u}\" -- \"{v}\";\n")
        f.write("}\n")


def main() -> None:
    edges = build_graph_edges()
    write_dot(OUTPUT_PATH, edges)
    print("Graph written to", OUTPUT_PATH)
    print("You can render it with Graphviz (dot) if installed:")
    print(f"  dot -Tpng {OUTPUT_PATH} -o temp/graph.png")


if __name__ == "__main__":
    main()
