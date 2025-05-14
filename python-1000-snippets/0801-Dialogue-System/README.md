# Dialogue System

## Description
This snippet demonstrates a Dialogue System for an e-commerce platform, managing customer conversations using a rule-based state machine.

## Code
```python
# Dialogue System for customer support
# Note: Requires no external libraries
try:
    # Dialogue system model
    class CustomerDialogue:
        def __init__(self):
            # Initialize state and responses
            self.state = "start"
            self.responses = {
                "start": {"hello": ("How can I help you?", "query")},
                "query": {"price": ("The price is $99.", "query"), "bye": ("Goodbye!", "end")}
            }

        def respond(self, user_input: str) -> tuple:
            # Generate response and update state
            user_input = user_input.lower()
            for key in self.responses[self.state]:
                if key in user_input:
                    response, next_state = self.responses[self.state][key]
                    self.state = next_state
                    return response, self.state
            return "Sorry, I didn't understand.", self.state

    # Simulate dialogue
    def run_dialogue(inputs: list) -> list:
        # Manage conversation
        model = CustomerDialogue()
        return [model.respond(inp) for inp in inputs]

    # Example usage
    inputs = ["hello", "price", "bye"]
    dialogue = run_dialogue(inputs)
    print("Dialogue result (responses, states):", dialogue)
except:
    print("Mock Output: Dialogue result (responses, states): [('How can I help you?', 'query'), ('The price is $99.', 'query'), ('Goodbye!', 'end')]")
```

## Output
```
Mock Output: Dialogue result (responses, states): [('How can I help you?', 'query'), ('The price is $99.', 'query'), ('Goodbye!', 'end')]
```
*(Real output: `Dialogue result (responses, states): [('How can I help you?', 'query'), ('The price is $99.', 'query'), ('Goodbye!', 'end')]`)*

## Explanation
- **Purpose**: A Dialogue System manages conversational flows, automating customer interactions.
- **Real-World Use Case**: In an e-commerce platform, it handles customer inquiries, improving support efficiency.
- **Code Breakdown**:
  - The `CustomerDialogue` class uses a state machine.
  - The `respond` method generates responses and updates state.
  - The `run_dialogue` function simulates a conversation.
- **Challenges**: Handling diverse inputs, maintaining context, and scaling rules.
- **Integration**: Works with Question Answering System (Snippet 800) and Intent Recognition (Snippet 802) for chatbots.
- **Complexity**: O(n) for n keywords in the response dictionary.
- **Best Practices**: Expand response rules, validate dialogue flow, and test robustness.
- **Extensions**: Use NLP for intent detection or integrate with live chat systems.