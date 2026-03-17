# sample3.py
# BFS iterator for a tree represented as nested dictionaries

class BFSTreeIterator:
    def __init__(self, tree):
        self.queue = [tree]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.queue:
            raise StopIteration
        node = self.queue.pop(0)
        children = node.get("children", [])
        self.queue.extend(children)
        return node["value"]


def main():
    tree = {
        "value": "root",
        "children": [
            {"value": "a", "children": [{"value": "a1"}, {"value": "a2"}]},
            {"value": "b", "children": [{"value": "b1"}]},
        ],
    }

    print("BFS order:", list(BFSTreeIterator(tree)))


if __name__ == "__main__":
    main()
