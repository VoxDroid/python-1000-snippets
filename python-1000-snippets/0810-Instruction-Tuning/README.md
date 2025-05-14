# Instruction Tuning

## Description
This snippet demonstrates Instruction Tuning for an e-commerce platform, fine-tuning a language model to follow customer service instructions.

## Code
```python
# Instruction Tuning for customer service
# Note: Requires `transformers`, `torch`. Install with `pip install transformers torch`
try:
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM

    # Instruction tuning model
    class CustomerServiceTuner:
        def __init__(self):
            # Initialize tokenizer and model
            self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
            self.model = AutoModelForCausalLM.from_pretrained("gpt2")

            # Fix: GPT-2 has no pad_token by default
            self.tokenizer.pad_token = self.tokenizer.eos_token
            self.model.config.pad_token_id = self.tokenizer.pad_token_id

        def preprocess(self, instructions: list, responses: list) -> dict:
            # Prepare instruction-response pairs
            inputs = [f"Instruction: {i}\nResponse: {r}" for i, r in zip(instructions, responses)]
            encodings = self.tokenizer(inputs, return_tensors="pt", padding=True, truncation=True)
            return encodings

        def simulate_tune(self, instructions: list, responses: list) -> None:
            # Simulate one tuning step
            encodings = self.preprocess(instructions, responses)
            outputs = self.model(**encodings, labels=encodings.input_ids)
            print("Loss:", outputs.loss.item())

    # Simulate instruction tuning
    def tune_customer_service(instructions: list, responses: list) -> None:
        model = CustomerServiceTuner()
        model.simulate_tune(instructions, responses)

    # Example usage
    instructions = ["Answer politely", "Provide price"]
    responses = ["Of course, how may I assist you?", "The price is $99."]
    tune_customer_service(instructions, responses)

except ImportError:
    print("Mock Output: Loss: ~5.7")
```

## Output
```
Mock Output: Loss: ~5.7
```
*(Real output with `transformers`, `torch`: `Loss: <float>`)*

## Explanation
- **Purpose**: Instruction Tuning fine-tunes models to follow specific instructions, improving task performance.
- **Real-World Use Case**: In an e-commerce platform, it tunes a model for polite and accurate customer service responses, enhancing support automation.
- **Code Breakdown**:
  - The `CustomerServiceTuner` class uses a GPT-2 model.
  - The `preprocess` method prepares instruction-response pairs.
  - The `simulate_tune` method simulates a tuning step.
  - The `tune_customer_service` function simulates tuning.
- **Challenges**: Curating instruction data, avoiding overfitting, and computational cost.
- **Integration**: Works with Language Model Pretraining (Snippet 809) and Dialogue System (Snippet 801) for language tasks.
- **Complexity**: O(n*t) for n tokens and t transformer layers.
- **Best Practices**: Use diverse instructions, monitor loss, and validate responses.
- **Extensions**: Scale tuning or integrate with chatbot systems.