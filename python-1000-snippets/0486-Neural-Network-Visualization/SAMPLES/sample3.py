# sample3.py
# Generate a textual visualization of a network layer by layer description.


def render_network(layers):
    lines = []
    max_width = max(layers)
    for i, size in enumerate(layers):
        padding = (max_width - size) // 2
        line = " " * padding + "O " * size
        lines.append(line.strip())
    return "\n".join(lines)


def main() -> None:
    layers = [4, 8, 6, 2]
    print("Neural Network Textual Visualization")
    print(render_network(layers))


if __name__ == '__main__':
    main()
