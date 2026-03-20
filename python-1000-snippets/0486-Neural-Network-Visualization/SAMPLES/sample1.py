# sample1.py
# Define a feedforward neural network structure and print node/connection details.


def build_network(layers):
    nodes = []
    connections = []
    for i, size in enumerate(layers):
        nodes.extend([(i, j) for j in range(size)])
        if i > 0:
            for j in range(layers[i-1]):
                for k in range(size):
                    connections.append(((i-1, j), (i, k)))
    return nodes, connections


def main() -> None:
    layers = [3, 5, 2]
    nodes, connections = build_network(layers)
    print(f"Network layers: {layers}")
    print("Total nodes:", len(nodes))
    print("Total connections:", len(connections))
    print("Example connections:")
    for c in connections[:10]:
        print("  ", c)


if __name__ == '__main__':
    main()
