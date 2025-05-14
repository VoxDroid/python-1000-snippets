# Knowledge Graph Construction

## Description
This snippet demonstrates Knowledge Graph Construction for an e-commerce platform, building a graph of products and categories to support semantic search.

## Code
```python
# Knowledge Graph Construction for semantic search
# Note: Requires `networkx`. Install with `pip install networkx`
try:
    import networkx as nx

    # Knowledge graph model
    class ProductKnowledgeGraph:
        def __init__(self):
            # Initialize directed graph
            self.graph = nx.DiGraph()

        def add_relations(self, products: list, categories: list, relations: list) -> None:
            # Add nodes and edges
            self.graph.add_nodes_from(products, type='product')
            self.graph.add_nodes_from(categories, type='category')
            self.graph.add_edges_from(relations)

        def get_related_products(self, category: str) -> list:
            # Find products in a category
            return [n for n in self.graph.predecessors(category) if self.graph.nodes[n]['type'] == 'product']

    # Simulate knowledge graph construction
    def build_product_graph(products: list, categories: list, relations: list) -> list:
        # Build and query knowledge graph
        model = ProductKnowledgeGraph()
        model.add_relations(products, categories, relations)
        return model.get_related_products(categories[0])

    # Example usage
    products = ['p1', 'p2', 'p3']
    categories = ['c1', 'c2']
    relations = [('p1', 'c1'), ('p2', 'c1'), ('p3', 'c2')]
    related = build_product_graph(products, categories, relations)
    print("Knowledge graph result (related products):", related)
except ImportError:
    print("Mock Output: Knowledge graph result (related products): ['p1', 'p2']")
```

## Output
```
Mock Output: Knowledge graph result (related products): ['p1', 'p2']
```
*(Real output with `networkx`: `Knowledge graph result (related products): ['p1', 'p2']`)*

## Explanation
- **Purpose**: Knowledge Graph Construction organizes entities and relationships into a graph, enabling semantic queries.
- **Real-World Use Case**: In an e-commerce platform, it builds a product-category graph to support semantic search, improving product discovery.
- **Code Breakdown**:
  - The `ProductKnowledgeGraph` class creates a directed graph.
  - The `add_relations` method adds nodes and edges.
  - The `get_related_products` method queries related products.
  - The `build_product_graph` function simulates construction.
- **Challenges**: Defining relations, scaling graphs, and ensuring data quality.
- **Integration**: Works with Hypergraph Processing (Snippet 796) and Entity Resolution (Snippet 798) for knowledge systems.
- **Complexity**: O(n + e) for n nodes and e edges.
- **Best Practices**: Validate relations, visualize graphs, and preprocess data.
- **Extensions**: Add more entity types or integrate with search engines.