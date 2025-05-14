# Question Answering System

## Description
This snippet demonstrates a Question Answering System for an e-commerce platform, answering customer queries about products using a simple keyword-based approach.

## Code
```python
# Question Answering System for product queries
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np

    # Question answering model
    class ProductQA:
        def __init__(self, knowledge_base: dict):
            # Map of canonical key -> list of aliases
            self.aliases = {
                "price": ["price", "cost", "how much"],
                "availability": ["availability", "available", "in stock"]
            }
            self.kb = knowledge_base

        def answer(self, question: str) -> str:
            question = question.lower()
            for key, keywords in self.aliases.items():
                if any(k in question for k in keywords):
                    return self.kb.get(key, "Sorry, I don't have an answer for that.")
            return "Sorry, I don't have an answer for that."

    # Simulate question answering
    def answer_product_questions(kb: dict, questions: list) -> list:
        # Answer customer questions
        model = ProductQA(kb)
        return [model.answer(q) for q in questions]

    # Example usage
    kb = {"price": "The price is $99.", "availability": "In stock."}
    questions = ["What is the price?", "Is it available?"]
    answers = answer_product_questions(kb, questions)
    print("QA result (answers):", answers)
except ImportError:
    print("Mock Output: QA result (answers): ['The price is $99.', 'In stock.']")
```

## Output
```
Mock Output: QA result (answers): ['The price is $99.', 'In stock.']
```
*(Real output with `numpy`: `QA result (answers): ['The price is $99.', 'In stock.']`)*

## Explanation
- **Purpose**: A Question Answering System retrieves answers to user queries, automating customer support.
- **Real-World Use Case**: In an e-commerce platform, it answers product-related questions, reducing support workload.
- **Code Breakdown**:
  - The `ProductQA` class uses a keyword-based knowledge base.
  - The `answer` method matches questions to answers.
  - The `answer_product_questions` function simulates QA.
- **Challenges**: Handling complex queries, scaling knowledge bases, and ensuring accuracy.
- **Integration**: Works with Relation Extraction (Snippet 799) and Dialogue System (Snippet 801) for customer support.
- **Complexity**: O(n) for n keywords in the knowledge base.
- **Best Practices**: Expand knowledge base, validate answers, and preprocess queries.
- **Extensions**: Use NLP models like BERT or integrate with chatbots.